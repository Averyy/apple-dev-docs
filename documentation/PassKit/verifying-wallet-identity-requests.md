# Verifying Wallet identity requests

**Framework**: PassKit (Apple Pay and Wallet)

Decrypt and verify an in-app presentment request on your server.

#### Overview

Your server needs to decrypt and validate a mobile driver’s license (mDL) document that an app requests. The response contains the user information that you request, plus several security elements your server needs to validate the information to ensure it’s authentic.

##### Understand the Response Structure

The `PassKit` framework uses the encryption certificate you create in the developer portal, so only your server can decrypt the response. The framework encrypts the data by using hybrid public key encryption (HPKE) that RFC 9180 defines.

The framework encodes the HPKE envelope and underlying plaintext with concise binary object representation (CBOR) — a binary JSON-like format that RFC 8949 defines. Because the framework encrypts the response data by using HPKE, it doesn’t use session encryption as ISO 18013-5 section 9.1.1 defines. The encryption envelope contains two parts, the encryption metadata and the encrypted data. When you decrypt the data, you get a CBOR-encoded data structure that contains an `mdoc` response object that ISO 18013-5 defines.

In HPKE, the `info` parameter — a session transcript — isn’t part of the package that you send. The sender and recipient need to build the `info` parameter independently, and need to generate the same value to successfully decrypt it. The following shows the HPKE envelope format:

```other
HPKEEnvelope = {
    “algorithm”: tstr,    ; A value that's always “APPLE-HPKE-v1”.
    “params”: HPKEParams,
    “data”: bstr          ; The encrypted data.
}

HPKEParams = {
    “mode”: uint,         ; A value that's always 0.
    “pkEm”: bstr,         ; An ephemeral sender public key.
    “pkRHash”: bstr,      ; The SHA256 hash of the recipient public key.
    “infoHash”: bstr      ; The SHA256 hash of the HPKE info param.
}
```

The `infoHash` in the HPKE structure is the SHA256 hash of the session transcript during encryption to allow the recipient to verify they’re using the correct `info` parameter.

##### Build a Session Transcript

The session transcript is a CBOR structure you use during decryption and during validation of the device signature. The session transcript allows you to validate that the response payload belongs to a specific request that your app makes.

Neither the session transcript nor the fields in it are part of the response payload. You need to create the structure on your server. Before you create the session transcript structure, verify that the hash of your public key matches the `pkRHash` property in the HPKE envelope.

The session transcript structure includes the same [`nonce`](pkidentityrequest/nonce.md) and merchant identifier you use in your [`PKIdentityRequest`](pkidentityrequest.md), a team identifier, and the SHA256 hash of the public key of the server’s decryption certificate. The session transcript values need to match your app and developer account.

The API uses a modified version of the `SessionTranscript` structure that ISO 18013-5 section 9.1.5.1 defines. The API doesn’t use `DeviceEngagementBytes` and `AReaderKeyBytes`, so those elements are `nil`. The handover element contains the `AppleHandover` structure, as the following code example shows:

```other
SessionTranscript = [
    nil,           ; DeviceEngagementBytes isn't available.
    nil,           ; EReaderKeyBytes isn't available.        
    AppleHandover  ; A custom handover structure. 
]

AppleHandover = [
    “AppleIdentityPresentment_1.0”  ; The version number.
    nonce,                          ; The app-provided nonce you use.  
    merchantId,                     ; The merchant ID of the requesting client.  
    teamID,                         ; The team ID of the requesting client.
    pkRHash                         ; A SHA256 hash of the recipient public key, the same as in HPKEParams.
]
```

Compute the SHA256 hash of the session transcript to produce a value that matches the `infoHash` parameter in the HPKE envelope.

##### Decrypt the Hpke Envelope

Decryption requires the encrypted data parameter from the HPKE envelope, the session transcript you create, and your server’s private key. The private key needs to correspond to the encryption certificate you create in the developer portal. The info parameter is the session transcript. The `enc` parameter is the `pkEm` parameter in the HPKE envelope.

Use the inputs, along with the following HPKE options, to decrypt the encrypted data as the HPKE specification describes:

|  |  |
| --- | --- |
| KEM | DHKEM(P-256, HKDF-SHA256) |
| KDF | HKDF-SHA256 |
| AEAD | AES-128-GCM |

The output is a CBOR topics structure that wraps an ISO 18013-5 `mdoc` response structure.

```other
Topics = {
    “identity”: DeviceResponse      ; A DeviceResponse structure.
}

DeviceResponse = {
    "version": tstr,                ; A value that's always 1.0.
    "documents": [+Document],       ; A list of documents with a length of 1.
    "status": uint,                 ; A value that's always 0.
}
```

The identity value contains the `DeviceResponse` structure that ISO 18013-5 section 8.2.2.1.2.2 defines.

An `mdoc` response contains three sections you use to verify that the response is valid. The issuer-signed items contain the elements your app requests. The issuer authentication structure contains the issuing authority’s signature and the metadata you use to verify the response authenticity. The device authentication structure contains a signature from the iPhone that’s requesting the information.

```other
Document = {
    “docType”: DocType,                 ; The document type.
    “issuerSigned”: IssuerSigned,       ; The data elements the issuer signs.
    “deviceSigned”: DeviceSigned,       ; The data elements the mdoc signs.
    ? “errors”: Errors                 
}
```

Before using the elements, you need to verify they come from the issuer and device you expect.

##### Verify the Issuer Signature

You use issuer data authentication to verify that the `mdoc` comes from an issuing authority you trust, and to verify it hasn’t been tampered with since issuance. Refer to ISO 18013-5 section 9.1.2 for more information.

The signed issuer structure includes the data elements you request, and an issuer authentication property that contains the mobile security object (MSO) you use for verification.

First, you need to verify that the user information in the response matches the data from the issuing authority. The issuer’s signature includes an array of digests, or hashes, covering every element in the mDL. There can be more digests than you see in the issuer-signed items structure because you only receive signed items for each element your app requests. Compute the digest for each signed item to make sure its digest is present in the issuer authentication.

Next, you use the issuer certificate to verify the issuer signature, and make sure the certificate matches an issuer root certificate your server trusts. The root certificates generally correspond to the issuing authorities of the state IDs you accept. For each state ID you accept, you need to download the root certificate from the corresponding state DMV website.

##### Verify the Device Signature

The device authentication structure contains the signature of the device that’s requesting the information. Refer to ISO 18013-5 section 9.1.3 for more information.

Two mechanisms exist for `mdoc` authentication, ECDSA and MAC. The `PassKit` framework only uses ECDSA authentication. The session transcript you use to construct the device authentication structure is the same session transcript you use for decryption. Get the device signing key — represented as a `COSE_Key` — from the MSO.

##### Test the Implementation

After you verify the issuer signature and device signature, you can use the signed items as necessary. To download a sample that contains the files necessary to test your implementation, see [`Apple Wallet Developer Resources`](https://developer.apple.comhttps://developer.apple.com/wallet/resources/).

## See Also

- [Requesting identity data from a Wallet pass](requesting-identity-data-from-a-wallet-pass.md)
  Initiate a request for identity information by prompting a user for permission and decrypting a response payload.
- [class PKIdentityAuthorizationController](pkidentityauthorizationcontroller.md)
  An object that presents a sheet that prompts the user to allow a request for identity information.
- [class PKIdentityRequest](pkidentityrequest.md)
  An object that represents a request for identity information from a Wallet pass.
- [class PKIdentityDocument](pkidentitydocument.md)
  An object that represents the response to a request.
- [class PKIdentityElement](pkidentityelement.md)
  An object that represents the elements an app requests from identity documents.
- [class PKIdentityButton](pkidentitybutton.md)
  An object that displays a button to trigger the identity verification flow.
- [struct VerifyIdentityWithWalletButton](verifyidentitywithwalletbutton.md)
  A view that displays a button for identity verification.
- [struct VerifyIdentityWithWalletButtonLabel](verifyidentitywithwalletbuttonlabel.md)
  A type that represents the label you use with a verify identity button.
- [struct VerifyIdentityWithWalletButtonStyle](verifyidentitywithwalletbuttonstyle.md)
  A type that represents the style you use with a verify identity button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/verifying-wallet-identity-requests)*
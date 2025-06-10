# Requesting a mobile document on the web

**Framework**: IdentityDocumentServices

Send a request for mobile document information for apps installed on a device.

#### Overview

The Digital Credentials API allows websites to request identity document information from apps installed on a device. You can request mobile documents (mdocs), as defined in the ISO/IEC 18013-5 standard, through the Digital Credentials API.

Using the Digital Credentials API is the most streamlined and secure way for websites to request mdocs. By implementing the API, your website has access to the mdocs stored in the Wallet app, and in other apps on device. By default, the API supports these flows across iPhone, iPad, and Mac without any platform-specific work required by the website. Additionally, the API leverages other standards to enable cross-platform flows to other operating systems.

#### Build the Request

Your server needs to build the request and handle encryption. The request format is defined in the mdoc request profile in ISO/IEC 18013-7 Annex C.

A request includes two parts: the encryption information and the device request. The encryption information contains parameters important for response encryption. Part of creating the encryption information is generating a recipient encryption key pair. Your server uses this key pair to decrypt the document response returned from the API, so you need to keep the encryption key safely on your server and rotate it frequently.

The parameters in the encryption information are:

The device request is the second part of a request. Section 8.3.2.1.2.1 of the ISO/IEC 18013-5 standard defines the format for this request. Use the latest version string available from the standard when building your device request for the Digital Credentials API.

Define the details of the document you’re requesting in the `ItemsRequest` type. The notable parameters are:

#### Sign and Authenticate the Request

After you build the request that describes the document you’re requesting, you might need to authenticate the request through a signature. Any apps that contain these documents are eligible to respond to this request. Some apps might have additional authentication that requires identification of the requesting website.

The standardized mechanism for authenticating the request is the `ReaderAuth` mechanism described in Section 9.1.4 of ISO/IEC 18013-5. This section contains instructions on how to generate a signature and attach it to your device request. The `SessionTranscript` your app uses to generate this signature needs to be the `SessionTranscript` defined in Annex C of ISO/IEC 18013-7.

##### Enable Apple Wallet to Accept an Mdoc Request

Apple Wallet’s authentication requirements include authenticating the request via the `ReaderAuth` mechanism with a certificate.

You get this request authentication certificate from Apple Business Connect. For more information, see the [`Apple Business Connect User Guide`](https://developer.apple.comhttps://support.apple.com/guide/apple-business-connect/welcome/web).

After you have this certificate, generate the `ReaderAuth` signature with its signing key. Then, attach the certificate to the `ReaderAuth` structure through the `x5chain` header defined in RFC 9360.

#### Call the Digital Credentials Api

First, you build the request based on the generated information from your server. Then, you can build the request structure for the Digital Credentials API.

After you create a request, then you pass it to `navigator.credentials.get` to trigger the Digital Credentials API. This code must be triggered by an explicit user interaction such as a click handler. If you call this API without a user interaction, the system throws an exception.

The following code shows how to call the API:

```javascript
// JavaScript website code.

// A user interaction, such as a click handler, triggers this code.
try {
    // A hardcoded sample request is provided below.
    // This request would normally be built on your server.
    const mdocRequest = {
        "deviceRequest": "pGd2ZXJzaW9uYzEuMWtkb2NSZXF1ZXN0c4GhbGl0ZW1zUmVxdWVzdNgYWG6iZ2RvY1R5cGV1b3JnLmlzby4xODAxMy41LjEubURMam5hbWVTcGFjZXOhcW9yZy5pc28uMTgwMTMuNS4xpGhwb3J0cmFpdPVqZ2l2ZW5fbmFtZfVrYWdlX292ZXJfMjH0a2ZhbWlseV9uYW1l9W1yZWFkZXJBdXRoQWxsgYRDoQEmoRghWQF9MIIBeTCCASACCQCdvhptTdV7cDAKBggqhkjOPQQDAjBFMRowGAYDVQQKDBFUZXN0IE9yZ2FuaXphdGlvbjEnMCUGA1UEAwweVGVzdCBSZXF1ZXN0IEF1dGhlbnRpY2F0aW9uIENBMB4XDTI1MDUyNzIwNDgwMFoXDTM1MDUyNTIwNDgwMFowRTEaMBgGA1UECgwRVGVzdCBPcmdhbml6YXRpb24xJzAlBgNVBAMMHlRlc3QgUmVxdWVzdCBBdXRoZW50aWNhdGlvbiBDQTBZMBMGByqGSM49AgEGCCqGSM49AwEHA0IABIt9TGoAW2u25Yi_Czptq21xNUqolJdfvpBDRVBYdMXSsdwxsbl2JH3gF3YiP6VldwYI0UxF0-CtkgUCoJ-LjaMwCgYIKoZIzj0EAwIDRwAwRAIgR8Pa4-6_xvHi5m7SLckA0QmdjVhUEzeam_SHkpmM4AECIH5H7lgKOw0C0mFIvgGG8cyS7IUuk6wGIsmc7JjtX9em9lhApChXUdkLtAgRXpmq_RGHLXpfazSUYQ3mi5nXDYw73R9yqw_gyOSDvxpjwEeSKkHEdYt777Wu8OskvwjqAiPahXFkZXZpY2VSZXF1ZXN0SW5mb9gYWCehaHVzZUNhc2VzgaJpbWFuZGF0b3J59Wxkb2N1bWVudFNldHOBgQA",
        "encryptionInfo": "gmVkY2FwaaJlbm9uY2VYIPlv505ZK3Y93ZZhO-Wi4HqqHWHismrehHtGtNx3fxOxcnJlY2lwaWVudFB1YmxpY0tleaQBAiABIVggrlztqHsaR_OK3Npf8eTvG6AZWNxJsb69ZTFIPJcUR-0iWCCbWR3FyNPy2ysLKoiTysxI7LjxvcRnfNsB-JLDNmZdDw"
    }
    
    const request = {
        mediation: "required",
        digital: {
            requests: [{
                protocol: "org-iso-mdoc",
                data: mdocRequest
            }]
        }
    };


    const response = await navigator.credentials.get(request);
    // Send the response to your server for handling.
} catch (error) {
    // Use an alternative identity verification method.
}
```

First, build the request based on the generated information from your server. Once built, you can build the request structure for the Digital Credentials API.

Pass your mdoc request as an individual request in the requests array. The protocol string `org-iso-mdoc` identifies the request profile.

#### Receive an Mdoc Response

The format of the mdoc response returned from the Digital Credentials API is defined in Annex C of ISO/IEC 18013-7. There are two important parameters in the mdoc response:

The server decrypts the response through Hybrid Public Key Encryption (HPKE) defined in RFC 9180. The particular parameters to use for decryption operation are defined in Annex C of ISO/IEC 18013-7.

The decryption results in a `DeviceResponse`, defined in Section 8.3.2.1.2.3 of ISO/IEC 18013-5. This device response contains the returned documents and element information.

There are some additional security structures attached in the response. You need to verify these properties before using the returned element information. The two structures that need to be verified are: the issuer authentication structure and the device authentication structure.

Section 9.1.2 of ISO/IEC 18013-5 defines a procedure for validating the issuer data in the device response. This helps your business verify that the data is authentic and comes from a source that you trust. Part of this process involves maintaining a list of trusted Issuing Authority Certificate Authority (IACA) root certificates. This list allows you to control which entities you trust to issue document data. If a document response isn’t signed by a certificate that chains up to an IACA in your trust store, then discard the response.

Section 9.1.3 of ISO/IEC 18013-5 defines a procedure for validating the mdoc itself. This procedure helps your business verify that the response came from the device to which it was issued by your app. Using this procedure helps prevent cloning of the mdoc to an unauthorized device. This is done through the `DeviceAuth` structure and an associated device key.

After you perform the validations above, then you’re ready to use the returned data.

## See Also

- [Implementing as an identity document provider](implenting-as-an-identity-document-provider.md)
  Add your app as an option for mobile document web presentment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/requesting-a-mobile-document-on-the-web)*
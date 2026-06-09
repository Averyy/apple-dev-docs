# Validating apps that connect to your server

**Framework**: DeviceCheck

Verify that connections to your server come from legitimate instances of your app.

#### Overview

Adopt App Attest to check whether clients connecting to your server are valid instances of your app. Your app uses the [`shared`](dcappattestservice/shared.md) instance of the [`DCAppAttestService`](dcappattestservice.md) to create a cryptographic key on a device, and then attest to the key’s validity. This produces an attestation object that your app passes to your server, along with the corresponding key identifier. Your server verifies the attestation object, and then extracts the embedded public key and other information. Later, your server uses the key to verify assertion objects that your app sends at critical points in the app’s life cycle, like when users try to download premium content.

![A diagram showing how your server sends challenges to your app, which responds with an attestation or an assertion, while relying on the App Attest logic. ](https://docs-assets.developer.apple.com/published/af2153e7215540c665379d51d65f532a/validating_apps_that_connect_to_your_server-1%402x.png)

This article describes how to integrate App Attest into your server logic. For more information about the activites you perform in your app to support App Attest, see [`Establishing your app’s integrity`](establishing-your-app-s-integrity.md).

##### Provide a Challenge

Every time your app needs to communicate attestation data to your server, the app first asks the server for a unique, one-time challenge. App Attest integrates this challenge into the objects that it provides, and that your app sends back to your server for validation. This makes it harder for an attacker to implement a replay attack.

When the app asks for a challenge, provide a randomized data value, and remember the value for use when verifying the corresponding attestation or assertion objects the client sends. How you use the challenge data depends on the kind of object that you need to validate.

##### Verify the Attestation

The App Attest service creates an attestation object that consists of authenticator data and an attestation statement according to the [`Web Authentication`](https://developer.apple.comhttps://www.w3.org/TR/webauthn/#sec-authenticator-data) specification. The following authenticator fields are of particular interest for App Attest:

- `RP ID` (32 bytes) — A hash of your app’s App ID, which is the concatenation of your app’s App ID prefix, a period, and your app’s [`CFBundleIdentifier`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/CFBundleIdentifier) value. The App ID prefix is usually automatically set to be your 10-digit team identifier, and can be found by inspecting the Identifier entry for your app in the [`Certificates, Identifiers & Profiles`](https://developer.apple.comhttps://developer.apple.com/account/resources/identifiers/list) section of your Apple Developer Account.

> **Note**: On macOS, the `RP ID` utilizes the [`signing identifier`](https://developer.apple.comhttps://developer.apple.com/documentation/technotes/tn3127-inside-code-signing-requirements) in place of the bundle identifier.

- `counter` (4 bytes) — A value that reports the number of times your app has used the attested key to sign an assertion.
- `aaguid` (16 bytes) — An App Attest–specific constant that indicates whether the attested key belongs to the development or production environment. Apps generate keys using the former during development, and the latter after distribution, as [`App Attest Environment`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.devicecheck.appattest-environment) describes.
- `credentialId length` (2 bytes) — The length of the hash of the public key part of the attested cryptographic key pair, following this field.
- `credentialId` (32 bytes) — A hash of the public key part of the attested cryptographic key pair.
- `Encoded key` (77 bytes) — The [`CBOR object signing and encryption (COSE)`](https://developer.apple.comhttps://datatracker.ietf.org/doc/html/rfc8152) formatted public key part of the attested cryptographic key pair.
- `extensions` (variable bytes) — [`CBOR dictionary object`](https://developer.apple.comhttps://www.w3.org/TR/webauthn/#sctn-extensions) that includes optional client properties.

> **Note**: An attestation `RP ID` that an App Clip generates uses the full app’s identifier, not the App Clip’s identifier. For information about the difference between the two, see [`Creating an App Clip with Xcode`](https://developer.apple.com/documentation/AppClip/creating-an-app-clip-with-xcode).

The attestation statement uses a custom Apple attestation statement format with the following syntax:

```other
$$attStmtType //= (
                      fmt: "apple-appattest",
                      attStmt: StmtFormat
                  )

StmtFormat =      {
                      x5c: [ credCert: bytes, * (caCert: bytes) ],
                      receipt: bytes,
                  }
```

To verify and decode the attestation object, check that it has the [`Concise Binary Object Representation (CBOR)`](https://developer.apple.comhttps://tools.ietf.org/html/rfc7049) data format with the expected syntax. The decoded object looks like this:

```javascript
{
  fmt: 'apple-appattest',
  attStmt: {
    x5c: [
      <Buffer 30 82 02 cc ... >,
      <Buffer 30 82 02 36 ... >
    ],
    receipt: <Buffer 30 80 06 09 ... >
  },
  authData: <Buffer 21 c9 9e 00 ... >
}
```

Use the decoded object, along with the key identifier that your app sends, to perform the following steps:

1. Verify that the `x5c` array contains the intermediate and leaf certificates for App Attest, starting from the credential certificate in the first data buffer in the array (`credcert`). Verify the validity of the certificates using Apple’s [`App Attest root certificate`](https://developer.apple.comhttps://www.apple.com/certificateauthority/private).
2. Create `clientDataHash` as the SHA256 hash of the one-time challenge your server sends to your app before performing the attestation, and append that hash to the end of the authenticator data (`authData` from the decoded object).
3. Generate a new SHA256 hash of the composite item to create `nonce`.
4. Obtain the value of the `credCert` extension with OID `1.2.840.113635.100.8.2`, which is a DER-encoded ASN.1 sequence. Decode the sequence and extract the single octet string that it contains. Verify that the string equals `nonce`.

> ❗ **Important**:  On macOS, obtain the value of the `aclBlob` for the key associated with the attestation with OID `1.2.840.113635.100.8.6`, which is a DER-encoded ASN.1 sequence. Decode the sequence and extract the single octet string that it contains. Verify that the string equals `MEAMAjExMDowCQwCb2uhAwEB/zAJDAJvYaEDAQH/MAsMBG9kZWyhAwEB/zAVDARvc2duoAYMBHJzZWMwBaYDAgEB`. This String value represents the encoded hash of the access policy for the attested key on macOS corresponding with both SIP and full security mode enabled. Attested keys on macOS should only be trusted for this exact hash value. This value should never change across macOS versions.

1. Create the SHA256 hash of the public key in `credCert` with X9.62 uncompressed point format, and verify that it matches the key identifier from your app.
2. Compute the SHA256 hash of your app’s App ID, and verify that it’s the same as the authenticator data’s `RP ID` hash.
3. Verify that the authenticator data’s `counter` field equals `0`.
4. Verify that the authenticator data’s `aaguid` field is either `appattestdevelop` if operating in the development environment, or `appattest` followed by seven `0x00` bytes if operating in the production environment.
5. Verify that the authenticator data’s `credentialId` field is the same as the key identifier.
6. Verify the `apple_validation_category_01` value within the `extensions` CBOR dictionary in the authenticator data.

> **Note**: This `UInt32` value represents the launch [`ValidationCategory`](https://developer.apple.com/documentation/LightweightCodeRequirements/ValidationCategory) of your app.

| Validation Category | Description |
| --- | --- |
| `0` | Invalid. |
| `1` | An operating system executable. |
| `2` | An executable distributed through TestFlight. |
| `3` | An executable signed by a development code signing identity. |
| `4` | An executable distributed through the App Store. |
| `5` | An executable distributed using an Enterprise Universal Provisioning Profile, or ad-hoc distribution. |
| `6` | An executable signed using Developer ID. |
| `7, 8, or 9` | These values aren’t appropriate as they represent categories of binaries that the system generates in certain restricted situations. |
| `10` | An executable signed with a code signing identity that doesn’t match any other category. |

1. Verify the `apple_bundle_version_01` value within the `extensions` CBOR dictionary in the authenticator data.

> **Note**: This `String` value representing the version of the distributed App.

After successfully completing these steps, you can trust the attestation object.

> **Note**: Follow the [`Attestation Object Validation Guide`](attestation-object-validation-guide.md) to ensure your implementation for the steps above is correct.

##### Store the Public Key and Receipt

Store the verified public key from `credCert` on your server and associate it with the user for the specific device. You use this key to check assertions later. As an added protection against replay attacks, make sure that the public key doesn’t already have an association with another user.

The attestation statement also contains a receipt that you can use later in a server-to-server call to request a fraud assessment metric from Apple. You use the metric to examine the number of attested keys for a specific device. This helps you to assess the risk that an attacker is using a compromised device to serve assertions to many compromised versions of your app.

When attestation succeeds, independently verify and store the receipt immediately. For more information about how to interpret the receipt, and how to use a receipt to obtain or refresh the metric, see [`Assessing fraud risk`](assessing-fraud-risk.md).

> ❗ **Important**: Be prepared to store multiple (key, receipt) pairs for each user. Store one pair for each device the user uses to access your services. Also, keep development pairs separate from production pairs because you can’t use one set in the other’s environment.

##### Verify the Assertion

After successful attestation, your server can require the associated client to accompany server requests with an assertion object. Each verified assertion reestablishes the legitimacy of the client. You typically require this for requests that access sensitive or premium content.

The client creates the assertion by packaging the request as `clientData`, and asking the App Attest service to sign the data with the attested private key. Along with the signature, App Attest includes a simplified authenticator data instance in the assertion object, similar to the one in the attestation object, but containing only the first few fields, including `RP ID` and `counter`.

After receiving the client data and the assertion, you need to verify and decode the assertion to ensure it uses the CBOR data format and has the expected contents. The decoded object looks like this:

```swift
{
  signature: <Buffer 30 45 02 20 ... >,
  authenticatorData: <Buffer 21 c9 9e 00 ... >
}
```

To verify the assertion, use the decoded assertion, the client data, and the previously stored public key, and follow these steps:

1. Compute `clientDataHash` as the SHA256 hash of `clientData`.
2. Concatenate `authenticatorData` and `clientDataHash`, and apply a SHA256 hash over the result to form `nonce`.
3. Use the public key that you store from the attestation object to verify that the assertion’s `signature` is valid for `nonce`.
4. Compute the SHA256 hash of the client’s App ID, and verify that it matches the `RP ID` in the authenticator data.
5. Verify that the authenticator data’s `counter` value is greater than the value from the previous assertion, or greater than `0` on the first assertion.
6. Verify that the embedded challenge in the client data matches the earlier challenge to the client.
7. Verify the `validationCategory` within the `extensions` CBOR dictionary in the authenticator data.
8. Verify the `bundleVersion` within the `extensions` CBOR dictionary in the authenticator data.

When the assertion meets all of these conditions, you can trust it. Store `counter` to use in step 5 when verifying the next assertion.

## See Also

- [Establishing your app’s integrity](establishing-your-app-s-integrity.md)
  Ensure that requests your server receives come from legitimate instances of your app.
- [Assessing fraud risk](assessing-fraud-risk.md)
  Request and analyze risk data using server-to-server calls.
- [Preparing to use the app attest service](preparing-to-use-the-app-attest-service.md)
  Test your implementation in a development environment and onboard users gradually.
- [Attestation Object Validation Guide](attestation-object-validation-guide.md)
  Use this guide to validate your implementation of verifying the attestation object verification process.
- [class DCAppAttestService](dcappattestservice.md)
  A service that you use to validate the instance of your app running on a device.
- [App Attest Environment](../BundleResources/Entitlements/com.apple.developer.devicecheck.appattest-environment.md)
  The environment for an app that uses the App Attest service to validate itself.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicecheck/validating-apps-that-connect-to-your-server)*
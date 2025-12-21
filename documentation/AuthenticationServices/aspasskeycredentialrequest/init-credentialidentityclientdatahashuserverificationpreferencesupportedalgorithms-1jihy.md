# init(credentialIdentity:clientDataHash:userVerificationPreference:supportedAlgorithms:)

**Framework**: Authentication Services  
**Kind**: init

Initializes a passkey credential request, identifying supported algorithms by number.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(credentialIdentity: ASPasskeyCredentialIdentity, clientDataHash: Data, userVerificationPreference: ASAuthorizationPublicKeyCredentialUserVerificationPreference, supportedAlgorithms: [NSNumber])
```

#### Discussion

The `supportedAlgorithms` parameter is empty for credential assertion requests. For credential registration requests, it contains one or more numbers from the Internet Assigned Numbers Authority (IANA) [`Concise Binary Object Representation Object Signing and Encryption (COSE) algorithms registry`](https://developer.apple.comhttps://www.iana.org/assignments/cose/cose.xhtml#algorithms).

## Parameters

- `credentialIdentity`: The identity of the requested passkey credential.
- `clientDataHash`: Hash of the client data from the passkey authentication challenge.
- `userVerificationPreference`: The relying party’s user verification preference.
- `supportedAlgorithms`: An array of numbers that represent cryptographic signature algorithms the identifying party supports.

## See Also

- [convenience init(credentialIdentity: ASPasskeyCredentialIdentity, clientDataHash: Data, userVerificationPreference: ASAuthorizationPublicKeyCredentialUserVerificationPreference, supportedAlgorithms: [ASCOSEAlgorithmIdentifier])](aspasskeycredentialrequest/init(credentialidentity:clientdatahash:userverificationpreference:supportedalgorithms:)-52txr.md)
  Initializes a passkey credential request, identifying supported algorithms with constants.
- [convenience init(credentialIdentity: ASPasskeyCredentialIdentity, clientDataHash: Data, userVerificationPreference: ASAuthorizationPublicKeyCredentialUserVerificationPreference, supportedAlgorithms: [ASCOSEAlgorithmIdentifier], extensionInput: ASPasskeyAssertionCredentialExtensionInput?)](aspasskeycredentialrequest/init(credentialidentity:clientdatahash:userverificationpreference:supportedalgorithms:extensioninput:)-9hsyv.md)
  Initializes a passkey credential request, providing additional passkey assertion data.
- [convenience init(credentialIdentity: ASPasskeyCredentialIdentity, clientDataHash: Data, userVerificationPreference: ASAuthorizationPublicKeyCredentialUserVerificationPreference, supportedAlgorithms: [ASCOSEAlgorithmIdentifier], extensionInput: ASPasskeyRegistrationCredentialExtensionInput?)](aspasskeycredentialrequest/init(credentialidentity:clientdatahash:userverificationpreference:supportedalgorithms:extensioninput:)-1258o.md)
  Initializes a passkey credential request, providing additional passkey registration data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasskeycredentialrequest/init(credentialidentity:clientdatahash:userverificationpreference:supportedalgorithms:)-1jihy)*
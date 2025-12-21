# init(credentialIdentity:clientDataHash:userVerificationPreference:supportedAlgorithms:extensionInput:)

**Framework**: Authentication Services  
**Kind**: init

Initializes a passkey credential request, providing additional passkey registration data.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
convenience init(credentialIdentity: ASPasskeyCredentialIdentity, clientDataHash: Data, userVerificationPreference: ASAuthorizationPublicKeyCredentialUserVerificationPreference, supportedAlgorithms: [ASCOSEAlgorithmIdentifier], extensionInput: ASPasskeyRegistrationCredentialExtensionInput?)
```

#### Discussion

For credential assertion requests, supply an empty array for `supportedAlgorithms`. For credential registration requests, supply an array of one or more [`ASCOSEAlgorithmIdentifier`](ascosealgorithmidentifier.md) values.

## Parameters

- `credentialIdentity`: The identity of the requested passkey credential.
- `clientDataHash`: The hash of the client data from the passkey authentication challenge.
- `userVerificationPreference`: The relying party’s user verification preference.
- `supportedAlgorithms`: A list of cryptographic signature algorithms that the relying party supports.
- `extensionInput`: Input for any requested passkey extensions.

## See Also

- [convenience init(credentialIdentity: ASPasskeyCredentialIdentity, clientDataHash: Data, userVerificationPreference: ASAuthorizationPublicKeyCredentialUserVerificationPreference, supportedAlgorithms: [NSNumber])](aspasskeycredentialrequest/init(credentialidentity:clientdatahash:userverificationpreference:supportedalgorithms:)-1jihy.md)
  Initializes a passkey credential request, identifying supported algorithms by number.
- [convenience init(credentialIdentity: ASPasskeyCredentialIdentity, clientDataHash: Data, userVerificationPreference: ASAuthorizationPublicKeyCredentialUserVerificationPreference, supportedAlgorithms: [ASCOSEAlgorithmIdentifier])](aspasskeycredentialrequest/init(credentialidentity:clientdatahash:userverificationpreference:supportedalgorithms:)-52txr.md)
  Initializes a passkey credential request, identifying supported algorithms with constants.
- [convenience init(credentialIdentity: ASPasskeyCredentialIdentity, clientDataHash: Data, userVerificationPreference: ASAuthorizationPublicKeyCredentialUserVerificationPreference, supportedAlgorithms: [ASCOSEAlgorithmIdentifier], extensionInput: ASPasskeyAssertionCredentialExtensionInput?)](aspasskeycredentialrequest/init(credentialidentity:clientdatahash:userverificationpreference:supportedalgorithms:extensioninput:)-9hsyv.md)
  Initializes a passkey credential request, providing additional passkey assertion data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasskeycredentialrequest/init(credentialidentity:clientdatahash:userverificationpreference:supportedalgorithms:extensioninput:)-1258o)*
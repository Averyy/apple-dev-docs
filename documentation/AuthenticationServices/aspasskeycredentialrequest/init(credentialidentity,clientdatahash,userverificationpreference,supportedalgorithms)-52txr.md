# init(credentialIdentity:clientDataHash:userVerificationPreference:supportedAlgorithms:)

**Framework**: Authentication Services  
**Kind**: init  
**Role**: Initializer

Initializes a passkey credential request, identifying supported algorithms with constants.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(credentialIdentity: ASPasskeyCredentialIdentity, clientDataHash: Data, userVerificationPreference: ASAuthorizationPublicKeyCredentialUserVerificationPreference, supportedAlgorithms: [ASCOSEAlgorithmIdentifier])
```

## Discussion

For credential assertion requests, supply an empty array for the `supportedAlgorithms`. For credential registration requests, supply an array of one or more [`ASCOSEAlgorithmIdentifier`](../ascosealgorithmidentifier.md) values.

## Parameters

- `credentialIdentity`: The identity of the requested passkey credential.
- `clientDataHash`: Hash of the client data from the passkey authentication challenge.
- `userVerificationPreference`: The relying party’s user verification preference.
- `supportedAlgorithms`: A list of cryptographic signature algorithms that the relying party supports.

## See Also

### Creating passkey credential requests
- [convenience init(credentialIdentity: ASPasskeyCredentialIdentity, clientDataHash: Data, userVerificationPreference: ASAuthorizationPublicKeyCredentialUserVerificationPreference, supportedAlgorithms: [NSNumber])](./init%28credentialidentity,clientdatahash,userverificationpreference,supportedalgorithms%29-1jihy.md)
  Initializes a passkey credential request, identifying supported algorithms by number.
- [convenience init(credentialIdentity: ASPasskeyCredentialIdentity, clientDataHash: Data, userVerificationPreference: ASAuthorizationPublicKeyCredentialUserVerificationPreference, supportedAlgorithms: [ASCOSEAlgorithmIdentifier], extensionInput: ASPasskeyAssertionCredentialExtensionInput?)](./init%28credentialidentity,clientdatahash,userverificationpreference,supportedalgorithms,extensioninput%29-9hsyv.md)
  Initializes a passkey credential request, providing additional passkey assertion data.
- [convenience init(credentialIdentity: ASPasskeyCredentialIdentity, clientDataHash: Data, userVerificationPreference: ASAuthorizationPublicKeyCredentialUserVerificationPreference, supportedAlgorithms: [ASCOSEAlgorithmIdentifier], extensionInput: ASPasskeyRegistrationCredentialExtensionInput?)](./init%28credentialidentity,clientdatahash,userverificationpreference,supportedalgorithms,extensioninput%29-1258o.md)
  Initializes a passkey credential request, providing additional passkey registration data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasskeycredentialrequest/init(credentialidentity:clientdatahash:userverificationpreference:supportedalgorithms:)-52txr)*
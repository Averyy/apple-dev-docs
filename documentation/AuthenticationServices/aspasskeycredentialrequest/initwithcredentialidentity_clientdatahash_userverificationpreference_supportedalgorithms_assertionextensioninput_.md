# initWithCredentialIdentity:clientDataHash:userVerificationPreference:supportedAlgorithms:assertionExtensionInput:

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

Initializes a passkey credential request, providing additional passkey registration data.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```objc
- (instancetype) initWithCredentialIdentity:(ASPasskeyCredentialIdentity *) credentialIdentity clientDataHash:(NSData *) clientDataHash userVerificationPreference:(ASAuthorizationPublicKeyCredentialUserVerificationPreference) userVerificationPreference supportedAlgorithms:(NSArray<NSNumber *> *) supportedAlgorithms assertionExtensionInput:(ASPasskeyAssertionCredentialExtensionInput *) assertionExtensionInput;
```

## Parameters

- `credentialIdentity`: The identity of the requested passkey credential.
- `clientDataHash`: The hash of the client data from the passkey authentication challenge.
- `userVerificationPreference`: The relying party’s user verification preference.
- `supportedAlgorithms`: A list of cryptographic signature algorithms that the relying party supports.
- `assertionExtensionInput`: Input for any requested passkey extensions.

## See Also

### Creating passkey credential requests
- [convenience init(credentialIdentity: ASPasskeyCredentialIdentity, clientDataHash: Data, userVerificationPreference: ASAuthorizationPublicKeyCredentialUserVerificationPreference, supportedAlgorithms: [NSNumber])](./init%28credentialidentity,clientdatahash,userverificationpreference,supportedalgorithms%29-1jihy.md)
  Initializes a passkey credential request, identifying supported algorithms by number.
- [- initWithCredentialIdentity:clientDataHash:userVerificationPreference:supportedAlgorithms:](./initwithcredentialidentity_clientdatahash_userverificationpreference_supportedalgorithms_.md)
  Initializes a passkey credential request.
- [- initWithCredentialIdentity:clientDataHash:userVerificationPreference:supportedAlgorithms:registrationExtensionInput:](./initwithcredentialidentity_clientdatahash_userverificationpreference_supportedalgorithms_registrationextensioninput_.md)
  Initializes a passkey credential request, providing additional passkey registration data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasskeycredentialrequest/initwithcredentialidentity:clientdatahash:userverificationpreference:supportedalgorithms:assertionextensioninput:)*
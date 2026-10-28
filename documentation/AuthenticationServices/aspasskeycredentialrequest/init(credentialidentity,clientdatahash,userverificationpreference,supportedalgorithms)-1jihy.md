# init(credentialIdentity:clientDataHash:userVerificationPreference:supportedAlgorithms:)

**Framework**: Authentication Services  
**Kind**: init  
**Role**: Initializer

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

```objc
+ (instancetype) requestWithCredentialIdentity:(ASPasskeyCredentialIdentity *) credentialIdentity clientDataHash:(NSData *) clientDataHash userVerificationPreference:(ASAuthorizationPublicKeyCredentialUserVerificationPreference) userVerificationPreference supportedAlgorithms:(NSArray<NSNumber *> *) supportedAlgorithms;
```

## Discussion

The `supportedAlgorithms` parameter is empty for credential assertion requests. For credential registration requests, it contains one or more numbers from the Internet Assigned Numbers Authority (IANA) [Concise Binary Object Representation Object Signing and Encryption (COSE) algorithms registry](https://www.iana.org/assignments/cose/cose.xhtml#algorithms).

## Parameters

- `credentialIdentity`: The identity of the requested passkey credential.
- `clientDataHash`: Hash of the client data from the passkey authentication challenge.
- `userVerificationPreference`: The relying party’s user verification preference.
- `supportedAlgorithms`: An array of numbers that represent cryptographic signature algorithms the identifying party supports.

## See Also

### Creating passkey credential requests
- [convenience init(credentialIdentity: ASPasskeyCredentialIdentity, clientDataHash: Data, userVerificationPreference: ASAuthorizationPublicKeyCredentialUserVerificationPreference, supportedAlgorithms: [ASCOSEAlgorithmIdentifier])](./init%28credentialidentity,clientdatahash,userverificationpreference,supportedalgorithms%29-52txr.md)
  Initializes a passkey credential request, identifying supported algorithms with constants.
- [convenience init(credentialIdentity: ASPasskeyCredentialIdentity, clientDataHash: Data, userVerificationPreference: ASAuthorizationPublicKeyCredentialUserVerificationPreference, supportedAlgorithms: [ASCOSEAlgorithmIdentifier], extensionInput: ASPasskeyAssertionCredentialExtensionInput?)](./init%28credentialidentity,clientdatahash,userverificationpreference,supportedalgorithms,extensioninput%29-9hsyv.md)
  Initializes a passkey credential request, providing additional passkey assertion data.
- [convenience init(credentialIdentity: ASPasskeyCredentialIdentity, clientDataHash: Data, userVerificationPreference: ASAuthorizationPublicKeyCredentialUserVerificationPreference, supportedAlgorithms: [ASCOSEAlgorithmIdentifier], extensionInput: ASPasskeyRegistrationCredentialExtensionInput?)](./init%28credentialidentity,clientdatahash,userverificationpreference,supportedalgorithms,extensioninput%29-1258o.md)
  Initializes a passkey credential request, providing additional passkey registration data.
- [- initWithCredentialIdentity:clientDataHash:userVerificationPreference:supportedAlgorithms:](./initwithcredentialidentity_clientdatahash_userverificationpreference_supportedalgorithms_.md)
  Initializes a passkey credential request.
- [- initWithCredentialIdentity:clientDataHash:userVerificationPreference:supportedAlgorithms:assertionExtensionInput:](./initwithcredentialidentity_clientdatahash_userverificationpreference_supportedalgorithms_assertionextensioninput_.md)
  Initializes a passkey credential request, providing additional passkey registration data.
- [- initWithCredentialIdentity:clientDataHash:userVerificationPreference:supportedAlgorithms:registrationExtensionInput:](./initwithcredentialidentity_clientdatahash_userverificationpreference_supportedalgorithms_registrationextensioninput_.md)
  Initializes a passkey credential request, providing additional passkey registration data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasskeycredentialrequest/init(credentialidentity:clientdatahash:userverificationpreference:supportedalgorithms:)-1jihy)*
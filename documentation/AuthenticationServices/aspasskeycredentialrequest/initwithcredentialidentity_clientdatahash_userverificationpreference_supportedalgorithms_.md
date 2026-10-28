# initWithCredentialIdentity:clientDataHash:userVerificationPreference:supportedAlgorithms:

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

Initializes a passkey credential request.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```objc
- (instancetype) initWithCredentialIdentity:(ASPasskeyCredentialIdentity *) credentialIdentity clientDataHash:(NSData *) clientDataHash userVerificationPreference:(ASAuthorizationPublicKeyCredentialUserVerificationPreference) userVerificationPreference supportedAlgorithms:(NSArray<NSNumber *> *) supportedAlgorithms;
```

## Return Value

An initialized passkey credential request.

## Discussion

For credential assertion requests, supply an empty array for the `supportedAlgorithms`. For credential registration requests, supply an array of one or more numbers from the Internet Assigned Numbers Authority (IANA) [Concise Binary Object Representation Object Signing and Encryption (COSE) algorithms registry](https://www.iana.org/assignments/cose/cose.xhtml#algorithms) as [`NSNumber`](../../Foundation/nsnumber.md) objects.

## Parameters

- `credentialIdentity`: The identity of the requested passkey credential.
- `clientDataHash`: Hash of the client data from the passkey authentication challenge.
- `userVerificationPreference`: The relying party’s user verification preference.
- `supportedAlgorithms`: An array of numbers that represent cryptographic signature algorithms the identifying party supports.

## See Also

### Creating passkey credential requests
- [convenience init(credentialIdentity: ASPasskeyCredentialIdentity, clientDataHash: Data, userVerificationPreference: ASAuthorizationPublicKeyCredentialUserVerificationPreference, supportedAlgorithms: [NSNumber])](./init%28credentialidentity,clientdatahash,userverificationpreference,supportedalgorithms%29-1jihy.md)
  Initializes a passkey credential request, identifying supported algorithms by number.
- [- initWithCredentialIdentity:clientDataHash:userVerificationPreference:supportedAlgorithms:assertionExtensionInput:](./initwithcredentialidentity_clientdatahash_userverificationpreference_supportedalgorithms_assertionextensioninput_.md)
  Initializes a passkey credential request, providing additional passkey registration data.
- [- initWithCredentialIdentity:clientDataHash:userVerificationPreference:supportedAlgorithms:registrationExtensionInput:](./initwithcredentialidentity_clientdatahash_userverificationpreference_supportedalgorithms_registrationextensioninput_.md)
  Initializes a passkey credential request, providing additional passkey registration data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasskeycredentialrequest/initwithcredentialidentity:clientdatahash:userverificationpreference:supportedalgorithms:)*
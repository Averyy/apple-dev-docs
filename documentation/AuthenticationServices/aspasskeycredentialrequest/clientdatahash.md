# clientDataHash

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

The hash of the client data for this assertion.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var clientDataHash: Data { get }
```

```objc
@property (nonatomic, readonly) NSData * clientDataHash;
```

#### Discussion

Use the client data hash for both registration and assertion challenges.

## See Also

### Viewing passkey challenge information
- [var userVerificationPreference: ASAuthorizationPublicKeyCredentialUserVerificationPreference](./userverificationpreference.md)
  The relying party’s user verification preference.
- [var supportedAlgorithms: [ASCOSEAlgorithmIdentifier]](./supportedalgorithms-74mad.md)
  A list of cryptographic signature algorithms that the relying party supports.
- [var extensionInput: ASPasskeyCredentialExtensionInput](./extensioninput.md)
  An input for WebAuthn extensions.
- [enum ASPasskeyCredentialExtensionInput](../aspasskeycredentialextensioninput.md)
  A type for WebAuthn extension inputs.
- [supportedAlgorithms](./supportedalgorithms-27z68.md)
  A list of cryptographic signature algorithms that the relying party supports.
- [assertionExtensionInput](./assertionextensioninput.md)
  An input for WebAuthn extensions.
- [ASPasskeyAssertionCredentialExtensionInput](../aspasskeyassertioncredentialextensioninput-c.class.md)
  A type that encapsulates input for various WebAuthn extensions during passkey assertion.
- [registrationExtensionInput](./registrationextensioninput.md)
  An input for WebAuthn extensions.
- [ASPasskeyRegistrationCredentialExtensionInput](../aspasskeyregistrationcredentialextensioninput-c.class.md)
  A type that encapsulates input for various WebAuthn extensions during passkey registration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasskeycredentialrequest/clientdatahash)*
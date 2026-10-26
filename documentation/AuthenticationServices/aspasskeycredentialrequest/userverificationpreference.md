# userVerificationPreference

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

The relying party’s user verification preference.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var userVerificationPreference: ASAuthorizationPublicKeyCredentialUserVerificationPreference { get set }
```

```objc
@property (nonatomic) ASAuthorizationPublicKeyCredentialUserVerificationPreference userVerificationPreference;
```

## See Also

### Viewing passkey challenge information
- [var clientDataHash: Data](./clientdatahash.md)
  The hash of the client data for this assertion.
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

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasskeycredentialrequest/userverificationpreference)*
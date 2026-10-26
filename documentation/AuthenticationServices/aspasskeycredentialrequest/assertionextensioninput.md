# assertionExtensionInput

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

An input for WebAuthn extensions.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```objc
@property (nonatomic, readonly, nullable) ASPasskeyAssertionCredentialExtensionInput * assertionExtensionInput;
```

## See Also

### Viewing passkey challenge information
- [var clientDataHash: Data](./clientdatahash.md)
  The hash of the client data for this assertion.
- [var userVerificationPreference: ASAuthorizationPublicKeyCredentialUserVerificationPreference](./userverificationpreference.md)
  The relying party’s user verification preference.
- [supportedAlgorithms](./supportedalgorithms-27z68.md)
  A list of cryptographic signature algorithms that the relying party supports.
- [ASPasskeyAssertionCredentialExtensionInput](../aspasskeyassertioncredentialextensioninput-c.class.md)
  A type that encapsulates input for various WebAuthn extensions during passkey assertion.
- [registrationExtensionInput](./registrationextensioninput.md)
  An input for WebAuthn extensions.
- [ASPasskeyRegistrationCredentialExtensionInput](../aspasskeyregistrationcredentialextensioninput-c.class.md)
  A type that encapsulates input for various WebAuthn extensions during passkey registration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasskeycredentialrequest/assertionextensioninput)*
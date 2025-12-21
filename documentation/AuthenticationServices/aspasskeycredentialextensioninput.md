# ASPasskeyCredentialExtensionInput

**Framework**: Authentication Services  
**Kind**: enum

A type for WebAuthn extension inputs.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
enum ASPasskeyCredentialExtensionInput
```

## Topics

### Extension input types
- [ASPasskeyCredentialExtensionInput.none](aspasskeycredentialextensioninput/none.md)
  An empty extension input.
- [case assertion(ASPasskeyAssertionCredentialExtensionInput)](aspasskeycredentialextensioninput/assertion(_:).md)
  An extension input for an assertion.
- [struct ASPasskeyAssertionCredentialExtensionInput](aspasskeyassertioncredentialextensioninput-swift.struct.md)
  A type that encapsulates input for various WebAuthn extensions during passkey assertion.
- [case registration(ASPasskeyRegistrationCredentialExtensionInput)](aspasskeycredentialextensioninput/registration(_:).md)
  An extension input for a registration.
- [struct ASPasskeyRegistrationCredentialExtensionInput](aspasskeyregistrationcredentialextensioninput-swift.struct.md)
  A type that encapsulates input for various WebAuthn extensions during passkey registration.

## See Also

- [var clientDataHash: Data](aspasskeycredentialrequest/clientdatahash.md)
  The hash of the client data for this assertion.
- [var userVerificationPreference: ASAuthorizationPublicKeyCredentialUserVerificationPreference](aspasskeycredentialrequest/userverificationpreference.md)
  The relying party’s user verification preference.
- [var supportedAlgorithms: [ASCOSEAlgorithmIdentifier]](aspasskeycredentialrequest/supportedalgorithms-74mad.md)
  A list of cryptographic signature algorithms that the relying party supports.
- [var extensionInput: ASPasskeyCredentialExtensionInput](aspasskeycredentialrequest/extensioninput.md)
  An input for WebAuthn extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasskeycredentialextensioninput)*
# ASPasskeyRegistrationCredentialExtensionInput

**Framework**: Authentication Services  
**Kind**: struct

A type that encapsulates input for various WebAuthn extensions during passkey registration.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
struct ASPasskeyRegistrationCredentialExtensionInput
```

## Topics

### Inputs
- [var largeBlob: ASAuthorizationPublicKeyCredentialLargeBlobRegistrationInput?](aspasskeyregistrationcredentialextensioninput-swift.struct/largeblob.md)
  Input for the WebAuthn large binary object extension in passkey registration requests.
- [struct ASAuthorizationPublicKeyCredentialLargeBlobRegistrationInput](asauthorizationpublickeycredentiallargeblobregistrationinput-swift.struct.md)
  A type that encapsulates input for large binary object extensions during registration.
- [var prf: ASAuthorizationPublicKeyCredentialPRFRegistrationInput?](aspasskeyregistrationcredentialextensioninput-swift.struct/prf.md)
  Input for the WebAuthn PRF extension in passkey registration requests.
- [struct ASAuthorizationPublicKeyCredentialPRFRegistrationInput](asauthorizationpublickeycredentialprfregistrationinput-swift.struct.md)
  A type that encapsulates input for PRF extensions during registration.

## See Also

- [ASPasskeyCredentialExtensionInput.none](aspasskeycredentialextensioninput/none.md)
  An empty extension input.
- [case assertion(ASPasskeyAssertionCredentialExtensionInput)](aspasskeycredentialextensioninput/assertion(_:).md)
  An extension input for an assertion.
- [struct ASPasskeyAssertionCredentialExtensionInput](aspasskeyassertioncredentialextensioninput-swift.struct.md)
  A type that encapsulates input for various WebAuthn extensions during passkey assertion.
- [case registration(ASPasskeyRegistrationCredentialExtensionInput)](aspasskeycredentialextensioninput/registration(_:).md)
  An extension input for a registration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasskeyregistrationcredentialextensioninput-swift.struct)*
# ASAuthorizationPublicKeyCredentialPRFRegistrationInput

**Framework**: Authentication Services  
**Kind**: struct

A type that encapsulates input for PRF extensions during registration.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
struct ASAuthorizationPublicKeyCredentialPRFRegistrationInput
```

## Topics

### Working with PRF inputs
- [let inputValues: ASAuthorizationPublicKeyCredentialPRFRegistrationInput.InputValues?](asauthorizationpublickeycredentialprfregistrationinput-swift.struct/inputvalues-swift.property.md)
  The input values to use when generating the PRF extension, if specified.
- [ASAuthorizationPublicKeyCredentialPRFRegistrationInput.InputValues](asauthorizationpublickeycredentialprfregistrationinput-swift.struct/inputvalues-swift.typealias.md)
  The type of the registration input values property.
- [static func inputValues(ASAuthorizationPublicKeyCredentialPRFRegistrationInput.InputValues) -> ASAuthorizationPublicKeyCredentialPRFRegistrationInput](asauthorizationpublickeycredentialprfregistrationinput-swift.struct/inputvalues(_:).md)
  The inputs for the PRF extension to evaluate if the new passkey supports the extension.
### Checking for support
- [let shouldCheckForSupport: Bool](asauthorizationpublickeycredentialprfregistrationinput-swift.struct/shouldcheckforsupport.md)
  A Boolean value that indicates whether to check for PRF support.
- [static var checkForSupport: ASAuthorizationPublicKeyCredentialPRFRegistrationInput](asauthorizationpublickeycredentialprfregistrationinput-swift.struct/checkforsupport.md)
  A check to determine extension support for the newly created passkey.

## See Also

- [var largeBlob: ASAuthorizationPublicKeyCredentialLargeBlobRegistrationInput?](aspasskeyregistrationcredentialextensioninput-swift.struct/largeblob.md)
  Input for the WebAuthn large binary object extension in passkey registration requests.
- [struct ASAuthorizationPublicKeyCredentialLargeBlobRegistrationInput](asauthorizationpublickeycredentiallargeblobregistrationinput-swift.struct.md)
  A type that encapsulates input for large binary object extensions during registration.
- [var prf: ASAuthorizationPublicKeyCredentialPRFRegistrationInput?](aspasskeyregistrationcredentialextensioninput-swift.struct/prf.md)
  Input for the WebAuthn PRF extension in passkey registration requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentialprfregistrationinput-swift.struct)*
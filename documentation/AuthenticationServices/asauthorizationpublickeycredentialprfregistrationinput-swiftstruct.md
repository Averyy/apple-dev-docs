# ASAuthorizationPublicKeyCredentialPRFRegistrationInput

**Framework**: Authentication Services  
**Kind**: struct

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

### Instance Properties
- [let inputValues: ASAuthorizationPublicKeyCredentialPRFRegistrationInput.InputValues?](asauthorizationpublickeycredentialprfregistrationinput-swift.struct/inputvalues-swift.property.md)
  If specified, the input values to use when generating the PRF extension. If not specified, the output will only indicate whether the extension is supported.
- [let shouldCheckForSupport: Bool](asauthorizationpublickeycredentialprfregistrationinput-swift.struct/shouldcheckforsupport.md)
### Type Aliases
- [ASAuthorizationPublicKeyCredentialPRFRegistrationInput.InputValues](asauthorizationpublickeycredentialprfregistrationinput-swift.struct/inputvalues-swift.typealias.md)
### Type Properties
- [static var checkForSupport: ASAuthorizationPublicKeyCredentialPRFRegistrationInput](asauthorizationpublickeycredentialprfregistrationinput-swift.struct/checkforsupport.md)
  Check for whether the extension is supported for the newly created passkey.
### Type Methods
- [static func inputValues(ASAuthorizationPublicKeyCredentialPRFRegistrationInput.InputValues) -> ASAuthorizationPublicKeyCredentialPRFRegistrationInput](asauthorizationpublickeycredentialprfregistrationinput-swift.struct/inputvalues(_:).md)
  The inputs for the PRF extension, to evaluate if the new passkey supports this extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentialprfregistrationinput-swift.struct)*
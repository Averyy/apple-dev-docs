# ASAuthorizationPublicKeyCredentialPRFAssertionInput.InputValues

**Framework**: Authentication Services  
**Kind**: struct

These are the values which will be used as inputs to the salts for deriving the SymmetricKey. This type is analogous to AuthenticationExtensionsPRFValues in the WebAuthn spec.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
struct InputValues
```

## Topics

### Initializers
- [init(saltInput1: Data, saltInput2: Data?)](asauthorizationpublickeycredentialprfassertioninput-swift.struct/inputvalues-swift.struct/init(saltinput1:saltinput2:).md)
### Instance Properties
- [var saltInput1: Data](asauthorizationpublickeycredentialprfassertioninput-swift.struct/inputvalues-swift.struct/saltinput1.md)
- [var saltInput2: Data?](asauthorizationpublickeycredentialprfassertioninput-swift.struct/inputvalues-swift.struct/saltinput2.md)
### Type Methods
- [static func saltInput1(Data, saltInput2: Data?) -> ASAuthorizationPublicKeyCredentialPRFAssertionInput.InputValues](asauthorizationpublickeycredentialprfassertioninput-swift.struct/inputvalues-swift.struct/saltinput1(_:saltinput2:).md)
  The inputs for generating the PRF output secrets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentialprfassertioninput-swift.struct/inputvalues-swift.struct)*
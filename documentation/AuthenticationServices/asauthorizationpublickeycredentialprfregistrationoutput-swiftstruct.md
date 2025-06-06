# ASAuthorizationPublicKeyCredentialPRFRegistrationOutput

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
struct ASAuthorizationPublicKeyCredentialPRFRegistrationOutput
```

## Topics

### Initializers
- [init(first: SymmetricKey, second: SymmetricKey?)](asauthorizationpublickeycredentialprfregistrationoutput-swift.struct/init(first:second:).md)
  This method should only be called if input values were provided with the registration request. Otherwise, use `.supported` or `.unsupported`.
### Instance Properties
- [let first: SymmetricKey?](asauthorizationpublickeycredentialprfregistrationoutput-swift.struct/first.md)
  A SymmetricKey that is unique to this passkey and derived from `input1`, if it was specified.
- [let isSupported: Bool](asauthorizationpublickeycredentialprfregistrationoutput-swift.struct/issupported.md)
- [let second: SymmetricKey?](asauthorizationpublickeycredentialprfregistrationoutput-swift.struct/second.md)
  A second SymmetricKey that is unique to this passkey, and derived from `input2` if it was specified.
### Type Properties
- [static var supported: ASAuthorizationPublicKeyCredentialPRFRegistrationOutput](asauthorizationpublickeycredentialprfregistrationoutput-swift.struct/supported.md)
- [static var unsupported: ASAuthorizationPublicKeyCredentialPRFRegistrationOutput](asauthorizationpublickeycredentialprfregistrationoutput-swift.struct/unsupported.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentialprfregistrationoutput-swift.struct)*
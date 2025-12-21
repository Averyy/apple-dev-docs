# inputValues

**Framework**: Authentication Services  
**Kind**: property

The input values to use when generating the PRF extension, if specified.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
let inputValues: ASAuthorizationPublicKeyCredentialPRFRegistrationInput.InputValues?
```

#### Discussion

If this property isn’t specified, the output only indicates whether there’s support for the extension.

## See Also

- [ASAuthorizationPublicKeyCredentialPRFRegistrationInput.InputValues](asauthorizationpublickeycredentialprfregistrationinput-swift.struct/inputvalues-swift.typealias.md)
  The type of the registration input values property.
- [static func inputValues(ASAuthorizationPublicKeyCredentialPRFRegistrationInput.InputValues) -> ASAuthorizationPublicKeyCredentialPRFRegistrationInput](asauthorizationpublickeycredentialprfregistrationinput-swift.struct/inputvalues(_:).md)
  The inputs for the PRF extension to evaluate if the new passkey supports the extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentialprfregistrationinput-swift.struct/inputvalues-swift.property)*
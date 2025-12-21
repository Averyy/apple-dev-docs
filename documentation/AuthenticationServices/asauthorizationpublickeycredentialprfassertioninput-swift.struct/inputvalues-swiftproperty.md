# inputValues

**Framework**: Authentication Services  
**Kind**: property

The input values to use when generating the PRF extension output, if specified.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
let inputValues: ASAuthorizationPublicKeyCredentialPRFAssertionInput.InputValues?
```

#### Discussion

When also using [`perCredentialInputValues`](asauthorizationpublickeycredentialprfassertioninput-swift.struct/percredentialinputvalues.md), you may use the corresponding value from that dictionary instead.

## See Also

- [static func inputValues(ASAuthorizationPublicKeyCredentialPRFAssertionInput.InputValues, perCredentialInputValues: [Data : ASAuthorizationPublicKeyCredentialPRFAssertionInput.InputValues]?) -> ASAuthorizationPublicKeyCredentialPRFAssertionInput](asauthorizationpublickeycredentialprfassertioninput-swift.struct/inputvalues(_:percredentialinputvalues:).md)
  The inputs for the PRF extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentialprfassertioninput-swift.struct/inputvalues-swift.property)*
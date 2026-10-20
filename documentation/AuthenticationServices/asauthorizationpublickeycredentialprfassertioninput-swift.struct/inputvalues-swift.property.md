# inputValues

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

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

When also using [`perCredentialInputValues`](./percredentialinputvalues.md), you may use the corresponding value from that dictionary instead.

## See Also

### Accessing input values
- [static func inputValues(ASAuthorizationPublicKeyCredentialPRFAssertionInput.InputValues, perCredentialInputValues: [Data : ASAuthorizationPublicKeyCredentialPRFAssertionInput.InputValues]?) -> ASAuthorizationPublicKeyCredentialPRFAssertionInput](./inputvalues%28_,percredentialinputvalues%29.md)
  The inputs for the PRF extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentialprfassertioninput-swift.struct/inputvalues-swift.property)*
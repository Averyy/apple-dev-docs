# inputValues(_:perCredentialInputValues:)

**Framework**: Authentication Services  
**Kind**: method

The inputs for the PRF extension.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
static func inputValues(_ inputValues: ASAuthorizationPublicKeyCredentialPRFAssertionInput.InputValues, perCredentialInputValues: [Data : ASAuthorizationPublicKeyCredentialPRFAssertionInput.InputValues]? = nil) -> ASAuthorizationPublicKeyCredentialPRFAssertionInput
```

#### Return Value

A configured instance of [`ASAuthorizationPublicKeyCredentialPRFAssertionInput`](asauthorizationpublickeycredentialprfassertioninput-swift.struct.md).

## Parameters

- `inputValues`: The default inputs to use for generating the PRF.
- `perCredentialInputValues`: This optional dictionary maps   values to alternate input values. If the user selects a passkey with a   that matches one of these keys, the extension uses the corresponding input values instead of those from the first argument. When specifying a nonempty value here, the request uses  .

## See Also

- [let inputValues: ASAuthorizationPublicKeyCredentialPRFAssertionInput.InputValues?](asauthorizationpublickeycredentialprfassertioninput-swift.struct/inputvalues-swift.property.md)
  The input values to use when generating the PRF extension output, if specified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentialprfassertioninput-swift.struct/inputvalues(_:percredentialinputvalues:))*
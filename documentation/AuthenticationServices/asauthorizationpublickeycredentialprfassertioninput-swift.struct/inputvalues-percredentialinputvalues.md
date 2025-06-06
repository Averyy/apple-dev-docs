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

A configured instance of `ASAuthorizationPublicKeyCredentialPRFAssertionInput`.

## Parameters

- `inputValues`: These are the default inputs that will be used for generating the PRF.
- `perCredentialInputValues`: This optional dictionary maps  s to alternate input values. If the user selects a passkey with a   that matches one of these keys, the corresponding input values will be used instead of those from the first argument. When specifying a non-empty value here, the request must use  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentialprfassertioninput-swift.struct/inputvalues(_:percredentialinputvalues:))*
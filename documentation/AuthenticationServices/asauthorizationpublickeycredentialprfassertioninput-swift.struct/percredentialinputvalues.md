# perCredentialInputValues(_:)

**Framework**: Authentication Services  
**Kind**: method

The inputs for the PRF extension, when not specifying general input values.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
static func perCredentialInputValues(_ perCredentialInputValues: [Data : ASAuthorizationPublicKeyCredentialPRFAssertionInput.InputValues]) -> ASAuthorizationPublicKeyCredentialPRFAssertionInput
```

#### Return Value

A configured instance of `ASAuthorizationPublicKeyCredentialPRFAssertionInput`.

## Parameters

- `perCredentialInputValues`: This dictionary maps  s to input values. If the user selects a passkey with a   that matches one of these keys, the corresponding input values will be used. If the selected passkey does not match, no PRF result will be returned. When using this option, the dictionary must be non-empty and the request must use  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentialprfassertioninput-swift.struct/percredentialinputvalues(_:))*
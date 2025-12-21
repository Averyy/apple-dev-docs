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

- `perCredentialInputValues`: This dictionary maps   values to input values. If the user selects a passkey with a   that matches one of these keys, the extension uses the corresponding input values. If the selected passkey doesn’t match, it doesn’t return a PRF result. When using this option, the dictionary needs to be nonempty and the request needs to use  .

## See Also

- [let perCredentialInputValues: [Data : ASAuthorizationPublicKeyCredentialPRFAssertionInput.InputValues]?](asauthorizationpublickeycredentialprfassertioninput-swift.struct/percredentialinputvalues.md)
  A map of credential identifiers to input values for the PRF extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentialprfassertioninput-swift.struct/percredentialinputvalues(_:))*
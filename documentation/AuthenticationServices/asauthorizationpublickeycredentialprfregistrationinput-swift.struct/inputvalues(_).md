# inputValues(_:)

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Type Method

The inputs for the PRF extension to evaluate if the new passkey supports the extension.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
static func inputValues(_ inputValues: ASAuthorizationPublicKeyCredentialPRFRegistrationInput.InputValues) -> ASAuthorizationPublicKeyCredentialPRFRegistrationInput
```

## Return Value

A configured instance of `ASAuthorizationPublicKeyCredentialPRFRegistrationInput`.

## Parameters

- `inputValues`: The inputs to use for generating the PRF.

## See Also

### Working with PRF inputs
- [let inputValues: ASAuthorizationPublicKeyCredentialPRFRegistrationInput.InputValues?](./inputvalues-swift.property.md)
  The input values to use when generating the PRF extension, if specified.
- [ASAuthorizationPublicKeyCredentialPRFRegistrationInput.InputValues](./inputvalues-swift.typealias.md)
  The type of the registration input values property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentialprfregistrationinput-swift.struct/inputvalues(_:))*
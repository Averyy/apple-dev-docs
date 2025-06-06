# inputValues(_:)

**Framework**: Authentication Services  
**Kind**: method

The inputs for the PRF extension, to evaluate if the new passkey supports this extension.

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

#### Return Value

A configured instance of `ASAuthorizationPublicKeyCredentialPRFRegistrationInput`.

## Parameters

- `inputValues`: These are the inputs that will be used for generating the PRF.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentialprfregistrationinput-swift.struct/inputvalues(_:))*
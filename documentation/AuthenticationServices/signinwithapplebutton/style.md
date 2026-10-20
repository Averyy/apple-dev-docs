# SignInWithAppleButton.Style

**Framework**: Authentication Services  
**Kind**: struct  
**Role**: Structure

The structure that defines styles that you use to control the button’s appearance.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
struct Style
```

## Topics

### Styles
- [static let black: SignInWithAppleButton.Style](./style/black.md)
  The constant that defines a black button.
- [static let white: SignInWithAppleButton.Style](./style/white.md)
  The constant that defines a white button.
- [static let whiteOutline: SignInWithAppleButton.Style](./style/whiteoutline.md)
  The constant that defines a white-outlined button.

## See Also

### Creating a button
- [init(SignInWithAppleButton.Label, onRequest: (ASAuthorizationAppleIDRequest) -> Void, onCompletion: (Result<ASAuthorization, any Error>) -> Void)](./init%28_,onrequest,oncompletion%29.md)
  Creates a Sign in with Apple button.
- [SignInWithAppleButton.Label](./label.md)
  The label that appears on the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/signinwithapplebutton/style)*
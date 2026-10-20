# SignInWithAppleButton.Label

**Framework**: Authentication Services  
**Kind**: struct  
**Role**: Structure

The label that appears on the button.

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
struct Label
```

## Topics

### Labels
- [static let `continue`: SignInWithAppleButton.Label](./label/continue.md)
  The constant that defines the Continue label on the button.
- [static let signIn: SignInWithAppleButton.Label](./label/signin.md)
  The constant that defines the Sign in with Apple label on the button.
- [static let signUp: SignInWithAppleButton.Label](./label/signup.md)
  The constant that defines the Sign up with Apple label on the button.

## See Also

### Creating a button
- [init(SignInWithAppleButton.Label, onRequest: (ASAuthorizationAppleIDRequest) -> Void, onCompletion: (Result<ASAuthorization, any Error>) -> Void)](./init%28_,onrequest,oncompletion%29.md)
  Creates a Sign in with Apple button.
- [SignInWithAppleButton.Style](./style.md)
  The structure that defines styles that you use to control the button’s appearance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/signinwithapplebutton/label)*
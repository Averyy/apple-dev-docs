# init(_:onRequest:onCompletion:)

**Framework**: Authentication Services  
**Kind**: init

Creates a Sign in with Apple button.

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
nonisolated
init(_ label: SignInWithAppleButton.Label = .signIn, onRequest: @escaping (ASAuthorizationAppleIDRequest) -> Void, onCompletion: @escaping (Result<ASAuthorization, any Error>) -> Void)
```

## Parameters

- `label`: The label that appears on the button.
- `onRequest`: The authorization request for an Apple ID.
- `onCompletion`: The completion handler that the system calls when the sign-in completes.

## See Also

- [SignInWithAppleButton.Label](signinwithapplebutton/label.md)
  The label that appears on the button.
- [SignInWithAppleButton.Style](signinwithapplebutton/style.md)
  The structure that defines styles that you use to control the button’s appearance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/signinwithapplebutton/init(_:onrequest:oncompletion:))*
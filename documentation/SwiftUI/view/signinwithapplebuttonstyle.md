# signInWithAppleButtonStyle(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the style used for displaying the control (see `SignInWithAppleButton.Style`).

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- macOS 11.0+
- tvOS 14.0+
- watchOS 7.0+

## Declaration

```swift
nonisolated
func signInWithAppleButtonStyle(_ style: SignInWithAppleButton.Style) -> some View
```

## Parameters

- `style`: The sign in style to apply to this button.

## See Also

- [struct LocalAuthenticationView](../LocalAuthentication/LocalAuthenticationView.md)
  A SwiftUI view that displays an authentication interface.
- [struct SignInWithAppleButton](../AuthenticationServices/SignInWithAppleButton.md)
  A SwiftUI view that creates the Sign in with Apple button for display.
- [var authorizationController: AuthorizationController](environmentvalues/authorizationcontroller.md)
  A value provided in the SwiftUI environment that views can use to perform authorization requests.
- [var webAuthenticationSession: WebAuthenticationSession](environmentvalues/webauthenticationsession.md)
  A value provided in the SwiftUI environment that views can use to authenticate a user through a web service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/signinwithapplebuttonstyle(_:))*
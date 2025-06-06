# authorizationController

**Framework**: SwiftUI  
**Kind**: property

A value provided in the SwiftUI environment that views can use to perform authorization requests.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- macOS 13.3+
- tvOS 16.4+
- watchOS 9.4+

## Declaration

```swift
var authorizationController: AuthorizationController { get }
```

#### Discussion

For example, you can perform authorization requests when the user taps a button:

```swift
struct AuthorizationControllerExample: View {
    @Environment(\.authorizationController) private var authorizationController

    var body: some View {
        Button("Sign In") {
            Task {
                do {
                    async let requests = authorizationRequests() // defined elsewhere
                    let result = try await authorizationController
                        .performRequests(requests)

                    switch result {
                    // code to handle the authorization result
                    }
                } catch {
                    // code to handle the authorization error
                }
            }
        }
    }
}
```

## See Also

- [@MainActor @preconcurrency struct LocalAuthenticationView<Label> where Label : View](../LocalAuthentication/LocalAuthenticationView.md)
  A SwiftUI view that displays an authentication interface.
- [@MainActor @preconcurrency struct SignInWithAppleButton](../AuthenticationServices/SignInWithAppleButton.md)
  The view that creates the Sign in with Apple button for display.
- [func signInWithAppleButtonStyle(SignInWithAppleButton.Style) -> some View](view/signinwithapplebuttonstyle(_:).md)
  Sets the style used for displaying the control (see `SignInWithAppleButton.Style`).
- [var webAuthenticationSession: WebAuthenticationSession](environmentvalues/webauthenticationsession.md)
  A value provided in the SwiftUI environment that views can use to authenticate a user through a web service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/authorizationcontroller)*
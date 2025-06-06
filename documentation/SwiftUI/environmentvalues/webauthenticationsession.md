# webAuthenticationSession

**Framework**: SwiftUI  
**Kind**: property

A value provided in the SwiftUI environment that views can use to authenticate a user through a web service.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- macOS 13.3+
- tvOS 16.4+
- watchOS 9.4+

## Declaration

```swift
var webAuthenticationSession: WebAuthenticationSession { get }
```

#### Discussion

For example, you can start a web authentication session when the user taps a button:

```swift
struct WebAuthenticationSessionExample: View {
    @Environment(\.webAuthenticationSession) private var webAuthenticationSession

    var body: some View {
        Button("Sign In") {
            Task {
                do {
                    let urlWithToken = try await webAuthenticationSession.authenticate(
                        using: URL(string: "https://www.example.com")!,
                        callbackURLScheme: "x-example-app")
                    try await signIn(using: urlWithToken) // defined elsewhere
                } catch {
                    // code to handle authentication errors
                }
            }
        }
    }
}
```

Use `WebAuthenticationSession/BrowserSession/ephemeral` to request that the browser doesn’t share cookies or other browsing data between the authentication session and the user’s normal browser session. Whether the request is honored depends on the user’s default web browser. Safari always honors the request.

```swift
let urlWithToken = try await webAuthenticationSession.authenticate(
    using: URL(string: "https://www.example.com")!,
    callbackURLScheme: "x-example-app",
    preferredBrowserSession: .ephemeral)
```

After the user authenticates, the authentication provider redirects the browser to a URL that uses the callback scheme. The browser detects the redirect, dismisses itself, and the complete URL will be returned. Inspect the URL to determine the outcome of the authentication:

```swift
let queryItems = URLComponents(string: urlWithToken.absoluteString)?.queryItems
let token = queryItems?.first(where: { $0.name == "token" })?.value
```

The above example looks for a token stored as a query parameter. The specific parsing that you have to do depends on how the authentication provider structures the callback URL.

## See Also

- [@MainActor @preconcurrency struct LocalAuthenticationView<Label> where Label : View](../LocalAuthentication/LocalAuthenticationView.md)
  A SwiftUI view that displays an authentication interface.
- [@MainActor @preconcurrency struct SignInWithAppleButton](../AuthenticationServices/SignInWithAppleButton.md)
  The view that creates the Sign in with Apple button for display.
- [func signInWithAppleButtonStyle(SignInWithAppleButton.Style) -> some View](view/signinwithapplebuttonstyle(_:).md)
  Sets the style used for displaying the control (see `SignInWithAppleButton.Style`).
- [var authorizationController: AuthorizationController](environmentvalues/authorizationcontroller.md)
  A value provided in the SwiftUI environment that views can use to perform authorization requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/webauthenticationsession)*
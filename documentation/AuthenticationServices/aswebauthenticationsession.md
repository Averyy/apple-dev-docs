# ASWebAuthenticationSession

**Framework**: Authentication Services  
**Kind**: class

A session that an app uses to authenticate a user through a web service.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+
- macOS 10.15+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
class ASWebAuthenticationSession
```

## Mentions

- [Authenticating a User Through a Web Service](authenticating-a-user-through-a-web-service.md)
- [Supporting Single Sign-On in a Web Browser App](supporting-single-sign-on-in-a-web-browser-app.md)

#### Overview

Use an [`ASWebAuthenticationSession`](aswebauthenticationsession.md) instance to authenticate a user through a web service, including one run by a third party. Initialize the session with a URL that points to the authentication webpage. When the user starts the authentication session, the operating system shows a modal view telling them which domain the app is authenticating with and asking whether to proceed. If the user proceeds with the authentication attempt, a browser loads and displays the page, from which the user can authenticate. In iOS, the browser is a secure, embedded web view. In macOS, the system opens the user’s default browser if it supports web authentication sessions, or Safari otherwise.

On completion, the service sends a callback URL to the session with an authentication token. The session passes this URL back to the app through a completion handler. [`ASWebAuthenticationSession`](aswebauthenticationsession.md) ensures that only the calling app’s session receives the authentication callback, even when more than one app registers the same callback URL scheme.

For more details, see [`Authenticating a User Through a Web Service`](authenticating-a-user-through-a-web-service.md).

## Topics

### Creating a session
- [init(url: URL, callback: ASWebAuthenticationSession.Callback, completionHandler: ASWebAuthenticationSession.CompletionHandler)](aswebauthenticationsession/init(url:callback:completionhandler:).md)
  Creates a web authentication session instance that uses a callback to evaluate a redirection URL.
- [ASWebAuthenticationSession.Callback](aswebauthenticationsession/callback.md)
  An object for evaluating navigation events in an authentication session.
- [ASWebAuthenticationSession.CompletionHandler](aswebauthenticationsession/completionhandler.md)
  A completion handler for the web authentication session.
### Configuring a session
- [var prefersEphemeralWebBrowserSession: Bool](aswebauthenticationsession/prefersephemeralwebbrowsersession.md)
  A Boolean value that indicates whether the session should ask the browser for a private authentication session.
### Starting and Stopping a Session
- [var canStart: Bool](aswebauthenticationsession/canstart.md)
  A Boolean indicating whether the session can begin.
- [func start() -> Bool](aswebauthenticationsession/start.md)
  Starts a web authentication session.
- [func cancel()](aswebauthenticationsession/cancel.md)
  Cancels a web authentication session.
### Presenting a Session
- [var presentationContextProvider: (any ASWebAuthenticationPresentationContextProviding)?](aswebauthenticationsession/presentationcontextprovider.md)
  A delegate that provides a display context in which the system can present an authentication session to the user.
- [protocol ASWebAuthenticationPresentationContextProviding](aswebauthenticationpresentationcontextproviding.md)
  An interface the session uses to ask a delegate for a presentation context.
### Recognizing Errors
- [struct ASWebAuthenticationSessionError](aswebauthenticationsessionerror.md)
  Errors that a web authentication session can generate.
- [let ASWebAuthenticationSessionErrorDomain: String](aswebauthenticationsessionerrordomain.md)
  The error domain for a web authentication session.
- [ASWebAuthenticationSessionError.Code](aswebauthenticationsessionerror/code.md)
  The error code for a web authentication session error.
### Instance properties
- [var additionalHeaderFields: [String : String]?](aswebauthenticationsession/additionalheaderfields.md)
  Any additional header fields to set when loading the initial URL.
### Deprecated symbols
- [init(url: URL, callbackURLScheme: String?, completionHandler: ASWebAuthenticationSession.CompletionHandler)](aswebauthenticationsession/init(url:callbackurlscheme:completionhandler:).md)
  Creates a web authentication session instance.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Authenticating a User Through a Web Service](authenticating-a-user-through-a-web-service.md)
  Use a web authentication session to authenticate a user in your app.
- [Securing Logins with iCloud Keychain Verification Codes](securing-logins-with-icloud-keychain-verification-codes.md)
  Use time-based codes generated on-device for a secure authentication experience.
- [struct WebAuthenticationSession](webauthenticationsession.md)
  A SwiftUI environment value that views use to authenticate someone using a web service.
- [Supporting Single Sign-On in a Web Browser App](supporting-single-sign-on-in-a-web-browser-app.md)
  Extend your web browser app to handle web authentication requests from other apps.
- [class ASWebAuthenticationSessionWebBrowserSessionManager](aswebauthenticationsessionwebbrowsersessionmanager.md)
  A session manager that mediates sharing data between an app and a web browser.
- [ASWebAuthenticationSessionWebBrowserSupportCapabilities](../BundleResources/Information-Property-List/ASWebAuthenticationSessionWebBrowserSupportCapabilities.md)
  A collection of keys that a browser app uses to declare its ability to handle authentication requests from other apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aswebauthenticationsession)*
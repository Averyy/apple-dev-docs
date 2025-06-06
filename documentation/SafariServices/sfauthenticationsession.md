# SFAuthenticationSession

**Framework**: Safari Services  
**Kind**: class

A class that manages sharing a one-time login between Safari and an app, which can also provide automatic login for associated apps.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class SFAuthenticationSession
```

#### Overview

Along with the login, this class manages sharing cookies and website data.

The two cases where you would use `SFAuthenticationSession` are:

- Logging in to a third party’s service using an authentication protocol (for example, OAuth). This option works well for social network applications.
- Providing a single sign-on (SSO) experience for applications. This option works well for enterprise companies that have many applications installed on the same device.

> **Note**:  Ensure that there is a strong reference to the `SFAuthenticationSession` instance when the session is in progress.

 Ensure that there is a strong reference to the `SFAuthenticationSession` instance when the session is in progress.

If an application uses `SFAuthenticationSession`, users are prompted by a dialog to give explicit consent, allowing the application to access the website’s data in Safari. When the webpage is presented, it runs in a separate process, so the user and web service are guaranteed that the app has no way to gain access to the user’s credentials. Instead, the app gets a unique authentication token.

Then, `SFAuthenticationSession` has a simple completion handler that’s called when the session completes. After instantiating `SFAuthenticationSession`, use the start method to show the consent dialog. If the user consents, the session will begin. If at any time you wants to stop the session, call cancel to dismiss the consent dialog or dismiss the webpage. When the session is dismissed, the completion handler is called. Then, the web service redirects to the expected URL, which contains the unique authentication token. A user can decide not to log in to the session either when they are prompted with the consent dialog or after this when they’re viewing the login page. In both cases, the completion handler will be called with the error `SFAuthenticationErrorCanceledLogin`.

The dismiss button in `SFAuthenticationSession` always says Cancel. Applications can’t add their own UIActivities to the Share Sheet or exclude items from the Share Sheet. However, the Share Sheet can still be used, in case the user needs a password manager to log in; additionally, it excludes items that could prevent login.

## Topics

### Type Aliases
- [SFAuthenticationSession.CompletionHandler](sfauthenticationsession/completionhandler.md)
  The completion handler for an authentication session when the user cancels or finishes the login.
### Initializers
- [init(url: URL, callbackURLScheme: String?, completionHandler: SFAuthenticationSession.CompletionHandler)](sfauthenticationsession/init(url:callbackurlscheme:completionhandler:).md)
  Initializes the SFAuthenticationSession in an application.
### Instance Methods
- [func cancel()](sfauthenticationsession/cancel.md)
  Cancels the currently running session when the consent dialog is up or when the webpage is up. This is how applications stop the login process.
- [func start() -> Bool](sfauthenticationsession/start.md)
  Starts the session after initializing an instance of SFAuthenticationSession. This will trigger the consent dialog.

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

- [let SFContentBlockerErrorDomain: String](sfcontentblockererrordomain.md)
  The domain for content blocker errors.
- [enum SFContentBlockerErrorCode](sfcontentblockererrorcode.md)
  Messages that describe a content blocker error.
- [struct SFAuthenticationError](sfauthenticationerror-swift.struct.md)
  An authentication error.
- [SFAuthenticationError.Code](sfauthenticationerror-swift.struct/code.md)
  Messages that describe an authentication error.
- [let SFAuthenticationErrorDomain: String](sfauthenticationerrordomain.md)
  The domain for authentication errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfauthenticationsession)*
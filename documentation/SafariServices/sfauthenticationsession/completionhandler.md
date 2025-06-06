# SFAuthenticationSession.CompletionHandler

**Framework**: Safari Services  
**Kind**: typealias

The completion handler for an authentication session when the user cancels or finishes the login.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.0+

## Declaration

```swift
typealias CompletionHandler = (URL?, (any Error)?) -> Void
```

#### Discussion

The custom callback URL should only be a custom URL scheme, and not a standard scheme (e.g. http or https). The session looks at the scheme registered first and routes to the app asking to start a session before potentially routing the scheme to another app.

## See Also

- [class SFSafariViewController](sfsafariviewcontroller.md)
  An object that provides a visible standard interface for browsing the web.
- [Importing data exported from Safari](importing-data-exported-from-safari.md)
  Transfer bookmarks, saved passwords, and other information between browsers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfauthenticationsession/completionhandler)*
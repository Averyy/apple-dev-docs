# ASWebAuthenticationSession.CompletionHandler

**Framework**: Authentication Services  
**Kind**: typealias

A completion handler for the web authentication session.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
typealias CompletionHandler = (URL?, (any Error)?) -> Void
```

## See Also

- [init(url: URL, callback: ASWebAuthenticationSession.Callback, completionHandler: ASWebAuthenticationSession.CompletionHandler)](aswebauthenticationsession/init(url:callback:completionhandler:).md)
  Creates a web authentication session instance that uses a callback to evaluate a redirection URL.
- [ASWebAuthenticationSession.Callback](aswebauthenticationsession/callback.md)
  An object for evaluating navigation events in an authentication session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aswebauthenticationsession/completionhandler)*
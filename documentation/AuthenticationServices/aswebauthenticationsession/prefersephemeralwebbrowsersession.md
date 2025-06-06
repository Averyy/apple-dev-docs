# prefersEphemeralWebBrowserSession

**Framework**: Authentication Services  
**Kind**: property

A Boolean value that indicates whether the session should ask the browser for a private authentication session.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
var prefersEphemeralWebBrowserSession: Bool { get set }
```

## Mentions

- [Authenticating a User Through a Web Service](authenticating-a-user-through-a-web-service.md)

#### Discussion

Set [`prefersEphemeralWebBrowserSession`](aswebauthenticationsession/prefersephemeralwebbrowsersession.md) to `true` to request that the browser doesn’t share cookies or other browsing data between the authentication session and the user’s normal browser session. Whether the request is honored depends on the user’s default web browser. Safari always honors the request.

The value of this property is `false` by default.

Set this property before you call [`start()`](aswebauthenticationsession/start().md). Otherwise it has no effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aswebauthenticationsession/prefersephemeralwebbrowsersession)*
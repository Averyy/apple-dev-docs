# authenticate(using:callback:preferredBrowserSession:additionalHeaderFields:)

**Framework**: Authentication Services  
**Kind**: method

Begins a web authentication session.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
@MainActor
func authenticate(using url: URL, callback: ASWebAuthenticationSession.Callback, preferredBrowserSession: WebAuthenticationSession.BrowserSession? = nil, additionalHeaderFields: [String : String]) async throws -> URL
```

#### Discussion

This initializer throws an error if `additionalHeaderFields` includes a “forbidden request-header” as defined by the WHATWG.

## Parameters

- `url`: A URL beginning with HTTP or HTTPS that points to the authentication webpage.
- `callback`: An object that describes when the session calls its completion handler.
- `preferredBrowserSession`: The preferred data-sharing behavior of the browser session. For more information, see  .
- `additionalHeaderFields`: A dictionary containing additional header fields to send when loading the initial URL.

## See Also

- [WebAuthenticationSession.BrowserSession](webauthenticationsession/browsersession.md)
  Describes the preferred browser session behavior.
- [ASWebAuthenticationSession.Callback](aswebauthenticationsession/callback.md)
  An object for evaluating navigation events in an authentication session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/webauthenticationsession/authenticate(using:callback:preferredbrowsersession:additionalheaderfields:))*
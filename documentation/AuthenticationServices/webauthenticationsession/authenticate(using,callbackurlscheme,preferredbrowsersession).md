# authenticate(using:callbackURLScheme:preferredBrowserSession:)

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

Begins a web authentication session.

**Availability**:
- iOS 16.4+ - Deprecated in 27.2
- iPadOS 16.4+ - Deprecated in 27.2
- Mac Catalyst 16.4+ - Deprecated in 27.2
- macOS 13.3+ - Deprecated in 27.2
- tvOS 16.4+ - Deprecated in 27.2
- visionOS 1.0+
- watchOS 9.4+ - Deprecated in 27.2

> **Deprecated**: Use [`authenticate(using:callback:preferredBrowserSession:additionalHeaderFields:)`](./authenticate%28using,callback,preferredbrowsersession,additionalheaderfields%29.md) to handle callbacks.

## Declaration

```swift
@MainActor
func authenticate(using url: URL, callbackURLScheme: String, preferredBrowserSession: WebAuthenticationSession.BrowserSession? = nil) async throws -> URL
```

#### Return Value

The URL that the authentication provider returns.

## Parameters

- `url`: A URL beginning with HTTP or HTTPS that points to the authentication webpage.
- `callbackURLScheme`: The app’s custom callback scheme.
- `preferredBrowserSession`: The preferred data-sharing behavior of the browser session. For more information, see [`WebAuthenticationSession.BrowserSession`](./browsersession.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/webauthenticationsession/authenticate(using:callbackurlscheme:preferredbrowsersession:))*
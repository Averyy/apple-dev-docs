# authenticate(using:callbackURLScheme:preferredBrowserSession:)

**Framework**: Authentication Services  
**Kind**: method

Begins a web authentication session.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 1.0+
- watchOS 9.4+

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
- `preferredBrowserSession`: The preferred data-sharing behavior of the browser session. For more information, see  .

## See Also

- [WebAuthenticationSession.BrowserSession](webauthenticationsession/browsersession.md)
  Describes the preferred browser session behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/webauthenticationsession/authenticate(using:callbackurlscheme:preferredbrowsersession:))*
# WebAuthenticationSession.BrowserSession

**Framework**: Authentication Services  
**Kind**: struct

Describes the preferred browser session behavior.

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
struct BrowserSession
```

## Topics

### Behaviors
- [static var ephemeral: WebAuthenticationSession.BrowserSession](webauthenticationsession/browsersession/ephemeral.md)
  A session that doesn’t share cookies or other browsing data with a person’s normal browser session.
- [static var shared: WebAuthenticationSession.BrowserSession](webauthenticationsession/browsersession/shared.md)
  A session that can share cookies and other browsing data with a person’s normal browser session.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func authenticate(using: URL, callbackURLScheme: String, preferredBrowserSession: WebAuthenticationSession.BrowserSession?) async throws -> URL](webauthenticationsession/authenticate(using:callbackurlscheme:preferredbrowsersession:).md)
  Begins a web authentication session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/webauthenticationsession/browsersession)*
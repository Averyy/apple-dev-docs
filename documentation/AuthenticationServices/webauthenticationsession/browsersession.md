# WebAuthenticationSession.BrowserSession

**Framework**: Authentication Services  
**Kind**: struct  
**Role**: Structure

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
- [static var ephemeral: WebAuthenticationSession.BrowserSession](./browsersession/ephemeral.md)
  A session that doesn’t share cookies or other browsing data with a person’s normal browser session.
- [static var shared: WebAuthenticationSession.BrowserSession](./browsersession/shared.md)
  A session that can share cookies and other browsing data with a person’s normal browser session.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Authenticating a session
- [func authenticate(using: URL, callback: ASWebAuthenticationSession.Callback, preferredBrowserSession: WebAuthenticationSession.BrowserSession?, additionalHeaderFields: [String : String]) async throws -> URL](./authenticate%28using,callback,preferredbrowsersession,additionalheaderfields%29.md)
  Begins a web authentication session.
- [ASWebAuthenticationSession.Callback](../aswebauthenticationsession/callback.md)
  An object for evaluating navigation events in an authentication session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/webauthenticationsession/browsersession)*
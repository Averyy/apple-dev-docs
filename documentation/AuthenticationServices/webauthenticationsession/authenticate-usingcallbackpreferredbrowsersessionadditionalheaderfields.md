# authenticate(using:callback:preferredBrowserSession:additionalHeaderFields:)

**Framework**: Authentication Services  
**Kind**: method

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/webauthenticationsession/authenticate(using:callback:preferredbrowsersession:additionalheaderfields:))*
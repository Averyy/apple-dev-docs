# developerToken(options:)

**Framework**: MusicKit  
**Kind**: method  
**Required**: Yes

Fetches and returns a developer token for Apple Music API.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func developerToken(options: MusicTokenRequestOptions) async throws -> String
```

#### Discussion

If you opt to create a custom implementation of the [`MusicDeveloperTokenProvider`](musicdevelopertokenprovider.md) protocol, make sure to discard any cached developer token if the `options` parameter contains [`ignoreCache`](musictokenrequestoptions/ignorecache.md).

You can add the newly generated token to an in-memory or persistent cache for faster access upon subsequent requests for this token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicdevelopertokenprovider/developertoken(options:))*
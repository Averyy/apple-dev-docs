# pushToStartToken

**Framework**: Now Playing  
**Kind**: property

The token you use to start a [`RemoteMediaSession`](remotemediasession.md) through a push notification.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
static var pushToStartToken: Data? { get }
```

## Mentions

- [Publishing remote media sessions](publishing-remote-media-sessions.md)

#### Discussion

The push token for a [`RemoteMediaSession`](remotemediasession.md) may change over time. Use the [`pushToStartTokenUpdates`](remotemediasession/pushtostarttokenupdates.md) asynchronous sequence to receive an updated push-to-start token.

> **Note**: When you receive an updated push token, transmit it securely to your server (for example, over HTTPS) and invalidate the outdated token promptly so it cannot be reused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/remotemediasession/pushtostarttoken)*
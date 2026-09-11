# pushToStartTokenUpdates

**Framework**: Now Playing  
**Kind**: property

An asynchronous sequence that delivers updated tokens for starting a [`RemoteMediaSession`](remotemediasession.md) through a push notification.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
@MainActor
static var pushToStartTokenUpdates: AsyncStream<Data> { get }
```

## Mentions

- [Publishing remote media sessions](publishing-remote-media-sessions.md)

#### Discussion

Use push notifications to start new remote sessions and update ongoing ones. For additional information, see [`Publishing remote media sessions`](publishing-remote-media-sessions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/remotemediasession/pushtostarttokenupdates)*
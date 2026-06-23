# pushTokenUpdates

**Framework**: Now Playing  
**Kind**: property

An asynchronous sequence you use to observe changes to the push token of this remote session.

**Availability**:
- iOS 27.0+ (Beta)
- iOS App Extension 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
var pushTokenUpdates: AsyncStream<Data> { get }
```

## Mentions

- [Publishing remote media sessions](publishing-remote-media-sessions.md)

#### Discussion

Monitor this sequence to receive updated push tokens. When the token changes, transmit the new token securely to your server so the server can continue to send update and end push notifications for this session. Invalidate the outdated token promptly so it cannot be reused, and retain the token only as long as needed to deliver session updates.

For additional information, see [`Publishing remote media sessions`](publishing-remote-media-sessions.md)

> **Note**: Push tokens are device-scoped identifiers. Handle them securely on your server (for example, over HTTPS) and follow your app’s privacy policy for any data collected alongside them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/remotemediasessionrepresentable/pushtokenupdates)*
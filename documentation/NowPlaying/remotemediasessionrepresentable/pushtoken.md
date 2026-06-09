# pushToken

**Framework**: Now Playing  
**Kind**: property

The token you use to send push notifications to update this remote session.

**Availability**:
- iOS 27.0+ (Beta)
- iOS App Extension 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
var pushToken: Data? { get }
```

## Mentions

- [Publishing remote media sessions](publishing-remote-media-sessions.md)

#### Discussion

The push token for a remote session may change over time. Use [`pushTokenUpdates`](remotemediasessionrepresentable/pushtokenupdates.md) to receive the updated push token.

> **Note**: When you receive an updated push token, transmit it securely to your server (for example, over HTTPS) and invalidate the outdated token promptly so it cannot be reused. The push token is a device-scoped identifier — handle it securely and retain it only as long as needed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/remotemediasessionrepresentable/pushtoken)*
# removeSession(_:)

**Framework**: AVSystemRouting  
**Kind**: method

Removes a session from the active route.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
final func removeSession(_ session: AVSystemRouteSession)
```

## Mentions

- [Routing and streaming media to remote devices](routing-and-streaming-media-to-remote-devices.md)

#### Discussion

Call this function to unregister a session from the route when playback ends or when you no longer need the session. Removing a session stops any ongoing communication associated with that session and releases system resources.

If the session is currently active, this function stops the session before removing it.

> ❗ **Important**: Always remove sessions when they are no longer needed to ensure proper cleanup of system resources and network connections. To start new playback after removing a session, create a new [`AVSystemRouteSession`](avsystemroutesession-gp78.md) instance.

## Parameters

- `session`: The session to remove from this route. If the session is not currently associated with this route, this function has no effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avsystemrouting/avsystemroute-5s2um/removesession(_:))*
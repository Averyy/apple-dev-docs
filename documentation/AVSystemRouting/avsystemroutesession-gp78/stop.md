# stop()

**Framework**: AVSystemRouting  
**Kind**: method

Stops the session and terminates media playback on the remote device.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
final func stop()
```

## Mentions

- [Routing and streaming media to remote devices](routing-and-streaming-media-to-remote-devices.md)

#### Discussion

Call this function to end the playback session and clean up resources on both the local and remote devices. After calling this function, the session is terminated and further calls to session functions will have no effect.

The system automatically handles disconnection and cleanup of the remote app or player. If you need to start playback again, create a new [`AVSystemRouteSession`](avsystemroutesession-gp78.md) instance.

> **Note**: Always call this function when playback ends to ensure proper resource cleanup and to notify the remote device that the session has concluded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avsystemrouting/avsystemroutesession-gp78/stop())*
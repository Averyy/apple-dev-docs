# stop

**Framework**: AVSystemRouting  
**Kind**: method  
**Role**: Instance Method

Stops the session and terminates media playback on the remote device.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```objc
- (void) stop;
```

## Discussion

Call this method to end the playback session and clean up resources on both the local and remote devices. After calling this method, the session is terminated and further calls to session methods will have no effect.

The system automatically handles disconnection and cleanup of the remote application or player. If you need to start playback again, create a new [`AVSystemRouteSession`](../avsystemroutesession-5i6j6.md) instance.

> **Note**: Always call this method when playback ends to ensure proper resource cleanup and to notify the remote device that the session has concluded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avsystemrouting/avsystemroutesession-5i6j6/stop)*
# pause()

**Framework**: Nearby Interaction  
**Kind**: method

Stops sending distance and direction updates to the peer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- watchOS 7.3+

## Declaration

```swift
func pause()
```

#### Discussion

To resume a paused session, the app calls [`run(_:)`](nisession/run(_:).md), passing in the session’s configuration.

If an app pauses the session for too long, the peer receives [`session(_:didRemove:reason:)`](nisessiondelegate/session(_:didremove:reason:).md) callback with the [`NINearbyObject.RemovalReason.timeout`](ninearbyobject/removalreason/timeout.md) reason.

## See Also

- [var delegate: (any NISessionDelegate)?](nisession/delegate.md)
  An object that the framework notifies of session events.
- [func invalidate()](nisession/invalidate.md)
  Stops a running session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nisession/pause())*
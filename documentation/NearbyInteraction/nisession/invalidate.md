# invalidate()

**Framework**: Nearby Interaction  
**Kind**: method

Stops a running session.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- watchOS 7.3+

## Declaration

```swift
func invalidate()
```

#### Discussion

When an app calls this function, NI invokes [`session(_:didRemove:reason:)`](nisessiondelegate/session(_:didremove:reason:).md) on the peer’s side and passes in the `reason` [`NINearbyObject.RemovalReason.peerEnded`](ninearbyobject/removalreason/peerended.md). The app can’t restart invalid sessions.

## See Also

- [var delegate: (any NISessionDelegate)?](nisession/delegate.md)
  An object that the framework notifies of session events.
- [func pause()](nisession/pause.md)
  Stops sending distance and direction updates to the peer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nisession/invalidate())*
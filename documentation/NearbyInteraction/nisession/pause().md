# pause()

**Framework**: Nearby Interaction  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) pause;
```

#### Discussion

To resume a paused session, the app calls [`run(_:)`](./run%28_%29.md), passing in the session’s configuration.

If an app pauses the session for too long, the peer receives [`session(_:didRemove:reason:)`](../nisessiondelegate/session%28_,didremove,reason%29.md) callback with the [`NINearbyObject.RemovalReason.timeout`](../ninearbyobject/removalreason/timeout.md) reason.

## See Also

### Managing life cycle
- [var delegate: (any NISessionDelegate)?](./delegate.md)
  An object that the framework notifies of session events.
- [func invalidate()](./invalidate%28%29.md)
  Stops a running session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nisession/pause())*
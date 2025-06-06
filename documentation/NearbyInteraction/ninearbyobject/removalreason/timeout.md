# NINearbyObject.RemovalReason.timeout

**Framework**: Nearby Interaction  
**Kind**: case

NI timed out the session.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- watchOS 7.3+

## Declaration

```swift
case timeout
```

#### Discussion

The framework times out a session if the peer user closes the app, or if too much time passes in a suspended state (see [`sessionWasSuspended(_:)`](nisessiondelegate/sessionwassuspended(_:).md)). NI may also time out a session to save device resources.

An app must watch for timed-out peers. If the app wishes to continue interaction with a timed-out peer device, the app must begin a new session.

## See Also

- [NINearbyObject.RemovalReason.peerEnded](ninearbyobject/removalreason/peerended.md)
  The peer ended the session.
- [NINearbyObject.RemovalReason.peerEnded](ninearbyobject/removalreason/peerended.md)
  The peer ended the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/ninearbyobject/removalreason/timeout)*
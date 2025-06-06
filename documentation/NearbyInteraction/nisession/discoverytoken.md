# discoveryToken

**Framework**: Nearby Interaction  
**Kind**: property

A temporary, random identifier for a device.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- watchOS 7.3+

## Declaration

```swift
@NSCopying
var discoveryToken: NIDiscoveryToken? { get }
```

## Mentions

- [Initiating and maintaining a session](initiating-and-maintaining-a-session.md)
- [Discovering peers with Multipeer Connectivity](discovering-peers-with-multipeer-connectivity.md)

#### Discussion

NI sets this property when an app initializes a session. The value of [`discoveryToken`](ninearbyobject/discoverytoken.md) is unique to the session and identifies the device that created the session.

To begin a session, an app shares this object with a nearby peer using a network technology that both devices agree to. For an example that shares discovery tokens using [`Multipeer Connectivity`](https://developer.apple.com/documentation/MultipeerConnectivity), see [`Implementing Interactions Between Users in Close Proximity`](implementing-interactions-between-users-in-close-proximity.md).

## See Also

- [class NIDiscoveryToken](nidiscoverytoken.md)
  An object that uniquely identifies a peer that participates in an interaction session.
- [func run(NIConfiguration)](nisession/run(_:).md)
  Starts a session with a nearby peer.
- [var configuration: NIConfiguration?](nisession/configuration.md)
  The configuration run by the session.
- [var delegateQueue: dispatch_queue_t?](nisession/delegatequeue.md)
  The dispatch queue on which the session invokes delegate callbacks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nisession/discoverytoken)*
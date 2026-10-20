# discoveryToken

**Framework**: Nearby Interaction  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, copy, readonly, nullable) NIDiscoveryToken * discoveryToken;
```

## Mentions

- [Initiating and maintaining a session](../initiating-and-maintaining-a-session.md)
- [Discovering peers with Multipeer Connectivity](../discovering-peers-with-multipeer-connectivity.md)

#### Discussion

NI sets this property when an app initializes a session. The value of [`discoveryToken`](../ninearbyobject/discoverytoken.md) is unique to the session and identifies the device that created the session.

To begin a session, an app shares this object with a nearby peer using a network technology that both devices agree to. For an example that shares discovery tokens using [Multipeer Connectivity](../../MultipeerConnectivity/MultipeerConnectivity.md), see [Implementing interactions between users in close proximity](../implementing-interactions-between-users-in-close-proximity.md).

## See Also

### Connecting to a peer device
- [class NIDiscoveryToken](../nidiscoverytoken.md)
  An object that uniquely identifies a peer that participates in an interaction session.
- [func run(NIConfiguration)](./run%28_%29.md)
  Starts a session with a nearby peer.
- [var configuration: NIConfiguration?](./configuration.md)
  The configuration run by the session.
- [var delegateQueue: dispatch_queue_t?](./delegatequeue.md)
  The dispatch queue on which the session invokes delegate callbacks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nisession/discoverytoken)*
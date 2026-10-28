# delegateQueue

**Framework**: Nearby Interaction  
**Kind**: property  
**Role**: Instance Property

The dispatch queue on which the session invokes delegate callbacks.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- watchOS 7.3+

## Declaration

```swift
var delegateQueue: dispatch_queue_t? { get set }
```

```objc
@property (nonatomic, strong, nullable) dispatch_queue_t delegateQueue;
```

## Discussion

By default, NI invokes delegate callbacks on [`main`](../../Dispatch/dispatchqueue/main.md).

## See Also

### Connecting to a peer device
- [var discoveryToken: NIDiscoveryToken?](./discoverytoken.md)
  A temporary, random identifier for a device.
- [class NIDiscoveryToken](../nidiscoverytoken.md)
  An object that uniquely identifies a peer that participates in an interaction session.
- [func run(NIConfiguration)](./run%28_%29.md)
  Starts a session with a nearby peer.
- [var configuration: NIConfiguration?](./configuration.md)
  The configuration run by the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nisession/delegatequeue)*
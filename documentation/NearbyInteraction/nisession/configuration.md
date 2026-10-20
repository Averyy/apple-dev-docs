# configuration

**Framework**: Nearby Interaction  
**Kind**: property  
**Role**: Instance Property

The configuration run by the session.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- watchOS 7.3+

## Declaration

```swift
@NSCopying
var configuration: NIConfiguration? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NIConfiguration * configuration;
```

#### Discussion

An app doesn’t set this property. Instead, NI sets its value to reflect the object that the app passed in to [`run(_:)`](./run%28_%29.md).

## See Also

### Connecting to a peer device
- [var discoveryToken: NIDiscoveryToken?](./discoverytoken.md)
  A temporary, random identifier for a device.
- [class NIDiscoveryToken](../nidiscoverytoken.md)
  An object that uniquely identifies a peer that participates in an interaction session.
- [func run(NIConfiguration)](./run%28_%29.md)
  Starts a session with a nearby peer.
- [var delegateQueue: dispatch_queue_t?](./delegatequeue.md)
  The dispatch queue on which the session invokes delegate callbacks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nisession/configuration)*
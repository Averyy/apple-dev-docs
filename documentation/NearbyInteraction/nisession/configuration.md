# configuration

**Framework**: Nearby Interaction  
**Kind**: property

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

#### Discussion

An app doesn’t set this property. Instead, NI sets its value to reflect the object that the app passed in to [`run(_:)`](nisession/run(_:).md).

## See Also

- [var discoveryToken: NIDiscoveryToken?](nisession/discoverytoken.md)
  A temporary, random identifier for a device.
- [class NIDiscoveryToken](nidiscoverytoken.md)
  An object that uniquely identifies a peer that participates in an interaction session.
- [func run(NIConfiguration)](nisession/run(_:).md)
  Starts a session with a nearby peer.
- [var delegateQueue: dispatch_queue_t?](nisession/delegatequeue.md)
  The dispatch queue on which the session invokes delegate callbacks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nisession/configuration)*
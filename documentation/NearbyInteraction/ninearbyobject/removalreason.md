# NINearbyObject.RemovalReason

**Framework**: Nearby Interaction  
**Kind**: enum

The reason a session removed a nearby object.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- watchOS 7.3+

## Declaration

```swift
enum RemovalReason
```

#### Overview

Each case is a possible value of the `reason` argument to the delegate’s [`session(_:didRemove:reason:)`](nisessiondelegate/session(_:didremove:reason:).md) callback.

## Topics

### Reasons
- [NINearbyObject.RemovalReason.peerEnded](ninearbyobject/removalreason/peerended.md)
  The peer ended the session.
- [NINearbyObject.RemovalReason.timeout](ninearbyobject/removalreason/timeout.md)
  NI timed out the session.
- [NINearbyObject.RemovalReason.peerEnded](ninearbyobject/removalreason/peerended.md)
  The peer ended the session.
- [NINearbyObject.RemovalReason.timeout](ninearbyobject/removalreason/timeout.md)
  NI timed out the session.
### Initializers
- [init?(rawValue: Int)](ninearbyobject/removalreason/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/ninearbyobject/removalreason)*
# NINearbyObject.RemovalReason

**Framework**: Nearby Interaction  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum NINearbyObjectRemovalReason : NSInteger;
```

## Overview

Each case is a possible value of the `reason` argument to the delegate’s [`session(_:didRemove:reason:)`](../nisessiondelegate/session%28_,didremove,reason%29.md) callback.

## Topics

### Reasons
- [NINearbyObject.RemovalReason.peerEnded](./removalreason/peerended.md)
  The peer ended the session.
- [NINearbyObject.RemovalReason.timeout](./removalreason/timeout.md)
  NI timed out the session.
- [NINearbyObject.RemovalReason.peerEnded](./removalreason/peerended.md)
  The peer ended the session.
- [NINearbyObject.RemovalReason.timeout](./removalreason/timeout.md)
  NI timed out the session.
### Initializers
- [init?(rawValue: Int)](./removalreason/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/ninearbyobject/removalreason)*
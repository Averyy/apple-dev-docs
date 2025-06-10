# SRDeletionReason

**Framework**: SensorKit  
**Kind**: enum

Reasons that the framework deletes samples.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
enum SRDeletionReason
```

## Topics

### Reasons
- [SRDeletionReason.ageLimit](srdeletionreason/agelimit.md)
  Indicates that the sample outlived the framework’s retention limit.
- [SRDeletionReason.lowDiskSpace](srdeletionreason/lowdiskspace.md)
  Indicates that the system’s disk space is low.
- [SRDeletionReason.noInterestedClients](srdeletionreason/nointerestedclients.md)
  Indicates that the sensor has no active stakeholders.
- [SRDeletionReason.systemInitiated](srdeletionreason/systeminitiated.md)
  Indicates that the system requests deletion.
- [SRDeletionReason.userInitiated](srdeletionreason/userinitiated.md)
  Indicates that the user requests deletion.
### Initializers
- [init?(rawValue: Int)](srdeletionreason/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var reason: SRDeletionReason](srdeletionrecord/reason.md)
  The reason the framework deletes samples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srdeletionreason)*
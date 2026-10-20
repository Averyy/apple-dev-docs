# SRDeletionReason.lowDiskSpace

**Framework**: SensorKit  
**Kind**: case  
**Role**: Case

Indicates that the system’s disk space is low.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
case lowDiskSpace
```

```c
SRDeletionReasonLowDiskSpace
```

## See Also

### Reasons
- [SRDeletionReason.ageLimit](./agelimit.md)
  Indicates that the sample outlived the framework’s retention limit.
- [SRDeletionReason.noInterestedClients](./nointerestedclients.md)
  Indicates that the sensor has no active stakeholders.
- [SRDeletionReason.systemInitiated](./systeminitiated.md)
  Indicates that the system requests deletion.
- [SRDeletionReason.userInitiated](./userinitiated.md)
  Indicates that the user requests deletion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srdeletionreason/lowdiskspace)*
# SRDeletionReason.noInterestedClients

**Framework**: SensorKit  
**Kind**: case

Indicates that the sensor has no active stakeholders.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
case noInterestedClients
```

#### Discussion

The framework deletes samples for this reason when there’s been no recording activity for a particular sensor.

## See Also

- [SRDeletionReason.ageLimit](srdeletionreason/agelimit.md)
  Indicates that the sample outlived the framework’s retention limit.
- [SRDeletionReason.lowDiskSpace](srdeletionreason/lowdiskspace.md)
  Indicates that the system’s disk space is low.
- [SRDeletionReason.systemInitiated](srdeletionreason/systeminitiated.md)
  Indicates that the system requests deletion.
- [SRDeletionReason.userInitiated](srdeletionreason/userinitiated.md)
  Indicates that the user requests deletion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srdeletionreason/nointerestedclients)*
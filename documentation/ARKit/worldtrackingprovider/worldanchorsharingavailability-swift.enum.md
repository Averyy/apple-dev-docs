# WorldTrackingProvider.WorldAnchorSharingAvailability

**Framework**: ARKit  
**Kind**: enum  
**Role**: Enumeration

Enumeration indicating the availability of world anchor sharing.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
enum WorldAnchorSharingAvailability
```

## Topics

### Enumeration Cases
- [WorldTrackingProvider.WorldAnchorSharingAvailability.available](./worldanchorsharingavailability-swift.enum/available.md)
  World anchors can be shared with nearby participants. This indicates that the device is in a SharePlay session with nearby participants.
- [WorldTrackingProvider.WorldAnchorSharingAvailability.unavailable](./worldanchorsharingavailability-swift.enum/unavailable.md)
  World anchors cannot be shared with nearby participants. This indicates that either there’s no SharePlay session or the session has ended.
### Instance Properties
- [var description: String](./worldanchorsharingavailability-swift.enum/description.md)
  A textual representation of this world anchor sharing availability.

## Relationships

### Conforms To
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/worldtrackingprovider/worldanchorsharingavailability-swift.enum)*
# WorldTrackingProvider.WorldAnchorSharingAvailability

**Framework**: ARKit  
**Kind**: enum

Enumeration indicating the availability of world anchor sharing.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
enum WorldAnchorSharingAvailability
```

## Topics

### Enumeration Cases
- [WorldTrackingProvider.WorldAnchorSharingAvailability.available](worldtrackingprovider/worldanchorsharingavailability-swift.enum/available.md)
  World anchors can be shared with nearby participants. This indicates that the device is in a SharePlay session with nearby participants.
- [WorldTrackingProvider.WorldAnchorSharingAvailability.unavailable](worldtrackingprovider/worldanchorsharingavailability-swift.enum/unavailable.md)
  World anchors cannot be shared with nearby participants. This indicates that either there’s no SharePlay session or the session has ended.
### Instance Properties
- [var description: String](worldtrackingprovider/worldanchorsharingavailability-swift.enum/description.md)
  A textual representation of this world anchor sharing availability.

## Relationships

### Conforms To
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/worldtrackingprovider/worldanchorsharingavailability-swift.enum)*
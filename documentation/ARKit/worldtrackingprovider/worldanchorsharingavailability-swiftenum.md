# WorldTrackingProvider.WorldAnchorSharingAvailability

**Framework**: ARKit  
**Kind**: enum

Enumeration indicating the availability of world anchor sharing.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
enum WorldAnchorSharingAvailability
```

## Topics

### Enumeration Cases
- [WorldTrackingProvider.WorldAnchorSharingAvailability.available](worldtrackingprovider/worldanchorsharingavailability-swift.enum/available.md)
  World anchors can be shared with nearby participants. Indicates that the device is in a SharePlay session with nearby participants.
- [WorldTrackingProvider.WorldAnchorSharingAvailability.unavailable](worldtrackingprovider/worldanchorsharingavailability-swift.enum/unavailable.md)
  World anchors cannot be shared with nearby participants. This indicates that either there’s no SharePlay session or the session has ended.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/worldtrackingprovider/worldanchorsharingavailability-swift.enum)*
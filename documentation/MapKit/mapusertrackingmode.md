# MapUserTrackingMode

**Framework**: MapKit  
**Kind**: enum  
**Role**: Enumeration

The modes available for user tracking.

**Availability**:
- iOS 14.0+ - Deprecated in 17.0
- iPadOS 14.0+ - Deprecated in 17.0
- Mac Catalyst 14.0+ - Deprecated in 17.0
- macOS 11.0+ - Deprecated in 14.0
- tvOS 14.0+ - Deprecated in 17.0
- visionOS
- watchOS 7.0+ - Deprecated in 10.0

> **Deprecated**: Use [`Map`](./map.md) initializers that take a `position` parameter along with  `MapCameraPosition.userLocation` to configure how the camera follows the user.

## Declaration

```swift
enum MapUserTrackingMode
```

## Topics

### Setting the user tracking mode
- [MapUserTrackingMode.none](./mapusertrackingmode/none.md)
  The map doesn’t update based on the person’s location.
- [MapUserTrackingMode.follow](./mapusertrackingmode/follow.md)
  The map updates by following a person’s location.
- [MapUserTrackingMode.followWithHeading](./mapusertrackingmode/followwithheading.md)
  The map updates by following the person’s heading.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapusertrackingmode)*
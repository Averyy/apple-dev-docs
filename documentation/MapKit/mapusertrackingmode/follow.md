# MapUserTrackingMode.follow

**Framework**: MapKit  
**Kind**: case  
**Role**: Case

The map updates by following a person’s location.

**Availability**:
- iOS 14.0+ - Deprecated in 17.0
- iPadOS 14.0+ - Deprecated in 17.0
- Mac Catalyst 14.0+ - Deprecated in 17.0
- macOS 11.0+ - Deprecated in 14.0
- tvOS 14.0+ - Deprecated in 17.0
- visionOS
- watchOS 7.0+ - Deprecated in 10.0

> **Deprecated**: Use Map initializers that take a `position` parameter along with\nMapCameraPosition.userLocation to configure the user location\ntracking behavior.

## Declaration

```swift
case follow
```

## See Also

### Setting the user tracking mode
- [MapUserTrackingMode.none](./none.md)
  The map doesn’t update based on the person’s location.
- [MapUserTrackingMode.followWithHeading](./followwithheading.md)
  The map updates by following the person’s heading.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapusertrackingmode/follow)*
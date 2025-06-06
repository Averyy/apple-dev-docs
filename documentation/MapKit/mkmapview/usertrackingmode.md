# userTrackingMode

**Framework**: MapKit  
**Kind**: property

The mode to use for tracking the user’s location.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var userTrackingMode: MKUserTrackingMode { get set }
```

#### Discussion

Setting the tracking mode to [`MKUserTrackingMode.follow`](mkusertrackingmode/follow.md) or [`MKUserTrackingMode.followWithHeading`](mkusertrackingmode/followwithheading.md) causes the map view to center the map on that location and begin tracking the user’s location. If it’s zoomed out, the map view automatically zooms in on the user’s location, effectively changing the current visible region.

For possible values, see [`MKUserTrackingMode`](mkusertrackingmode.md).

## See Also

- [Converting a user’s location to a descriptive placemark](converting-a-user-s-location-to-a-descriptive-placemark.md)
  Transform the user’s location that displays on a map into an informative textual description by reverse geocoding.
- [var showsUserLocation: Bool](mkmapview/showsuserlocation.md)
  A Boolean value that indicates whether the map tries to display the user’s location.
- [var isUserLocationVisible: Bool](mkmapview/isuserlocationvisible.md)
  A Boolean value that indicates whether the user’s location is visible in the map view.
- [var userLocation: MKUserLocation](mkmapview/userlocation.md)
  The annotation object that represents the user’s location.
- [func setUserTrackingMode(MKUserTrackingMode, animated: Bool)](mkmapview/setusertrackingmode(_:animated:).md)
  Sets the mode to use for tracking the user’s location, with optional animation.
- [enum MKUserTrackingMode](mkusertrackingmode.md)
  The mode to use for tracking the user’s location on the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/usertrackingmode)*
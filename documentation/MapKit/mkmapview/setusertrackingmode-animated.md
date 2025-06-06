# setUserTrackingMode(_:animated:)

**Framework**: MapKit  
**Kind**: method

Sets the mode to use for tracking the user’s location, with optional animation.

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
func setUserTrackingMode(_ mode: MKUserTrackingMode, animated: Bool)
```

#### Discussion

Setting the tracking mode to [`MKUserTrackingMode.follow`](mkusertrackingmode/follow.md) or [`MKUserTrackingMode.followWithHeading`](mkusertrackingmode/followwithheading.md) causes the map view to center the map on that location and begin tracking the user’s location. If it’s zoomed out, the map view automatically zooms in on the user’s location, effectively changing the current visible region.

## Parameters

- `mode`: The mode for tracking the user’s location.   describes the possible values.
- `animated`: If  , the map animates the change from the current mode to the new mode; otherwise, it doesn’t. This parameter affects only tracking-mode changes. Changes to the user’s location or heading use animation.

## See Also

- [func mapView(MKMapView, didChange: MKUserTrackingMode, animated: Bool)](mkmapviewdelegate/mapview(_:didchange:animated:).md)
  Tells the delegate when the user-tracking mode changes.
- [func mapView(MKMapView, didUpdate: MKUserLocation)](mkmapviewdelegate/mapview(_:didupdate:).md)
  Tells the delegate when the map view updates the user’s location.
- [var heading: CLHeading?](mkuserlocation/heading.md)
  The heading of the user’s location.
- [Converting a user’s location to a descriptive placemark](converting-a-user-s-location-to-a-descriptive-placemark.md)
  Transform the user’s location that displays on a map into an informative textual description by reverse geocoding.
- [var showsUserLocation: Bool](mkmapview/showsuserlocation.md)
  A Boolean value that indicates whether the map tries to display the user’s location.
- [var isUserLocationVisible: Bool](mkmapview/isuserlocationvisible.md)
  A Boolean value that indicates whether the user’s location is visible in the map view.
- [var userLocation: MKUserLocation](mkmapview/userlocation.md)
  The annotation object that represents the user’s location.
- [var userTrackingMode: MKUserTrackingMode](mkmapview/usertrackingmode.md)
  The mode to use for tracking the user’s location.
- [enum MKUserTrackingMode](mkusertrackingmode.md)
  The mode to use for tracking the user’s location on the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/setusertrackingmode(_:animated:))*
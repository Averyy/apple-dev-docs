# mapView(_:didUpdate:)

**Framework**: MapKit  
**Kind**: method

Tells the delegate when the map view updates the user’s location.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func mapView(_ mapView: MKMapView, didUpdate userLocation: MKUserLocation)
```

## Mentions

- [Converting a user’s location to a descriptive placemark](converting-a-user-s-location-to-a-descriptive-placemark.md)

#### Discussion

While the [`showsUserLocation`](mkmapview/showsuserlocation.md) property is [`true`](https://developer.apple.com/documentation/Swift/true), the map view calls this method whenever it receives a new location update. It also calls this method if the map view’s user-tracking mode is [`MKUserTrackingMode.followWithHeading`](mkusertrackingmode/followwithheading.md) and the heading changes.

The.map view doesn’t call this method if the app is running in the background. If you want to receive location updates while running in the background, use the Core Location framework.

## Parameters

- `mapView`: The map view that’s tracking the user’s location.
- `userLocation`: The location object representing the user’s latest location. This property may be  .

## See Also

- [func mapViewWillStartLocatingUser(MKMapView)](mkmapviewdelegate/mapviewwillstartlocatinguser(_:).md)
  Tells the delegate that the map view is about to start tracking the user’s location.
- [func mapViewDidStopLocatingUser(MKMapView)](mkmapviewdelegate/mapviewdidstoplocatinguser(_:).md)
  Tells the delegate when the map view stops tracking the user’s location.
- [func mapView(MKMapView, didFailToLocateUserWithError: any Error)](mkmapviewdelegate/mapview(_:didfailtolocateuserwitherror:).md)
  Tells the delegate when an attempt to locate the user’s location fails.
- [func mapView(MKMapView, didChange: MKUserTrackingMode, animated: Bool)](mkmapviewdelegate/mapview(_:didchange:animated:).md)
  Tells the delegate when the user-tracking mode changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/mapview(_:didupdate:))*
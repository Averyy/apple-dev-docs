# mapView(_:didFailToLocateUserWithError:)

**Framework**: MapKit  
**Kind**: method

Tells the delegate when an attempt to locate the user’s location fails.

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
optional func mapView(_ mapView: MKMapView, didFailToLocateUserWithError error: any Error)
```

## Parameters

- `mapView`: The map view that’s tracking the user’s location.
- `error`: An error object containing the reason why location tracking fails.

## See Also

- [func mapViewWillStartLocatingUser(MKMapView)](mkmapviewdelegate/mapviewwillstartlocatinguser(_:).md)
  Tells the delegate that the map view is about to start tracking the user’s location.
- [func mapViewDidStopLocatingUser(MKMapView)](mkmapviewdelegate/mapviewdidstoplocatinguser(_:).md)
  Tells the delegate when the map view stops tracking the user’s location.
- [func mapView(MKMapView, didUpdate: MKUserLocation)](mkmapviewdelegate/mapview(_:didupdate:).md)
  Tells the delegate when the map view updates the user’s location.
- [func mapView(MKMapView, didChange: MKUserTrackingMode, animated: Bool)](mkmapviewdelegate/mapview(_:didchange:animated:).md)
  Tells the delegate when the user-tracking mode changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/mapview(_:didfailtolocateuserwitherror:))*
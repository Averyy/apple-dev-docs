# mapViewWillStartLocatingUser(_:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the map view is about to start tracking the user’s location.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
optional func mapViewWillStartLocatingUser(_ mapView: MKMapView)
```

```objc
- (void) mapViewWillStartLocatingUser:(MKMapView *) mapView;
```

#### Discussion

The map view calls this method when the value of the [`showsUserLocation`](../mkmapview/showsuserlocation.md) property changes to [`true`](../../Swift/true.md).

## Parameters

- `mapView`: The map view that’s tracking the user’s location.

## See Also

### Tracking the user’s location
- [func mapViewDidStopLocatingUser(MKMapView)](./mapviewdidstoplocatinguser%28_%29.md)
  Tells the delegate when the map view stops tracking the user’s location.
- [func mapView(MKMapView, didUpdate: MKUserLocation)](./mapview%28_,didupdate%29.md)
  Tells the delegate when the map view updates the user’s location.
- [func mapView(MKMapView, didFailToLocateUserWithError: any Error)](./mapview%28_,didfailtolocateuserwitherror%29.md)
  Tells the delegate when an attempt to locate the user’s location fails.
- [func mapView(MKMapView, didChange: MKUserTrackingMode, animated: Bool)](./mapview%28_,didchange,animated%29.md)
  Tells the delegate when the user-tracking mode changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/mapviewwillstartlocatinguser(_:))*
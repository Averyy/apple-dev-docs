# mapViewDidFinishLoadingMap(_:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate when the specified map view successfully loads the needed map data.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
optional func mapViewDidFinishLoadingMap(_ mapView: MKMapView)
```

```objc
- (void) mapViewDidFinishLoadingMap:(MKMapView *) mapView;
```

#### Discussion

The map view calls this method when it finishes reloading the map tiles associated with the current request. The map view requests map tiles when a new visible area scrolls into view and tiles aren’t already available. The map may also request map tiles for portions of the map that aren’t currently visible. For example, the map view may load tiles immediately surrounding the currently visible area as needed to handle small pans by the user.

## Parameters

- `mapView`: The map view that starts the load operation.

## See Also

### Loading the map data
- [func mapViewWillStartLoadingMap(MKMapView)](./mapviewwillstartloadingmap%28_%29.md)
  Tells the delegate that the specified map view is about to retrieve some map data.
- [func mapViewDidFailLoadingMap(MKMapView, withError: any Error)](./mapviewdidfailloadingmap%28_,witherror%29.md)
  Tells the delegate that the specified view is unable to load the map data.
- [func mapViewWillStartRenderingMap(MKMapView)](./mapviewwillstartrenderingmap%28_%29.md)
  Tells the delegate that the map view is about to start rendering some of its tiles.
- [func mapViewDidFinishRenderingMap(MKMapView, fullyRendered: Bool)](./mapviewdidfinishrenderingmap%28_,fullyrendered%29.md)
  Tells the delegate when the map view finishes rendering all visible tiles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/mapviewdidfinishloadingmap(_:))*
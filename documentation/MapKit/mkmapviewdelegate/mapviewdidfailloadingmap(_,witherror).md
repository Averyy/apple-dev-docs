# mapViewDidFailLoadingMap(_:withError:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the specified view is unable to load the map data.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
optional func mapViewDidFailLoadingMap(_ mapView: MKMapView, withError error: any Error)
```

```objc
- (void) mapViewDidFailLoadingMap:(MKMapView *) mapView withError:(NSError *) error;
```

## Discussion

The map view might call this method in situations where the device doesn’t have access to the network or is unable to load the map data for some reason. The map view may also call this method if a request for additional map tiles comes in while a previous request for tiles is pending. You can use this message to notify the user that the map data is unavailable.

## Parameters

- `mapView`: The map view that starts the load operation.
- `error`: The reason that the map view can’t load the map data.

## See Also

### Loading the map data
- [func mapViewWillStartLoadingMap(MKMapView)](./mapviewwillstartloadingmap%28_%29.md)
  Tells the delegate that the specified map view is about to retrieve some map data.
- [func mapViewDidFinishLoadingMap(MKMapView)](./mapviewdidfinishloadingmap%28_%29.md)
  Tells the delegate when the specified map view successfully loads the needed map data.
- [func mapViewWillStartRenderingMap(MKMapView)](./mapviewwillstartrenderingmap%28_%29.md)
  Tells the delegate that the map view is about to start rendering some of its tiles.
- [func mapViewDidFinishRenderingMap(MKMapView, fullyRendered: Bool)](./mapviewdidfinishrenderingmap%28_,fullyrendered%29.md)
  Tells the delegate when the map view finishes rendering all visible tiles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/mapviewdidfailloadingmap(_:witherror:))*
# mapViewWillStartLoadingMap(_:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the specified map view is about to retrieve some map data.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
optional func mapViewWillStartLoadingMap(_ mapView: MKMapView)
```

```objc
- (void) mapViewWillStartLoadingMap:(MKMapView *) mapView;
```

#### Discussion

The map view calls this method whenever it needs to download a new group of map tiles from the server. This typically occurs whenever you expose portions of the map by panning or zooming the content. You can use this method to mark the time that it takes for the map view to load the data.

## Parameters

- `mapView`: The map view that begins loading the data.

## See Also

### Loading the map data
- [func mapViewDidFinishLoadingMap(MKMapView)](./mapviewdidfinishloadingmap%28_%29.md)
  Tells the delegate when the specified map view successfully loads the needed map data.
- [func mapViewDidFailLoadingMap(MKMapView, withError: any Error)](./mapviewdidfailloadingmap%28_,witherror%29.md)
  Tells the delegate that the specified view is unable to load the map data.
- [func mapViewWillStartRenderingMap(MKMapView)](./mapviewwillstartrenderingmap%28_%29.md)
  Tells the delegate that the map view is about to start rendering some of its tiles.
- [func mapViewDidFinishRenderingMap(MKMapView, fullyRendered: Bool)](./mapviewdidfinishrenderingmap%28_,fullyrendered%29.md)
  Tells the delegate when the map view finishes rendering all visible tiles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/mapviewwillstartloadingmap(_:))*
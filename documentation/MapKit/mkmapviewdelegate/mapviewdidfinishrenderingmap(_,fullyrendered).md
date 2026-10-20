# mapViewDidFinishRenderingMap(_:fullyRendered:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate when the map view finishes rendering all visible tiles.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
optional func mapViewDidFinishRenderingMap(_ mapView: MKMapView, fullyRendered: Bool)
```

```objc
- (void) mapViewDidFinishRenderingMap:(MKMapView *) mapView fullyRendered:(BOOL) fullyRendered;
```

#### Discussion

This method lets you know when the map view finishes rendering all of the currently visible tiles to the best of its ability. The map view calls this method regardless of whether the view renders all tiles successfully. If there are errors loading one or more tiles that prevent the map view from rendering them, MapKit sets the `fullyRendered` parameter to [`false`](../../Swift/false.md).

## Parameters

- `mapView`: The map view rendering its tiles.
- `fullyRendered`: This parameter is [`true`](../../Swift/true.md) if the map view is able to render all tiles completely, or [`false`](../../Swift/false.md) if errors prevent the map view from rendering all tiles.

## See Also

### Loading the map data
- [func mapViewWillStartLoadingMap(MKMapView)](./mapviewwillstartloadingmap%28_%29.md)
  Tells the delegate that the specified map view is about to retrieve some map data.
- [func mapViewDidFinishLoadingMap(MKMapView)](./mapviewdidfinishloadingmap%28_%29.md)
  Tells the delegate when the specified map view successfully loads the needed map data.
- [func mapViewDidFailLoadingMap(MKMapView, withError: any Error)](./mapviewdidfailloadingmap%28_,witherror%29.md)
  Tells the delegate that the specified view is unable to load the map data.
- [func mapViewWillStartRenderingMap(MKMapView)](./mapviewwillstartrenderingmap%28_%29.md)
  Tells the delegate that the map view is about to start rendering some of its tiles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/mapviewdidfinishrenderingmap(_:fullyrendered:))*
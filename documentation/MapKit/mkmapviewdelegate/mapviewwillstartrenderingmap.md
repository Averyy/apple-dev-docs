# mapViewWillStartRenderingMap(_:)

**Framework**: MapKit  
**Kind**: method

Tells the delegate that the map view is about to start rendering some of its tiles.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func mapViewWillStartRenderingMap(_ mapView: MKMapView)
```

#### Discussion

The map view calls this method when the map reveals one or more tiles that require rendering.

## Parameters

- `mapView`: The map view that’s about to start rendering.

## See Also

- [func mapViewWillStartLoadingMap(MKMapView)](mkmapviewdelegate/mapviewwillstartloadingmap(_:).md)
  Tells the delegate that the specified map view is about to retrieve some map data.
- [func mapViewDidFinishLoadingMap(MKMapView)](mkmapviewdelegate/mapviewdidfinishloadingmap(_:).md)
  Tells the delegate when the specified map view successfully loads the needed map data.
- [func mapViewDidFailLoadingMap(MKMapView, withError: any Error)](mkmapviewdelegate/mapviewdidfailloadingmap(_:witherror:).md)
  Tells the delegate that the specified view is unable to load the map data.
- [func mapViewDidFinishRenderingMap(MKMapView, fullyRendered: Bool)](mkmapviewdelegate/mapviewdidfinishrenderingmap(_:fullyrendered:).md)
  Tells the delegate when the map view finishes rendering all visible tiles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/mapviewwillstartrenderingmap(_:))*
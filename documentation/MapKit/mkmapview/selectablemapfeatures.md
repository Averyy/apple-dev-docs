# selectableMapFeatures

**Framework**: MapKit  
**Kind**: property

The property that describes which selectable features the map responds to.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var selectableMapFeatures: MKMapFeatureOptions { get set }
```

## See Also

- [func mapView(MKMapView, didSelect: MKAnnotationView)](mkmapviewdelegate/mapview(_:didselect:)-41by3.md)
  Tells the delegate when the user selects one or more of its annotation views.
- [func mapView(MKMapView, didDeselect: MKAnnotationView)](mkmapviewdelegate/mapview(_:diddeselect:)-yo7q.md)
  Tells the delegate when the user deselects one or more of its annotation views.
- [func mapView(MKMapView, didDeselect: any MKAnnotation)](mkmapviewdelegate/mapview(_:diddeselect:)-4ldss.md)
  Tells the delegate when the user deselects one or more annotations.
- [func mapView(MKMapView, didSelect: any MKAnnotation)](mkmapviewdelegate/mapview(_:didselect:)-9km43.md)
  Tells the delegate when the user selects one or more annotations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/selectablemapfeatures)*
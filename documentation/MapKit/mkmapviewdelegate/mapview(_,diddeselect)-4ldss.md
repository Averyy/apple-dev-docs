# mapView(_:didDeselect:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate when the user deselects one or more annotations.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
optional func mapView(_ mapView: MKMapView, didDeselect annotation: any MKAnnotation)
```

```objc
- (void) mapView:(MKMapView *) mapView didDeselectAnnotation:(id<MKAnnotation>) annotation;
```

## Parameters

- `mapView`: The map view containing the annotation view.
- `annotation`: The deselected annotation view.

## See Also

### Selecting annotations and annotations views
- [func mapView(MKMapView, didSelect: MKAnnotationView)](./mapview%28_,didselect%29-41by3.md)
  Tells the delegate when the user selects one or more of its annotation views.
- [func mapView(MKMapView, didDeselect: MKAnnotationView)](./mapview%28_,diddeselect%29-yo7q.md)
  Tells the delegate when the user deselects one or more of its annotation views.
- [func mapView(MKMapView, didSelect: any MKAnnotation)](./mapview%28_,didselect%29-9km43.md)
  Tells the delegate when the user selects one or more annotations.
- [var selectableMapFeatures: MKMapFeatureOptions](../mkmapview/selectablemapfeatures.md)
  The property that describes which selectable features the map responds to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/mapview(_:diddeselect:)-4ldss)*
# mapView(_:didSelect:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate when the user selects one or more of its annotation views.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
optional func mapView(_ mapView: MKMapView, didSelect view: MKAnnotationView)
```

```objc
- (void) mapView:(MKMapView *) mapView didSelectAnnotationView:(MKAnnotationView *) view;
```

## Discussion

You can use this method to track changes in the selection state of annotation views.

## Parameters

- `mapView`: The map view containing the annotation view.
- `view`: The selected annotation view.

## See Also

### Selecting annotations and annotations views
- [func mapView(MKMapView, didDeselect: MKAnnotationView)](./mapview%28_,diddeselect%29-yo7q.md)
  Tells the delegate when the user deselects one or more of its annotation views.
- [func mapView(MKMapView, didDeselect: any MKAnnotation)](./mapview%28_,diddeselect%29-4ldss.md)
  Tells the delegate when the user deselects one or more annotations.
- [func mapView(MKMapView, didSelect: any MKAnnotation)](./mapview%28_,didselect%29-9km43.md)
  Tells the delegate when the user selects one or more annotations.
- [var selectableMapFeatures: MKMapFeatureOptions](../mkmapview/selectablemapfeatures.md)
  The property that describes which selectable features the map responds to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/mapview(_:didselect:)-41by3)*
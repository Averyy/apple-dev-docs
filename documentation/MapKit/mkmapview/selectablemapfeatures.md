# selectableMapFeatures

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The property that describes which selectable features the map responds to.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
var selectableMapFeatures: MKMapFeatureOptions { get set }
```

```objc
@property (nonatomic) MKMapFeatureOptions selectableMapFeatures;
```

## See Also

### Selecting annotations and annotations views
- [func mapView(MKMapView, didSelect: MKAnnotationView)](../mkmapviewdelegate/mapview%28_,didselect%29-41by3.md)
  Tells the delegate when the user selects one or more of its annotation views.
- [func mapView(MKMapView, didDeselect: MKAnnotationView)](../mkmapviewdelegate/mapview%28_,diddeselect%29-yo7q.md)
  Tells the delegate when the user deselects one or more of its annotation views.
- [func mapView(MKMapView, didDeselect: any MKAnnotation)](../mkmapviewdelegate/mapview%28_,diddeselect%29-4ldss.md)
  Tells the delegate when the user deselects one or more annotations.
- [func mapView(MKMapView, didSelect: any MKAnnotation)](../mkmapviewdelegate/mapview%28_,didselect%29-9km43.md)
  Tells the delegate when the user selects one or more annotations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/selectablemapfeatures)*
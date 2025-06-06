# mapView(_:didAdd:)

**Framework**: MapKit  
**Kind**: method

Tells the delegate when the map view adds one or more annotation views to the map.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func mapView(_ mapView: MKMapView, didAdd views: [MKAnnotationView])
```

#### Discussion

By the time the map view calls this method, MapKit has added the specified views to the map.

## Parameters

- `mapView`: The map view that adds the annotation views.
- `views`: An array of   objects representing the views that the map view adds.

## See Also

- [func mapView(MKMapView, viewFor: any MKAnnotation) -> MKAnnotationView?](mkmapviewdelegate/mapview(_:viewfor:)-8humz.md)
  Returns the view associated with the specified annotation object.
- [func mapView(MKMapView, annotationView: MKAnnotationView, calloutAccessoryControlTapped: UIControl)](mkmapviewdelegate/mapview(_:annotationview:calloutaccessorycontroltapped:).md)
  Tells the delegate when the user taps one of the annotation view’s accessory buttons.
- [func mapView(MKMapView, clusterAnnotationForMemberAnnotations: [any MKAnnotation]) -> MKClusterAnnotation](mkmapviewdelegate/mapview(_:clusterannotationformemberannotations:).md)
  Asks the delegate to provide a cluster annotation object for the specified annotations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/mapview(_:didadd:)-44xon)*
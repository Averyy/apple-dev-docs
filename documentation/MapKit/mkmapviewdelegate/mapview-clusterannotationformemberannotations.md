# mapView(_:clusterAnnotationForMemberAnnotations:)

**Framework**: MapKit  
**Kind**: method

Asks the delegate to provide a cluster annotation object for the specified annotations.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func mapView(_ mapView: MKMapView, clusterAnnotationForMemberAnnotations memberAnnotations: [any MKAnnotation]) -> MKClusterAnnotation
```

#### Return Value

The cluster annotation object.

#### Discussion

Use this method to customize the cluster annotations that display on your map. Typically, MapKit creates cluster annotation objects automatically when one or more annotations with the same cluster identifier are too close together. However, you can implement this method and return a custom cluster annotation object for the specified set of annotations.

## Parameters

- `mapView`: The map view containing the specified annotations.
- `memberAnnotations`: The annotations for the map to cluster together. The returned   object needs to include the specific annotations in this parameter.

## See Also

- [func mapView(MKMapView, viewFor: any MKAnnotation) -> MKAnnotationView?](mkmapviewdelegate/mapview(_:viewfor:)-8humz.md)
  Returns the view associated with the specified annotation object.
- [func mapView(MKMapView, didAdd: [MKAnnotationView])](mkmapviewdelegate/mapview(_:didadd:)-44xon.md)
  Tells the delegate when the map view adds one or more annotation views to the map.
- [func mapView(MKMapView, annotationView: MKAnnotationView, calloutAccessoryControlTapped: UIControl)](mkmapviewdelegate/mapview(_:annotationview:calloutaccessorycontroltapped:).md)
  Tells the delegate when the user taps one of the annotation view’s accessory buttons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/mapview(_:clusterannotationformemberannotations:))*
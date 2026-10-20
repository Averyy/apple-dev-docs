# mapView(_:didAdd:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

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
optional func mapView(_ mapView: MKMapView, didAdd views: [MKAnnotationView])
```

```objc
- (void) mapView:(MKMapView *) mapView didAddAnnotationViews:(NSArray<MKAnnotationView *> *) views;
```

#### Discussion

By the time the map view calls this method, MapKit has added the specified views to the map.

## Parameters

- `mapView`: The map view that adds the annotation views.
- `views`: An array of `MKAnnotationView` objects representing the views that the map view adds.

## See Also

### Managing annotation views
- [func mapView(MKMapView, viewFor: any MKAnnotation) -> MKAnnotationView?](./mapview%28_,viewfor%29-8humz.md)
  Returns the view associated with the specified annotation object.
- [func mapView(MKMapView, annotationView: MKAnnotationView, calloutAccessoryControlTapped: UIControl)](./mapview%28_,annotationview,calloutaccessorycontroltapped%29.md)
  Tells the delegate when the user taps one of the annotation view’s accessory buttons.
- [func mapView(MKMapView, clusterAnnotationForMemberAnnotations: [any MKAnnotation]) -> MKClusterAnnotation](./mapview%28_,clusterannotationformemberannotations%29.md)
  Asks the delegate to provide a cluster annotation object for the specified annotations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/mapview(_:didadd:)-44xon)*
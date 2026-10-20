# mapView(_:viewFor:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Returns the view associated with the specified annotation object.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
optional func mapView(_ mapView: MKMapView, viewFor annotation: any MKAnnotation) -> MKAnnotationView?
```

```objc
- (MKAnnotationView *) mapView:(MKMapView *) mapView viewForAnnotation:(id<MKAnnotation>) annotation;
```

#### Return Value

The annotation view to display for the specified annotation, or `nil` if you want to display a standard annotation view.

#### Discussion

Rather than create a new view each time the map view calls this method, call the [`dequeueReusableAnnotationView(withIdentifier:)`](../mkmapview/dequeuereusableannotationview%28withidentifier%29.md) method of the [`MKMapView`](../mkmapview.md) class to see if an existing annotation view of the desired type already exists. If one exists, update the returned view to reflect the attributes of the specified annotation and return it. If a view of the appropriate type doesn’t exist, create one, configure it with the needed annotation data, and return it.

If the object in the `annotation` parameter is an instance of the [`MKUserLocation`](../mkuserlocation.md) class, you can provide a custom view to denote the user’s location. To display the user’s location using the default system view, return `nil`.

If you don’t implement this method, or if you return `nil` from your implementation for annotations other than the user location annotation, the map view uses a standard pin annotation view.

## Parameters

- `mapView`: The map view that requests the annotation view.
- `annotation`: The object representing the annotation that the map view is about to display. In addition to your custom annotations, this object might be an [`MKUserLocation`](../mkuserlocation.md) object representing the user’s location.

## See Also

### Managing annotation views
- [func mapView(MKMapView, didAdd: [MKAnnotationView])](./mapview%28_,didadd%29-44xon.md)
  Tells the delegate when the map view adds one or more annotation views to the map.
- [func mapView(MKMapView, annotationView: MKAnnotationView, calloutAccessoryControlTapped: UIControl)](./mapview%28_,annotationview,calloutaccessorycontroltapped%29.md)
  Tells the delegate when the user taps one of the annotation view’s accessory buttons.
- [func mapView(MKMapView, clusterAnnotationForMemberAnnotations: [any MKAnnotation]) -> MKClusterAnnotation](./mapview%28_,clusterannotationformemberannotations%29.md)
  Asks the delegate to provide a cluster annotation object for the specified annotations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/mapview(_:viewfor:)-8humz)*
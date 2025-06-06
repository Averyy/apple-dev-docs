# MKMapViewDefaultClusterAnnotationViewReuseIdentifier

**Framework**: MapKit  
**Kind**: var

The default reuse identifier for the annotation view representing a cluster of annotations.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
let MKMapViewDefaultClusterAnnotationViewReuseIdentifier: String
```

#### Discussion

Use this constant to register a default annotation view to use for clusters of annotations. The map view uses this cluster annotation view when your map view’s delegate doesn’t implement the [`mapView(_:viewFor:)`](mkmapviewdelegate/mapview(_:viewfor:)-8humz.md) method, or when that method returns `nil`.

## See Also

- [func register(AnyClass?, forAnnotationViewWithReuseIdentifier: String)](mkmapview/register(_:forannotationviewwithreuseidentifier:).md)
  Registers an annotation view class that the map can create automatically.
- [func dequeueReusableAnnotationView(withIdentifier: String, for: any MKAnnotation) -> MKAnnotationView](mkmapview/dequeuereusableannotationview(withidentifier:for:).md)
  Returns a reusable annotation view using the specified identifier with a specified existing annotation view, if possible.
- [func dequeueReusableAnnotationView(withIdentifier: String) -> MKAnnotationView?](mkmapview/dequeuereusableannotationview(withidentifier:).md)
  Returns a reusable annotation view using its identifier.
- [func view(for: any MKAnnotation) -> MKAnnotationView?](mkmapview/view(for:)-33w8k.md)
  Returns the annotation view associated with the specified annotation object, if any.
- [let MKMapViewDefaultAnnotationViewReuseIdentifier: String](mkmapviewdefaultannotationviewreuseidentifier.md)
  The default reuse identifier for your map’s annotation views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapviewdefaultclusterannotationviewreuseidentifier)*
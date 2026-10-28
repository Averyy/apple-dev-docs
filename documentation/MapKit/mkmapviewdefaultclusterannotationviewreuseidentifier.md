# MKMapViewDefaultClusterAnnotationViewReuseIdentifier

**Framework**: MapKit  
**Kind**: var  
**Role**: Global Variable

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

```c
extern NSString * const MKMapViewDefaultClusterAnnotationViewReuseIdentifier;
```

## Discussion

Use this constant to register a default annotation view to use for clusters of annotations. The map view uses this cluster annotation view when your map view’s delegate doesn’t implement the [`mapView(_:viewFor:)`](./mkmapviewdelegate/mapview%28_,viewfor%29-8humz.md) method, or when that method returns `nil`.

## See Also

### Creating annotation views
- [func register(AnyClass?, forAnnotationViewWithReuseIdentifier: String)](./mkmapview/register%28_,forannotationviewwithreuseidentifier%29.md)
  Registers an annotation view class that the map can create automatically.
- [func dequeueReusableAnnotationView(withIdentifier: String, for: any MKAnnotation) -> MKAnnotationView](./mkmapview/dequeuereusableannotationview%28withidentifier,for%29.md)
  Returns a reusable annotation view using the specified identifier with a specified existing annotation view, if possible.
- [func dequeueReusableAnnotationView(withIdentifier: String) -> MKAnnotationView?](./mkmapview/dequeuereusableannotationview%28withidentifier%29.md)
  Returns a reusable annotation view using its identifier.
- [func view(for: any MKAnnotation) -> MKAnnotationView?](./mkmapview/view%28for%29-33w8k.md)
  Returns the annotation view associated with the specified annotation object, if any.
- [let MKMapViewDefaultAnnotationViewReuseIdentifier: String](./mkmapviewdefaultannotationviewreuseidentifier.md)
  The default reuse identifier for your map’s annotation views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapviewdefaultclusterannotationviewreuseidentifier)*
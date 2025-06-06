# register(_:forAnnotationViewWithReuseIdentifier:)

**Framework**: MapKit  
**Kind**: method

Registers an annotation view class that the map can create automatically.

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
func register(_ viewClass: AnyClass?, forAnnotationViewWithReuseIdentifier identifier: String)
```

#### Discussion

Use this method to register one or more views that you use to display annotations on your map. Register your classes before adding any annotations to the map.

When you register an annotation view class using this method, the [`dequeueReusableAnnotationView(withIdentifier:for:)`](mkmapview/dequeuereusableannotationview(withidentifier:for:).md) method uses the provided identifier to create the view that you register. It creates a new view only if an existing view isn’t available for reuse.

## Parameters

- `viewClass`: The class of an annotation view that you use in your map. The class needs to be a subclass of  .
- `identifier`: The reuse identifier to associate with the specified class. This parameter can’t be   or an empty string.

## See Also

- [func dequeueReusableAnnotationView(withIdentifier: String, for: any MKAnnotation) -> MKAnnotationView](mkmapview/dequeuereusableannotationview(withidentifier:for:).md)
  Returns a reusable annotation view using the specified identifier with a specified existing annotation view, if possible.
- [func dequeueReusableAnnotationView(withIdentifier: String) -> MKAnnotationView?](mkmapview/dequeuereusableannotationview(withidentifier:).md)
  Returns a reusable annotation view using its identifier.
- [func view(for: any MKAnnotation) -> MKAnnotationView?](mkmapview/view(for:)-33w8k.md)
  Returns the annotation view associated with the specified annotation object, if any.
- [let MKMapViewDefaultAnnotationViewReuseIdentifier: String](mkmapviewdefaultannotationviewreuseidentifier.md)
  The default reuse identifier for your map’s annotation views.
- [let MKMapViewDefaultClusterAnnotationViewReuseIdentifier: String](mkmapviewdefaultclusterannotationviewreuseidentifier.md)
  The default reuse identifier for the annotation view representing a cluster of annotations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/register(_:forannotationviewwithreuseidentifier:))*
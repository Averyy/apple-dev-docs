# dequeueReusableAnnotationView(withIdentifier:)

**Framework**: MapKit  
**Kind**: method

Returns a reusable annotation view using its identifier.

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
func dequeueReusableAnnotationView(withIdentifier identifier: String) -> MKAnnotationView?
```

#### Return Value

An annotation view with the specified identifier, or `nil` if no such object exists in the reuse queue.

#### Discussion

For performance reasons, it’s best practice to reuse [`MKAnnotationView`](mkannotationview.md) objects in your map views. As annotation views move offscreen, the map view moves them to an internally managed reuse queue. As new annotations move onscreen, and the map view prompts your code to provide a corresponding annotation view, attempt to dequeue an existing view before creating a new one. Dequeueing saves time and memory during performance-critical operations like scrolling.

## Parameters

- `identifier`: A string identifying the annotation view for the map view to reuse. This string is the same one you specify when initializing the annotation view using the   method.

## See Also

- [func register(AnyClass?, forAnnotationViewWithReuseIdentifier: String)](mkmapview/register(_:forannotationviewwithreuseidentifier:).md)
  Registers an annotation view class that the map can create automatically.
- [func dequeueReusableAnnotationView(withIdentifier: String, for: any MKAnnotation) -> MKAnnotationView](mkmapview/dequeuereusableannotationview(withidentifier:for:).md)
  Returns a reusable annotation view using the specified identifier with a specified existing annotation view, if possible.
- [func view(for: any MKAnnotation) -> MKAnnotationView?](mkmapview/view(for:)-33w8k.md)
  Returns the annotation view associated with the specified annotation object, if any.
- [let MKMapViewDefaultAnnotationViewReuseIdentifier: String](mkmapviewdefaultannotationviewreuseidentifier.md)
  The default reuse identifier for your map’s annotation views.
- [let MKMapViewDefaultClusterAnnotationViewReuseIdentifier: String](mkmapviewdefaultclusterannotationviewreuseidentifier.md)
  The default reuse identifier for the annotation view representing a cluster of annotations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/dequeuereusableannotationview(withidentifier:))*
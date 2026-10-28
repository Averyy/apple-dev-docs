# dequeueReusableAnnotationView(withIdentifier:for:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Returns a reusable annotation view using the specified identifier with a specified existing annotation view, if possible.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func dequeueReusableAnnotationView(withIdentifier identifier: String, for annotation: any MKAnnotation) -> MKAnnotationView
```

```objc
- (MKAnnotationView *) dequeueReusableAnnotationViewWithIdentifier:(NSString *) identifier forAnnotation:(id<MKAnnotation>) annotation;
```

## Return Value

An annotation view with the specified identifier.

## Discussion

For performance reasons, be sure to reuse [`MKAnnotationView`](../mkannotationview.md) objects in your map views. As annotation views move offscreen, the map view moves them to an internally managed reuse queue. As new annotations move onscreen, and the map view prompts your code to provide a corresponding annotation view, use this method to dequeue an existing view. Dequeueing saves time and memory during performance-critical operations, such as scrolling.

If the map view can dequeue an existing view, this method tries to create one from the specified identifier. Before this can happen, you need to register an annotation view class using the [`register(_:forAnnotationViewWithReuseIdentifier:)`](./register%28_,forannotationviewwithreuseidentifier%29.md) method. If there’s no registered class with the appropriate identifier, this method throws an exception.

## Parameters

- `identifier`: A string identifying the annotation view to create.
- `annotation`: The annotation the map is displaying. This method automatically assigns this annotation object to the returned annotation view.

## See Also

### Creating annotation views
- [func register(AnyClass?, forAnnotationViewWithReuseIdentifier: String)](./register%28_,forannotationviewwithreuseidentifier%29.md)
  Registers an annotation view class that the map can create automatically.
- [func dequeueReusableAnnotationView(withIdentifier: String) -> MKAnnotationView?](./dequeuereusableannotationview%28withidentifier%29.md)
  Returns a reusable annotation view using its identifier.
- [func view(for: any MKAnnotation) -> MKAnnotationView?](./view%28for%29-33w8k.md)
  Returns the annotation view associated with the specified annotation object, if any.
- [let MKMapViewDefaultAnnotationViewReuseIdentifier: String](../mkmapviewdefaultannotationviewreuseidentifier.md)
  The default reuse identifier for your map’s annotation views.
- [let MKMapViewDefaultClusterAnnotationViewReuseIdentifier: String](../mkmapviewdefaultclusterannotationviewreuseidentifier.md)
  The default reuse identifier for the annotation view representing a cluster of annotations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/dequeuereusableannotationview(withidentifier:for:))*
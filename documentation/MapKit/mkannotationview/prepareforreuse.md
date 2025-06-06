# prepareForReuse()

**Framework**: MapKit  
**Kind**: method

Calls this method when removing the view from the reuse queue.

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
func prepareForReuse()
```

#### Discussion

The default implementation of this method does nothing. You can override it in your custom annotation views and use it to put the view in a known state before the map view returns it to your map view delegate.

## See Also

- [func dequeueReusableAnnotationView(withIdentifier: String) -> MKAnnotationView?](mkmapview/dequeuereusableannotationview(withidentifier:).md)
  Returns a reusable annotation view using its identifier.
- [init(annotation: (any MKAnnotation)?, reuseIdentifier: String?)](mkannotationview/init(annotation:reuseidentifier:).md)
  Creates and returns a new annotation view.
- [init?(coder: NSCoder)](mkannotationview/init(coder:).md)
  Creates an annotation view using data from the specified unarchiver.
- [func prepareForDisplay()](mkannotationview/preparefordisplay.md)
  Notifies the annotation view that the map view is about to display it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkannotationview/prepareforreuse())*
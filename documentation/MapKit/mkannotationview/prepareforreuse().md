# prepareForReuse()

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

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
func prepareForReuse()
```

```objc
- (void) prepareForReuse;
```

#### Discussion

The default implementation of this method does nothing. You can override it in your custom annotation views and use it to put the view in a known state before the map view returns it to your map view delegate.

## See Also

### Related Documentation
- [func dequeueReusableAnnotationView(withIdentifier: String) -> MKAnnotationView?](../mkmapview/dequeuereusableannotationview%28withidentifier%29.md)
  Returns a reusable annotation view using its identifier.
### Creating and preparing an annotation view
- [init(annotation: (any MKAnnotation)?, reuseIdentifier: String?)](./init%28annotation,reuseidentifier%29.md)
  Creates and returns a new annotation view.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates an annotation view using data from the specified unarchiver.
- [func prepareForDisplay()](./preparefordisplay%28%29.md)
  Notifies the annotation view that the map view is about to display it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkannotationview/prepareforreuse())*
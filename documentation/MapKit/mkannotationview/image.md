# image

**Framework**: MapKit  
**Kind**: property

The image the annotation view displays.

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
var image: UIImage? { get set }
```

#### Discussion

Assigning a new image to this property also changes the size of the view’s frame so that it matches the width and height of the new image. The position of the view’s frame doesn’t change.

## See Also

- [var isEnabled: Bool](mkannotationview/isenabled.md)
  A Boolean value that indicates whether the annotation is in an enabled state.
- [var isHighlighted: Bool](mkannotationview/ishighlighted.md)
  A Boolean value that indicates whether the map view highlights the annotation view.
- [var annotation: (any MKAnnotation)?](mkannotationview/annotation.md)
  The annotation object associated with the view.
- [var centerOffset: CGPoint](mkannotationview/centeroffset.md)
  The offset (in points) at which to display the view.
- [var calloutOffset: CGPoint](mkannotationview/calloutoffset.md)
  The offset (in points) at which to place the callout.
- [var reuseIdentifier: String?](mkannotationview/reuseidentifier.md)
  The string that identifies that the annotation view is reusable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkannotationview/image)*
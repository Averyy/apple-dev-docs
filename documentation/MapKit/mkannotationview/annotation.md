# annotation

**Framework**: MapKit  
**Kind**: property

The annotation object associated with the view.

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
var annotation: (any MKAnnotation)? { get set }
```

#### Discussion

Don’t change the value of this property directly. This property contains a non-`nil` value only while the annotation view is visible on the map. If the map view queues this annotation view and is waiting to reuse it, the value is `nil`.

## See Also

- [var isEnabled: Bool](mkannotationview/isenabled.md)
  A Boolean value that indicates whether the annotation is in an enabled state.
- [var image: UIImage?](mkannotationview/image.md)
  The image the annotation view displays.
- [var isHighlighted: Bool](mkannotationview/ishighlighted.md)
  A Boolean value that indicates whether the map view highlights the annotation view.
- [var centerOffset: CGPoint](mkannotationview/centeroffset.md)
  The offset (in points) at which to display the view.
- [var calloutOffset: CGPoint](mkannotationview/calloutoffset.md)
  The offset (in points) at which to place the callout.
- [var reuseIdentifier: String?](mkannotationview/reuseidentifier.md)
  The string that identifies that the annotation view is reusable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkannotationview/annotation)*
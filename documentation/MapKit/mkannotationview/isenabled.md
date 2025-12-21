# isEnabled

**Framework**: MapKit  
**Kind**: property

A Boolean value that indicates whether the annotation is in an enabled state.

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
var isEnabled: Bool { get set }
```

#### Discussion

The default value of this property is [`true`](https://developer.apple.com/documentation/Swift/true). If the value of this property is [`false`](https://developer.apple.com/documentation/Swift/false), the annotation view ignores touch events and isn’t selectable. Subclasses may also display the annotation contents differently depending on the value of this property.

## See Also

- [var image: UIImage?](mkannotationview/image.md)
  The image the annotation view displays.
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

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkannotationview/isenabled)*
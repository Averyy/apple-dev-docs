# calloutOffset

**Framework**: MapKit  
**Kind**: property

The offset (in points) at which to place the callout.

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
var calloutOffset: CGPoint { get set }
```

#### Discussion

This property determines the additional distance by which to move the callout. When this property is `(0, 0)`, the map view places the anchor point of the callout on the top-center point of the annotation view’s frame. Specifying positive offset values moves the callout down and to the right, and specifying negative values moves it up and to the left.

MapKit doesn’t use the [`calloutOffset`](mkannotationview/calloutoffset.md) property in macOS apps. Instead, macOS apps use [`leftCalloutOffset`](mkannotationview/leftcalloutoffset.md) and [`rightCalloutOffset`](mkannotationview/rightcalloutoffset.md).

## See Also

- [var isEnabled: Bool](mkannotationview/isenabled.md)
  A Boolean value that indicates whether the annotation is in an enabled state.
- [var image: UIImage?](mkannotationview/image.md)
  The image the annotation view displays.
- [var isHighlighted: Bool](mkannotationview/ishighlighted.md)
  A Boolean value that indicates whether the map view highlights the annotation view.
- [var annotation: (any MKAnnotation)?](mkannotationview/annotation.md)
  The annotation object associated with the view.
- [var centerOffset: CGPoint](mkannotationview/centeroffset.md)
  The offset (in points) at which to display the view.
- [var reuseIdentifier: String?](mkannotationview/reuseidentifier.md)
  The string that identifies that the annotation view is reusable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkannotationview/calloutoffset)*
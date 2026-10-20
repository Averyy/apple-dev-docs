# reuseIdentifier

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The string that identifies that the annotation view is reusable.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
var reuseIdentifier: String? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSString * reuseIdentifier;
```

#### Discussion

You specify the reuse identifier when you create the view. You use this type to retrieve an annotation view that MapKit isn’t currently using because its annotation isn’t onscreen.

If you define distinctly different types of annotations (with distinctly different annotation views to go with them), you can differentiate between the annotation types by specifying different reuse identifiers for each one.

## See Also

### Getting and setting attributes
- [var isEnabled: Bool](./isenabled.md)
  A Boolean value that indicates whether the annotation is in an enabled state.
- [var image: UIImage?](./image.md)
  The image the annotation view displays.
- [var isHighlighted: Bool](./ishighlighted.md)
  A Boolean value that indicates whether the map view highlights the annotation view.
- [var annotation: (any MKAnnotation)?](./annotation.md)
  The annotation object associated with the view.
- [var centerOffset: CGPoint](./centeroffset.md)
  The offset (in points) at which to display the view.
- [var calloutOffset: CGPoint](./calloutoffset.md)
  The offset (in points) at which to place the callout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkannotationview/reuseidentifier)*
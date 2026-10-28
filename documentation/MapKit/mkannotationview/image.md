# image

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The image the annotation view displays.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
var image: UIImage? { get set }
```

*macOS*

```swift
var image: NSImage? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, strong, nullable) UIImage * image;
```

*macOS*

```objc
@property (nonatomic, strong, nullable) NSImage * image;
```

## Discussion

Assigning a new image to this property also changes the size of the view’s frame so that it matches the width and height of the new image. The position of the view’s frame doesn’t change.

## See Also

### Getting and setting attributes
- [var isEnabled: Bool](./isenabled.md)
  A Boolean value that indicates whether the annotation is in an enabled state.
- [var isHighlighted: Bool](./ishighlighted.md)
  A Boolean value that indicates whether the map view highlights the annotation view.
- [var annotation: (any MKAnnotation)?](./annotation.md)
  The annotation object associated with the view.
- [var centerOffset: CGPoint](./centeroffset.md)
  The offset (in points) at which to display the view.
- [var calloutOffset: CGPoint](./calloutoffset.md)
  The offset (in points) at which to place the callout.
- [var reuseIdentifier: String?](./reuseidentifier.md)
  The string that identifies that the annotation view is reusable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkannotationview/image)*
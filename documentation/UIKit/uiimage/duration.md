# duration

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The time interval for displaying an animated image.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var duration: TimeInterval { get }
```

```objc
@property (nonatomic, readonly) NSTimeInterval duration;
```

## Discussion

For a non-animated image, the value of this property is `0.0`.

## See Also

### Accessing image attributes
- [var imageOrientation: UIImage.Orientation](./imageorientation.md)
  The orientation of the receiver’s image.
- [UIImage.Orientation](./orientation.md)
  Constants that specify the intended display orientation for an image.
- [var flipsForRightToLeftLayoutDirection: Bool](./flipsforrighttoleftlayoutdirection.md)
  A Boolean value that indicates whether the image flips in a right-to-left layout.
- [var resizingMode: UIImage.ResizingMode](./resizingmode-swift.property.md)
  The resizing mode of the image.
- [UIImage.ResizingMode](./resizingmode-swift.enum.md)
  Constants that specify the possible resizing modes for an image.
- [var capInsets: UIEdgeInsets](./capinsets.md)
  The end-cap insets.
- [var alignmentRectInsets: UIEdgeInsets](./alignmentrectinsets.md)
  The alignment metadata for positioning the image during layout.
- [var isSymbolImage: Bool](./issymbolimage.md)
  A Boolean value that indicates whether the image is a symbol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/duration)*
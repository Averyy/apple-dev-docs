# isSymbolImage

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the image is a symbol.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var isSymbolImage: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isSymbolImage) BOOL symbolImage;
```

#### Discussion

Symbol images are vector-based images that you use for your app’s iconography. The value of this property is [`true`](../../Swift/true.md) if the image is either a system-provided symbol image or a custom symbol image that you supplied in your asset catalog. The value is [`false`](../../Swift/false.md) for all other image types.

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
- [var duration: TimeInterval](./duration.md)
  The time interval for displaying an animated image.
- [var capInsets: UIEdgeInsets](./capinsets.md)
  The end-cap insets.
- [var alignmentRectInsets: UIEdgeInsets](./alignmentrectinsets.md)
  The alignment metadata for positioning the image during layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/issymbolimage)*
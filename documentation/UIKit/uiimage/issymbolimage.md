# isSymbolImage

**Framework**: UIKit  
**Kind**: property

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

#### Discussion

Symbol images are vector-based images that you use for your app’s iconography. The value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) if the image is either a system-provided symbol image or a custom symbol image that you supplied in your asset catalog. The value is [`false`](https://developer.apple.com/documentation/Swift/false) for all other image types.

## See Also

- [var imageOrientation: UIImage.Orientation](uiimage/imageorientation.md)
  The orientation of the receiver’s image.
- [UIImage.Orientation](uiimage/orientation.md)
  Constants that specify the intended display orientation for an image.
- [var flipsForRightToLeftLayoutDirection: Bool](uiimage/flipsforrighttoleftlayoutdirection.md)
  A Boolean value that indicates whether the image flips in a right-to-left layout.
- [var resizingMode: UIImage.ResizingMode](uiimage/resizingmode-swift.property.md)
  The resizing mode of the image.
- [UIImage.ResizingMode](uiimage/resizingmode-swift.enum.md)
  Constants that specify the possible resizing modes for an image.
- [var duration: TimeInterval](uiimage/duration.md)
  The time interval for displaying an animated image.
- [var capInsets: UIEdgeInsets](uiimage/capinsets.md)
  The end-cap insets.
- [var alignmentRectInsets: UIEdgeInsets](uiimage/alignmentrectinsets.md)
  The alignment metadata for positioning the image during layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/issymbolimage)*
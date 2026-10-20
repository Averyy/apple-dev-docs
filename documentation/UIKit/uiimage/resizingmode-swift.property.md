# resizingMode

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The resizing mode of the image.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var resizingMode: UIImage.ResizingMode { get }
```

```objc
@property (nonatomic, readonly) UIImageResizingMode resizingMode;
```

#### Discussion

The default value for this property is [`UIImage.ResizingMode.tile`](./resizingmode-swift.enum/tile.md). However, [`UIImage`](../uiimage.md) will implement the resizing mode the fastest way possible while still retaining the desired visual appearance. This means that if the region to be resized is a 1-pixel region and this property is set to [`UIImage.ResizingMode.tile`](./resizingmode-swift.enum/tile.md), the region will be stretched instead because the two are virtually indistinguishable for a region of that size and stretching is dramatically faster than tiling. To set the value of this property, you need to call either [`animatedResizableImageNamed(_:capInsets:resizingMode:duration:)`](./animatedresizableimagenamed%28_,capinsets,resizingmode,duration%29.md) or [`resizableImage(withCapInsets:resizingMode:)`](./resizableimage%28withcapinsets,resizingmode%29.md) and specify the resizing mode using the `resizingMode` parameter. For a list of possible values for this property, see [`UIImage.ResizingMode`](./resizingmode-swift.enum.md).

## See Also

### Accessing image attributes
- [var imageOrientation: UIImage.Orientation](./imageorientation.md)
  The orientation of the receiver’s image.
- [UIImage.Orientation](./orientation.md)
  Constants that specify the intended display orientation for an image.
- [var flipsForRightToLeftLayoutDirection: Bool](./flipsforrighttoleftlayoutdirection.md)
  A Boolean value that indicates whether the image flips in a right-to-left layout.
- [UIImage.ResizingMode](./resizingmode-swift.enum.md)
  Constants that specify the possible resizing modes for an image.
- [var duration: TimeInterval](./duration.md)
  The time interval for displaying an animated image.
- [var capInsets: UIEdgeInsets](./capinsets.md)
  The end-cap insets.
- [var alignmentRectInsets: UIEdgeInsets](./alignmentrectinsets.md)
  The alignment metadata for positioning the image during layout.
- [var isSymbolImage: Bool](./issymbolimage.md)
  A Boolean value that indicates whether the image is a symbol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/resizingmode-swift.property)*
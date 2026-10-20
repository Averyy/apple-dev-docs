# imageOrientation

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The orientation of the receiver’s image.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var imageOrientation: UIImage.Orientation { get }
```

```objc
@property (nonatomic, readonly) UIImageOrientation imageOrientation;
```

#### Discussion

Image orientation affects the way the image data is displayed when drawn. By default, images are displayed in the “up” orientation. If the image has associated metadata (such as EXIF information), however, this property contains the orientation indicated by that metadata. For a list of possible values for this property, see [`UIImage.Orientation`](./orientation.md).

## See Also

### Accessing image attributes
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
- [var isSymbolImage: Bool](./issymbolimage.md)
  A Boolean value that indicates whether the image is a symbol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/imageorientation)*
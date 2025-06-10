# UIImage.ResizingMode

**Framework**: UIKit  
**Kind**: enum

Constants that specify the possible resizing modes for an image.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+
- watchOS 2.0+

## Declaration

```swift
enum ResizingMode
```

## Topics

### Constants
- [UIImage.ResizingMode.tile](uiimage/resizingmode-swift.enum/tile.md)
  The image is tiled when it is resized. In other words, the interior region of the original image will be repeated to fill in the interior region of the newly resized image.
- [UIImage.ResizingMode.stretch](uiimage/resizingmode-swift.enum/stretch.md)
  The image is stretched when it is resized. In other words, the interior region of the original image will be scaled to fill in the interior region of the newly resized imaged.
### Initializers
- [init?(rawValue: Int)](uiimage/resizingmode-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var imageOrientation: UIImage.Orientation](uiimage/imageorientation.md)
  The orientation of the receiver’s image.
- [UIImage.Orientation](uiimage/orientation.md)
  Constants that specify the intended display orientation for an image.
- [var flipsForRightToLeftLayoutDirection: Bool](uiimage/flipsforrighttoleftlayoutdirection.md)
  A Boolean value that indicates whether the image flips in a right-to-left layout.
- [var resizingMode: UIImage.ResizingMode](uiimage/resizingmode-swift.property.md)
  The resizing mode of the image.
- [var duration: TimeInterval](uiimage/duration.md)
  The time interval for displaying an animated image.
- [var capInsets: UIEdgeInsets](uiimage/capinsets.md)
  The end-cap insets.
- [var alignmentRectInsets: UIEdgeInsets](uiimage/alignmentrectinsets.md)
  The alignment metadata for positioning the image during layout.
- [var isSymbolImage: Bool](uiimage/issymbolimage.md)
  A Boolean value that indicates whether the image is a symbol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/resizingmode-swift.enum)*
# UIImage.Orientation

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that specify the intended display orientation for an image.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS
- watchOS 2.0+

## Declaration

```swift
enum Orientation
```

```c
enum UIImageOrientation : NSInteger;
```

## Overview

Orientation values are commonly found in image metadata, and specifying image orientation correctly can be important both for displaying the image and for certain kinds of image processing.

The [`UIImage`](../uiimage.md) class automatically handles the transform necessary to present an image in the correct display orientation according to its orientation metadata, so an image object’s [`imageOrientation`](./imageorientation.md) property simply indicates which transform was applied.

For example, an iOS device camera always encodes pixel data in the camera sensor’s native landscape orientation, along with metadata indicating the camera orientation. When UIImage loads a photo shot in portrait orientation, it automatically applies a 90° rotation before displaying the image data, and the image’s [`imageOrientation`](./imageorientation.md) value of [`UIImage.Orientation.right`](./orientation/right.md) indicates that this rotation has been applied.

![UIImage rotates an image with right orientation for correct display](https://developer.apple.com/tutorials/images/com.apple.uikit/media-2948302@2x.png)

> **Note**:  Some frameworks describe image orientation using the [`CGImagePropertyOrientation`](../../ImageIO/cgimagepropertyorientation.md) type (or the raw TIFF/Exif numeric values that type defines symbols for). However, the underlying numeric values of that type are incompatible with [`UIImage.Orientation`](./orientation.md). For conversion help, see the [`CGImagePropertyOrientation`](../../ImageIO/cgimagepropertyorientation.md) overview.

## Topics

### Image orientations
- [UIImage.Orientation.up](./orientation/up.md)
  The original pixel data matches the image’s intended display orientation.
- [UIImage.Orientation.down](./orientation/down.md)
  The image has been rotated 180° from the orientation of its original pixel data.
- [UIImage.Orientation.left](./orientation/left.md)
  The image has been rotated 90° counterclockwise from the orientation of its original pixel data.
- [UIImage.Orientation.right](./orientation/right.md)
  The image has been rotated 90° clockwise from the orientation of its original pixel data.
- [UIImage.Orientation.upMirrored](./orientation/upmirrored.md)
  The image has been horizontally flipped from the orientation of its original pixel data.
- [UIImage.Orientation.downMirrored](./orientation/downmirrored.md)
  The image has been vertically flipped from the orientation of its original pixel data.
- [UIImage.Orientation.leftMirrored](./orientation/leftmirrored.md)
  The image has been rotated 90° clockwise and flipped horizontally from the orientation of its original pixel data.
- [UIImage.Orientation.rightMirrored](./orientation/rightmirrored.md)
  The image has been rotated 90° counterclockwise and flipped horizontally from the orientation of its original pixel data.
### Initializers
- [init?(rawValue: Int)](./orientation/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Related Documentation
- [enum CGImagePropertyOrientation](../../ImageIO/cgimagepropertyorientation.md)
  A value describing the intended display orientation for an image.
### Accessing image attributes
- [var imageOrientation: UIImage.Orientation](./imageorientation.md)
  The orientation of the receiver’s image.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/orientation)*
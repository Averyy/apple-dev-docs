# UIImage.Orientation.right

**Framework**: UIKit  
**Kind**: case

The image has been rotated 90° clockwise from the orientation of its original pixel data.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+
- watchOS 2.0+

## Declaration

```swift
case right
```

#### Discussion

If an image is encoded with this orientation, then displayed by software unaware of orientation metadata, the image appears to be rotated 90° counter-clockwise. (That is, to present the image in its intended orientation, you must rotate it 90° clockwise.)

![To correct an image with right orientation for display, rotate it 90° clockwise.](https://docs-assets.developer.apple.com/published/a4de8a358cbf9a76800cc595fceb8892/media-2948303%402x.png)

## See Also

- [CGImagePropertyOrientation.right](../ImageIO/CGImagePropertyOrientation/right.md)
  The encoded image data is rotated 90° clockwise from the image’s intended display orientation.
- [UIImage.Orientation.up](uiimage/orientation/up.md)
  The original pixel data matches the image’s intended display orientation.
- [UIImage.Orientation.down](uiimage/orientation/down.md)
  The image has been rotated 180° from the orientation of its original pixel data.
- [UIImage.Orientation.left](uiimage/orientation/left.md)
  The image has been rotated 90° counterclockwise from the orientation of its original pixel data.
- [UIImage.Orientation.upMirrored](uiimage/orientation/upmirrored.md)
  The image has been horizontally flipped from the orientation of its original pixel data.
- [UIImage.Orientation.downMirrored](uiimage/orientation/downmirrored.md)
  The image has been vertically flipped from the orientation of its original pixel data.
- [UIImage.Orientation.leftMirrored](uiimage/orientation/leftmirrored.md)
  The image has been rotated 90° clockwise and flipped horizontally from the orientation of its original pixel data.
- [UIImage.Orientation.rightMirrored](uiimage/orientation/rightmirrored.md)
  The image has been rotated 90° counterclockwise and flipped horizontally from the orientation of its original pixel data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/orientation/right)*
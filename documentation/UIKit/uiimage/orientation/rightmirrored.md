# UIImage.Orientation.rightMirrored

**Framework**: UIKit  
**Kind**: case

The image has been rotated 90° counterclockwise and flipped horizontally from the orientation of its original pixel data.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+
- watchOS 2.0+

## Declaration

```swift
case rightMirrored
```

#### Discussion

If an image is encoded with this orientation, then displayed by software unaware of orientation metadata, the image appears to be horizontally mirrored, then rotated 90° clockwise. (That is, to present the image in its intended orientation, you can rotate  90° counter-clockwise, then flip horizontally.)

![To correct an image with rightMirrored orientation for display, rotate it 90° counterclockwise then flip it horizontally.](https://docs-assets.developer.apple.com/published/6427cc1184994ac80c5119002426bac6/media-2948306%402x.png)

## See Also

- [CGImagePropertyOrientation.rightMirrored](../ImageIO/CGImagePropertyOrientation/rightMirrored.md)
  The encoded image data is horizontally flipped and rotated 90° clockwise from the image’s intended display orientation.
- [UIImage.Orientation.up](uiimage/orientation/up.md)
  The original pixel data matches the image’s intended display orientation.
- [UIImage.Orientation.down](uiimage/orientation/down.md)
  The image has been rotated 180° from the orientation of its original pixel data.
- [UIImage.Orientation.left](uiimage/orientation/left.md)
  The image has been rotated 90° counterclockwise from the orientation of its original pixel data.
- [UIImage.Orientation.right](uiimage/orientation/right.md)
  The image has been rotated 90° clockwise from the orientation of its original pixel data.
- [UIImage.Orientation.upMirrored](uiimage/orientation/upmirrored.md)
  The image has been horizontally flipped from the orientation of its original pixel data.
- [UIImage.Orientation.downMirrored](uiimage/orientation/downmirrored.md)
  The image has been vertically flipped from the orientation of its original pixel data.
- [UIImage.Orientation.leftMirrored](uiimage/orientation/leftmirrored.md)
  The image has been rotated 90° clockwise and flipped horizontally from the orientation of its original pixel data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/orientation/rightmirrored)*
# UIImage.Orientation.leftMirrored

**Framework**: UIKit  
**Kind**: case

The image has been rotated 90° clockwise and flipped horizontally from the orientation of its original pixel data.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+
- watchOS 2.0+

## Declaration

```swift
case leftMirrored
```

#### Discussion

If an image is encoded with this orientation, then displayed by software unaware of orientation metadata, the image appears to be horizontally mirrored, then rotated 90° counter-clockwise. (That is, to present the image in its intended orientation, you can rotate it 90° clockwise, then flip horizontally.)

![To correct an image with leftMirrored orientation for display, rotate it 90° clockwise then flip it horizontally.](https://docs-assets.developer.apple.com/published/ed7462784881f7d23e39b968a2ecefff/media-2948307%402x.png)

## See Also

- [CGImagePropertyOrientation.leftMirrored](../ImageIO/CGImagePropertyOrientation/leftMirrored.md)
  The encoded image data is horizontally flipped and rotated 90° counter-clockwise from the image’s intended display orientation.
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
- [UIImage.Orientation.rightMirrored](uiimage/orientation/rightmirrored.md)
  The image has been rotated 90° counterclockwise and flipped horizontally from the orientation of its original pixel data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/orientation/leftmirrored)*
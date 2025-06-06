# UIImage.Orientation.upMirrored

**Framework**: UIKit  
**Kind**: case

The image has been horizontally flipped from the orientation of its original pixel data.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+
- watchOS 2.0+

## Declaration

```swift
case upMirrored
```

#### Discussion

If an image is encoded with this orientation, then displayed by software unaware of orientation metadata, the image appears horizontally mirrored.

![To correct an image with upMirrored orientation for display, flip it horizontally.](https://docs-assets.developer.apple.com/published/3b93501e18e409bc3d6f779ae1e59673/media-2948304%402x.png)

## See Also

- [CGImagePropertyOrientation.upMirrored](../ImageIO/CGImagePropertyOrientation/upMirrored.md)
  The encoded image data is horizontally flipped from the image’s intended display orientation.
- [UIImage.Orientation.up](uiimage/orientation/up.md)
  The original pixel data matches the image’s intended display orientation.
- [UIImage.Orientation.down](uiimage/orientation/down.md)
  The image has been rotated 180° from the orientation of its original pixel data.
- [UIImage.Orientation.left](uiimage/orientation/left.md)
  The image has been rotated 90° counterclockwise from the orientation of its original pixel data.
- [UIImage.Orientation.right](uiimage/orientation/right.md)
  The image has been rotated 90° clockwise from the orientation of its original pixel data.
- [UIImage.Orientation.downMirrored](uiimage/orientation/downmirrored.md)
  The image has been vertically flipped from the orientation of its original pixel data.
- [UIImage.Orientation.leftMirrored](uiimage/orientation/leftmirrored.md)
  The image has been rotated 90° clockwise and flipped horizontally from the orientation of its original pixel data.
- [UIImage.Orientation.rightMirrored](uiimage/orientation/rightmirrored.md)
  The image has been rotated 90° counterclockwise and flipped horizontally from the orientation of its original pixel data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/orientation/upmirrored)*
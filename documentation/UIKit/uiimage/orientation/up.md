# UIImage.Orientation.up

**Framework**: UIKit  
**Kind**: case

The original pixel data matches the image’s intended display orientation.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+
- watchOS 2.0+

## Declaration

```swift
case up
```

#### Discussion

If an image is encoded with this orientation, then displayed by software unaware of orientation metadata, the image appears correctly “right side up”. That is, this orientation is an identity value.

![An image in up orientation can be presented for display without rotating or flipping.](https://docs-assets.developer.apple.com/published/08b6857053beb92301df7ceb36ab8175/media-2948308%402x.png)

## See Also

- [CGImagePropertyOrientation.up](../ImageIO/CGImagePropertyOrientation/up.md)
  The encoded image data matches the image’s intended display orientation.
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
- [UIImage.Orientation.rightMirrored](uiimage/orientation/rightmirrored.md)
  The image has been rotated 90° counterclockwise and flipped horizontally from the orientation of its original pixel data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/orientation/up)*
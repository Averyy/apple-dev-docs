# CGImagePropertyOrientation.left

**Framework**: Image I/O  
**Kind**: case

The encoded image data is rotated 90° clockwise from the image’s intended display orientation.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
case left
```

#### Discussion

The (x,y) pixel coordinates of the origin point (0,0) represent the bottom row and leftmost column, respectively. Pixel (x,y) positions increase bottom-to-top, left-to-right.

If an image is encoded with this orientation, then displayed by software unaware of orientation metadata, the image appears to be rotated 90° clockwise. (That is, to present the image in its intended orientation, you must rotate 90° counter-clockwise.)

![To correct an image with left orientation for display, rotate it 90° counterclockwise.](https://docs-assets.developer.apple.com/published/a33bb23b55f1eb490a0abf2b86b81f66/media-2948296%402x.png)

## See Also

- [CGImagePropertyOrientation.up](cgimagepropertyorientation/up.md)
  The encoded image data matches the image’s intended display orientation.
- [CGImagePropertyOrientation.upMirrored](cgimagepropertyorientation/upmirrored.md)
  The encoded image data is horizontally flipped from the image’s intended display orientation.
- [CGImagePropertyOrientation.down](cgimagepropertyorientation/down.md)
  The encoded image data is rotated 180° from the image’s intended display orientation.
- [CGImagePropertyOrientation.downMirrored](cgimagepropertyorientation/downmirrored.md)
  The encoded image data is vertically flipped from the image’s intended display orientation.
- [CGImagePropertyOrientation.leftMirrored](cgimagepropertyorientation/leftmirrored.md)
  The encoded image data is horizontally flipped and rotated 90° counter-clockwise from the image’s intended display orientation.
- [CGImagePropertyOrientation.right](cgimagepropertyorientation/right.md)
  The encoded image data is rotated 90° clockwise from the image’s intended display orientation.
- [CGImagePropertyOrientation.rightMirrored](cgimagepropertyorientation/rightmirrored.md)
  The encoded image data is horizontally flipped and rotated 90° clockwise from the image’s intended display orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagepropertyorientation/left)*
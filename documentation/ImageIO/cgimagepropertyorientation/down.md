# CGImagePropertyOrientation.down

**Framework**: Image I/O  
**Kind**: case

The encoded image data is rotated 180° from the image’s intended display orientation.

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
case down
```

#### Discussion

The (x,y) pixel coordinates of the origin point (0,0) represent the rightmost column and bottom row, respectively. Pixel (x,y) positions increase right-to-left, bottom-to-top.

If an image is encoded with this orientation, then displayed by software unaware of orientation metadata, the image appears rotated 180°.

![To correct an image with down orientation for display, rotate it 180°.](https://docs-assets.developer.apple.com/published/1530f2c9454d2a3fb9e99de9bee4fe01/media-2948290%402x.png)

## See Also

- [CGImagePropertyOrientation.up](cgimagepropertyorientation/up.md)
  The encoded image data matches the image’s intended display orientation.
- [CGImagePropertyOrientation.upMirrored](cgimagepropertyorientation/upmirrored.md)
  The encoded image data is horizontally flipped from the image’s intended display orientation.
- [CGImagePropertyOrientation.downMirrored](cgimagepropertyorientation/downmirrored.md)
  The encoded image data is vertically flipped from the image’s intended display orientation.
- [CGImagePropertyOrientation.leftMirrored](cgimagepropertyorientation/leftmirrored.md)
  The encoded image data is horizontally flipped and rotated 90° counter-clockwise from the image’s intended display orientation.
- [CGImagePropertyOrientation.right](cgimagepropertyorientation/right.md)
  The encoded image data is rotated 90° clockwise from the image’s intended display orientation.
- [CGImagePropertyOrientation.rightMirrored](cgimagepropertyorientation/rightmirrored.md)
  The encoded image data is horizontally flipped and rotated 90° clockwise from the image’s intended display orientation.
- [CGImagePropertyOrientation.left](cgimagepropertyorientation/left.md)
  The encoded image data is rotated 90° clockwise from the image’s intended display orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagepropertyorientation/down)*
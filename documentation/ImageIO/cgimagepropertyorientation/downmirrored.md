# CGImagePropertyOrientation.downMirrored

**Framework**: Image I/O  
**Kind**: case

The encoded image data is vertically flipped from the image’s intended display orientation.

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
case downMirrored
```

#### Discussion

The (x,y) pixel coordinates of the origin point (0,0) represent the leftmost column and bottom row, respectively. Pixel (x,y) positions increase left-to-right, bottom-to-top.

If an image is encoded with this orientation, then displayed by software unaware of orientation metadata, the image appears vertically flipped. (Alternatively, the image is rotated 180° and then flipped horizontally.)

![To correct an image with downMirrored orientation for display, flip it vertically.](https://docs-assets.developer.apple.com/published/8170a1cc20c32b7a29544fc6e92a7f74/media-2948294%402x.png)

## See Also

- [CGImagePropertyOrientation.up](cgimagepropertyorientation/up.md)
  The encoded image data matches the image’s intended display orientation.
- [CGImagePropertyOrientation.upMirrored](cgimagepropertyorientation/upmirrored.md)
  The encoded image data is horizontally flipped from the image’s intended display orientation.
- [CGImagePropertyOrientation.down](cgimagepropertyorientation/down.md)
  The encoded image data is rotated 180° from the image’s intended display orientation.
- [CGImagePropertyOrientation.leftMirrored](cgimagepropertyorientation/leftmirrored.md)
  The encoded image data is horizontally flipped and rotated 90° counter-clockwise from the image’s intended display orientation.
- [CGImagePropertyOrientation.right](cgimagepropertyorientation/right.md)
  The encoded image data is rotated 90° clockwise from the image’s intended display orientation.
- [CGImagePropertyOrientation.rightMirrored](cgimagepropertyorientation/rightmirrored.md)
  The encoded image data is horizontally flipped and rotated 90° clockwise from the image’s intended display orientation.
- [CGImagePropertyOrientation.left](cgimagepropertyorientation/left.md)
  The encoded image data is rotated 90° clockwise from the image’s intended display orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagepropertyorientation/downmirrored)*
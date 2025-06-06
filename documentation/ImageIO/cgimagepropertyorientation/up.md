# CGImagePropertyOrientation.up

**Framework**: Image I/O  
**Kind**: case

The encoded image data matches the image’s intended display orientation.

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
case up
```

#### Discussion

The (x,y) pixel coordinates of the origin point (0,0) represent the leftmost column and top row, respectively. Pixel (x,y) positions increase left-to-right, top-to-bottom.

If an image is encoded with this orientation, then displayed by software unaware of orientation metadata, the image appears correctly “right side up”. That is, this orientation is an identity value.

![An image in up orientation can be presented for display without rotating or flipping.](https://docs-assets.developer.apple.com/published/08b6857053beb92301df7ceb36ab8175/media-2948288%402x.png)

## See Also

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
- [CGImagePropertyOrientation.left](cgimagepropertyorientation/left.md)
  The encoded image data is rotated 90° clockwise from the image’s intended display orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagepropertyorientation/up)*
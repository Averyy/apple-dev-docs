# CGImagePropertyOrientation.up

**Framework**: Image I/O  
**Kind**: case  
**Role**: Case

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

```c
kCGImagePropertyOrientationUp
```

## Discussion

The (x,y) pixel coordinates of the origin point (0,0) represent the leftmost column and top row, respectively. Pixel (x,y) positions increase left-to-right, top-to-bottom.

If an image is encoded with this orientation, then displayed by software unaware of orientation metadata, the image appears correctly “right side up”. That is, this orientation is an identity value.

![An image in up orientation can be presented for display without rotating or flipping.](https://developer.apple.com/tutorials/images/com.apple.imageio/media-2948288@2x.png)

## See Also

### Image Orientations
- [CGImagePropertyOrientation.upMirrored](./upmirrored.md)
  The encoded image data is horizontally flipped from the image’s intended display orientation.
- [CGImagePropertyOrientation.down](./down.md)
  The encoded image data is rotated 180° from the image’s intended display orientation.
- [CGImagePropertyOrientation.downMirrored](./downmirrored.md)
  The encoded image data is vertically flipped from the image’s intended display orientation.
- [CGImagePropertyOrientation.leftMirrored](./leftmirrored.md)
  The encoded image data is horizontally flipped and rotated 90° counter-clockwise from the image’s intended display orientation.
- [CGImagePropertyOrientation.right](./right.md)
  The encoded image data is rotated 90° counter-clockwise from the image’s intended display orientation.
- [CGImagePropertyOrientation.rightMirrored](./rightmirrored.md)
  The encoded image data is horizontally flipped and rotated 90° clockwise from the image’s intended display orientation.
- [CGImagePropertyOrientation.left](./left.md)
  The encoded image data is rotated 90° clockwise from the image’s intended display orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagepropertyorientation/up)*
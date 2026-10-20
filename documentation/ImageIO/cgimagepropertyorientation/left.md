# CGImagePropertyOrientation.left

**Framework**: Image I/O  
**Kind**: case  
**Role**: Case

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

```c
kCGImagePropertyOrientationLeft
```

#### Discussion

The (x,y) pixel coordinates of the origin point (0,0) represent the bottom row and leftmost column, respectively. Pixel (x,y) positions increase bottom-to-top, left-to-right.

If an image is encoded with this orientation, then displayed by software unaware of orientation metadata, the image appears to be rotated 90° clockwise. (That is, to present the image in its intended orientation, you must rotate 90° counter-clockwise.)

![To correct an image with left orientation for display, rotate it 90° counterclockwise.](https://developer.apple.com/tutorials/images/com.apple.imageio/media-2948296@2x.png)

## See Also

### Image Orientations
- [CGImagePropertyOrientation.up](./up.md)
  The encoded image data matches the image’s intended display orientation.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagepropertyorientation/left)*
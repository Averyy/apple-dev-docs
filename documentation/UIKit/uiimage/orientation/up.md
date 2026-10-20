# UIImage.Orientation.up

**Framework**: UIKit  
**Kind**: case  
**Role**: Case

The original pixel data matches the image’s intended display orientation.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS
- watchOS 2.0+

## Declaration

```swift
case up
```

```c
UIImageOrientationUp
```

#### Discussion

If an image is encoded with this orientation, then displayed by software unaware of orientation metadata, the image appears correctly “right side up”. That is, this orientation is an identity value.

![An image in up orientation can be presented for display without rotating or flipping.](https://developer.apple.com/tutorials/images/com.apple.uikit/media-2948308@2x.png)

## See Also

### Related Documentation
- [CGImagePropertyOrientation.up](../../../ImageIO/cgimagepropertyorientation/up.md)
  The encoded image data matches the image’s intended display orientation.
### Image orientations
- [UIImage.Orientation.down](./down.md)
  The image has been rotated 180° from the orientation of its original pixel data.
- [UIImage.Orientation.left](./left.md)
  The image has been rotated 90° counterclockwise from the orientation of its original pixel data.
- [UIImage.Orientation.right](./right.md)
  The image has been rotated 90° clockwise from the orientation of its original pixel data.
- [UIImage.Orientation.upMirrored](./upmirrored.md)
  The image has been horizontally flipped from the orientation of its original pixel data.
- [UIImage.Orientation.downMirrored](./downmirrored.md)
  The image has been vertically flipped from the orientation of its original pixel data.
- [UIImage.Orientation.leftMirrored](./leftmirrored.md)
  The image has been rotated 90° clockwise and flipped horizontally from the orientation of its original pixel data.
- [UIImage.Orientation.rightMirrored](./rightmirrored.md)
  The image has been rotated 90° counterclockwise and flipped horizontally from the orientation of its original pixel data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/orientation/up)*
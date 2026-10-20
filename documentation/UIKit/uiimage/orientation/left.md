# UIImage.Orientation.left

**Framework**: UIKit  
**Kind**: case  
**Role**: Case

The image has been rotated 90° counterclockwise from the orientation of its original pixel data.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS
- watchOS 2.0+

## Declaration

```swift
case left
```

```c
UIImageOrientationLeft
```

#### Discussion

If an image is encoded with this orientation, then displayed by software unaware of orientation metadata, the image appears to be rotated 90° clockwise. (That is, to present the image in its intended orientation, you must rotate 90° counter-clockwise.)

![To correct an image with left orientation for display, rotate it 90° counterclockwise.](https://developer.apple.com/tutorials/images/com.apple.uikit/media-2948305@2x.png)

## See Also

### Related Documentation
- [CGImagePropertyOrientation.left](../../../ImageIO/cgimagepropertyorientation/left.md)
  The encoded image data is rotated 90° clockwise from the image’s intended display orientation.
### Image orientations
- [UIImage.Orientation.up](./up.md)
  The original pixel data matches the image’s intended display orientation.
- [UIImage.Orientation.down](./down.md)
  The image has been rotated 180° from the orientation of its original pixel data.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/orientation/left)*
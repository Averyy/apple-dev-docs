# setRotationAngle(_:center:)

**Framework**: Quartz  
**Kind**: method

Sets the rotation angle at the provided origin.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func setRotationAngle(_ rotationAngle: CGFloat, center centerPoint: NSPoint)
```

## Parameters

- `rotationAngle`: The rotation angle to apply to the image.
- `centerPoint`: The point that specifies the origin of the rotation angle.

## See Also

- [var rotationAngle: CGFloat](ikimageview/rotationangle.md)
  Specifies the rotation angle for the image view.
- [func setImageZoomFactor(CGFloat, center: NSPoint)](ikimageview/setimagezoomfactor(_:center:).md)
  Sets the zoom factor at the provided origin.
- [func zoomImageToFit(Any!)](ikimageview/zoomimagetofit(_:).md)
  Zooms the image so that it fits in the image view.
- [func zoomImageToActualSize(Any!)](ikimageview/zoomimagetoactualsize(_:).md)
  Zooms the image so that it is displayed using its true size.
- [func zoomImage(to: NSRect)](ikimageview/zoomimage(to:).md)
  Zooms the image so that it fits in the specified rectangle.
- [func zoomIn(Any!)](ikimageview/zoomin(_:).md)
  Zooms the image in.
- [func zoomOut(Any!)](ikimageview/zoomout(_:).md)
  Zooms the image out.
- [func crop(Any!)](ikimageview/crop(_:).md)
  Crops the image using the current selection.
- [func flipImageHorizontal(Any!)](ikimageview/flipimagehorizontal(_:).md)
  Flips an image along the horizontal axis.
- [func flipImageVertical(Any!)](ikimageview/flipimagevertical(_:).md)
  Flips an image along the vertical axis.
- [func rotateImageLeft(Any!)](ikimageview/rotateimageleft(_:).md)
  Rotates the image left (counter-clockwise).
- [func rotateImageRight(Any!)](ikimageview/rotateimageright(_:).md)
  Rotates the image right (clockwise).


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimageview/setrotationangle(_:center:))*
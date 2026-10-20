# setImageZoomFactor(_:center:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Sets the zoom factor at the provided origin.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func setImageZoomFactor(_ zoomFactor: CGFloat, center centerPoint: NSPoint)
```

```objc
- (void) setImageZoomFactor:(CGFloat) zoomFactor centerPoint:(NSPoint) centerPoint;
```

## Parameters

- `zoomFactor`: The zoom factor to apply to the image.
- `centerPoint`: The point that specifies the origin of the zoom factor.

## See Also

### Related Documentation
- [var zoomFactor: CGFloat](./zoomfactor.md)
  Specifies the zoom factor for the image view.
### Manipulating the Image in a View
- [func setRotationAngle(CGFloat, center: NSPoint)](./setrotationangle%28_,center%29.md)
  Sets the rotation angle at the provided origin.
- [func zoomImageToFit(Any!)](./zoomimagetofit%28_%29.md)
  Zooms the image so that it fits in the image view.
- [func zoomImageToActualSize(Any!)](./zoomimagetoactualsize%28_%29.md)
  Zooms the image so that it is displayed using its true size.
- [func zoomImage(to: NSRect)](./zoomimage%28to%29.md)
  Zooms the image so that it fits in the specified rectangle.
- [func zoomIn(Any!)](./zoomin%28_%29.md)
  Zooms the image in.
- [func zoomOut(Any!)](./zoomout%28_%29.md)
  Zooms the image out.
- [func crop(Any!)](./crop%28_%29.md)
  Crops the image using the current selection.
- [func flipImageHorizontal(Any!)](./flipimagehorizontal%28_%29.md)
  Flips an image along the horizontal axis.
- [func flipImageVertical(Any!)](./flipimagevertical%28_%29.md)
  Flips an image along the vertical axis.
- [func rotateImageLeft(Any!)](./rotateimageleft%28_%29.md)
  Rotates the image left (counter-clockwise).
- [func rotateImageRight(Any!)](./rotateimageright%28_%29.md)
  Rotates the image right (clockwise).


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimageview/setimagezoomfactor(_:center:))*
# displayTransformForOrientation:viewportSize:

**Framework**: ARKit  
**Kind**: method  
**Role**: Instance Method

Returns an affine transform for converting between normalized image coordinates and a coordinate space appropriate for rendering the camera image onscreen.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0

## Declaration

```objc
- (CGAffineTransform) displayTransformForOrientation:(UIInterfaceOrientation) orientation viewportSize:(CGSize) viewportSize;
```

## Return Value

A transform matrix that converts from normalized image coordinates in the captured image to normalized image coordinates that account for the specified parameters.

## Discussion

Normalized image coordinates range from `(0,0)` in the upper left corner of the image to `(1,1)` in the lower right corner.

This method creates an affine transform representing the rotation and aspect-fit crop operations necessary to adapt the camera image to the specified orientation and to the aspect ratio of the specified viewport. The affine transform does not scale to the viewport’s pixel size.

The [`capturedImage`](./capturedimage.md) pixel buffer is the original image captured by the device camera, and thus not adjusted for device orientation or view aspect ratio.

## Parameters

- `orientation`: The orientation intended for presenting the view.
- `viewportSize`: The size, in points, of the view intended for rendering the camera image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arframe/displaytransformfororientation:viewportsize:)*
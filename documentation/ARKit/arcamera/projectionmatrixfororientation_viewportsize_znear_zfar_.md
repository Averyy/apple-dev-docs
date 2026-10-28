# projectionMatrixForOrientation:viewportSize:zNear:zFar:

**Framework**: ARKit  
**Kind**: method  
**Role**: Instance Method

Returns a transform matrix appropriate for rendering 3D content to match the image captured by the camera, using the specified parameters.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0

## Declaration

```objc
- (simd_float4x4) projectionMatrixForOrientation:(UIInterfaceOrientation) orientation viewportSize:(CGSize) viewportSize zNear:(CGFloat) zNear zFar:(CGFloat) zFar;
```

## Return Value

A projection matrix that provides an aspect fill and rotation for the provided viewport size and orientation.

## Discussion

This method has no effect on ARKit, and the `zNear` and `zFar` parameters have no relationships to ARKit camera state. Instead, this method uses those parameters as well as the camera’s state to construct a projection matrix for use in your own rendering code.

The projection matrix returned provides an aspect fill for the provided viewport size and orientation. If zFar is set to 0, an infinite projection matrix will be returned.

## Parameters

- `orientation`: The orientation in which the camera image is to be presented.
- `viewportSize`: The size, in points, of the view in which the camera image is to be presented.
- `zNear`: The distance from the camera to the near clipping plane.
- `zFar`: The distance from the camera to the far clipping plane.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arcamera/projectionmatrixfororientation:viewportsize:znear:zfar:)*
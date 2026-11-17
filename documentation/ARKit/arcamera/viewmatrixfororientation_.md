# viewMatrixForOrientation:

**Framework**: ARKit  
**Kind**: method  
**Role**: Instance Method

Returns a transform matrix for converting from world space to camera space.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0

## Declaration

```objc
- (simd_float4x4) viewMatrixForOrientation:(UIInterfaceOrientation) orientation;
```

## Return Value

A view matrix appropriate for the camera with the specified orientation.

## Discussion

This method has no effect on ARKit. Instead, this method uses the orientation parameter and the camera’s state to construct a view matrix for your own rendering code.

The view matrix can be used to transform geometry from world space into camera space for a given orientation.

## Parameters

- `orientation`: The orientation in which the camera image is to be presented.

## See Also

### Applying Camera Geometry
- [var projectionMatrix: simd_float4x4](./projectionmatrix.md)
  A transform matrix appropriate for rendering 3D content to match the image captured by the camera.
- [- projectionMatrixForOrientation:viewportSize:zNear:zFar:](./projectionmatrixfororientation_viewportsize_znear_zfar_.md)
  Returns a transform matrix appropriate for rendering 3D content to match the image captured by the camera, using the specified parameters.
- [- projectPoint:orientation:viewportSize:](./projectpoint_orientation_viewportsize_.md)
  Returns the projection of a point from the 3D world space detected by ARKit into the 2D space of a view rendering the scene.
- [- unprojectPoint:ontoPlaneWithTransform:orientation:viewportSize:](./unprojectpoint_ontoplanewithtransform_orientation_viewportsize_.md)
  Returns the projection of a point from the 2D space of a view rendering the scene onto a plane in the 3D world space detected by ARKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arcamera/viewmatrixfororientation:)*
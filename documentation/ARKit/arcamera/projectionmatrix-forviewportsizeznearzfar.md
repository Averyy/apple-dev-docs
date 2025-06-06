# projectionMatrix(for:viewportSize:zNear:zFar:)

**Framework**: ARKit  
**Kind**: method

Returns a transform matrix appropriate for rendering 3D content to match the image captured by the camera, using the specified parameters.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func projectionMatrix(for orientation: UIInterfaceOrientation, viewportSize: CGSize, zNear: CGFloat, zFar: CGFloat) -> simd_float4x4
```

#### Return Value

A projection matrix that provides an aspect fill and rotation for the provided viewport size and orientation.

#### Discussion

This method has no effect on ARKit, and the `zNear` and `zFar` parameters have no relationships to ARKit camera state. Instead, this method uses those parameters as well as the camera’s state to construct a projection matrix for use in your own rendering code.

## Parameters

- `orientation`: The orientation in which the camera image is to be presented.
- `viewportSize`: The size, in points, of the view in which the camera image is to be presented.
- `zNear`: The distance from the camera to the near clipping plane.
- `zFar`: The distance from the camera to the far clipping plane.

## See Also

- [var projectionMatrix: simd_float4x4](arcamera/projectionmatrix.md)
  A transform matrix appropriate for rendering 3D content to match the image captured by the camera.
- [func viewMatrix(for: UIInterfaceOrientation) -> simd_float4x4](arcamera/viewmatrix(for:).md)
  Returns a transform matrix for converting from world space to camera space.
- [func projectPoint(simd_float3, orientation: UIInterfaceOrientation, viewportSize: CGSize) -> CGPoint](arcamera/projectpoint(_:orientation:viewportsize:).md)
  Returns the projection of a point from the 3D world space detected by ARKit into the 2D space of a view rendering the scene.
- [func unprojectPoint(CGPoint, ontoPlane: simd_float4x4, orientation: UIInterfaceOrientation, viewportSize: CGSize) -> simd_float3?](arcamera/unprojectpoint(_:ontoplane:orientation:viewportsize:).md)
  Returns the projection of a point from the 2D space of a view rendering the scene onto a plane in the 3D world space detected by ARKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arcamera/projectionmatrix(for:viewportsize:znear:zfar:))*
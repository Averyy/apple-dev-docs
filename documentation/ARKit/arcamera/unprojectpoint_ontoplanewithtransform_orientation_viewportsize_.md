# unprojectPoint:ontoPlaneWithTransform:orientation:viewportSize:

**Framework**: ARKit  
**Kind**: method  
**Role**: Instance Method

Returns the projection of a point from the 2D space of a view rendering the scene onto a plane in the 3D world space detected by ARKit.

**Availability**:
- iOS 12.0+ - Deprecated in 27.0
- iPadOS 12.0+ - Deprecated in 27.0

## Declaration

```objc
- (simd_float3) unprojectPoint:(CGPoint) point ontoPlaneWithTransform:(simd_float4x4) planeTransform orientation:(UIInterfaceOrientation) orientation viewportSize:(CGSize) viewportSize;
```

## Return Value

The 3D point in world space where a ray projected from the specified 2D point intersects the specified plane. If the ray does not intersect the plane, this method returns a `float3` vector where all elements are `NaN`.

## Discussion

A 2D point in the viewport coordinate space can refer to any point along a line segment in the 3D coordinate space. Unprojecting calculates the 3D position of the point along this line segment that intersects the provided plane.

If you display AR content with SceneKit, the `ARSCNView` class provides an otherwise equivalent `ARSCNView.unprojectPoint(_:ontoPlane:)` method that requires fewer parameters (because the view can infer its orientation and size).

## Parameters

- `point`: The point in 2D view space to project onto a plane.

  The coordinate space for this point has its origin in the upper left corner and a size matching the `viewportSize` parameter.
- `planeTransform`: A transform matrix specifying the position and orientation of a plane (with infinite extent) in 3D world space. The plane is the xz-plane of the local coordinate space this transform defines.
- `orientation`: The orientation in which the camera image is to be presented.
- `viewportSize`: The size, in points, of the view in which the camera image is to be presented.

## See Also

### Applying Camera Geometry
- [var projectionMatrix: simd_float4x4](./projectionmatrix.md)
  A transform matrix appropriate for rendering 3D content to match the image captured by the camera.
- [- projectionMatrixForOrientation:viewportSize:zNear:zFar:](./projectionmatrixfororientation_viewportsize_znear_zfar_.md)
  Returns a transform matrix appropriate for rendering 3D content to match the image captured by the camera, using the specified parameters.
- [- viewMatrixForOrientation:](./viewmatrixfororientation_.md)
  Returns a transform matrix for converting from world space to camera space.
- [- projectPoint:orientation:viewportSize:](./projectpoint_orientation_viewportsize_.md)
  Returns the projection of a point from the 3D world space detected by ARKit into the 2D space of a view rendering the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arcamera/unprojectpoint:ontoplanewithtransform:orientation:viewportsize:)*
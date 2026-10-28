# projectionMatrix

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

A transform matrix appropriate for rendering 3D content to match the image captured by the camera.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
var projectionMatrix: simd_float4x4 { get }
```

```objc
@property (nonatomic, readonly) simd_float4x4 projectionMatrix;
```

## Discussion

Reading this property’s value is equivalent to calling the `projectionMatrix(withViewportSize:orientation:zNear:zFar:)` method, using the camera’s [`imageResolution`](./imageresolution.md) and [`intrinsics`](./intrinsics.md) properties to derive size and orientation, and passing default values of `0.001` and `1000.0` for the near and far clipping planes.

## See Also

### Applying Camera Geometry
- [func unprojectPoint(CGPoint, ontoPlane: simd_float4x4, orientation: UIInterfaceOrientation, viewportSize: CGSize) -> simd_float3?](./unprojectpoint%28_,ontoplane,orientation,viewportsize%29.md)
  Returns the projection of a point from the 2D space of a view rendering the scene onto a plane in the 3D world space detected by ARKit.
- [- unprojectPoint:ontoPlaneWithTransform:orientation:viewportSize:](./unprojectpoint_ontoplanewithtransform_orientation_viewportsize_.md)
  Returns the projection of a point from the 2D space of a view rendering the scene onto a plane in the 3D world space detected by ARKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arcamera/projectionmatrix)*
# unproject(_:ontoPlane:relativeToCamera:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Unproject a 2D point from the view onto a plane in 3D world coordinates.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency func unproject(_ point: CGPoint, ontoPlane planeTransform: float4x4, relativeToCamera: Bool) -> SIMD3<Float>?
```

## Return Value

3D position in world coordinates or nil if unprojection is not possible.

## Discussion

A 2D point in the view’s coordinate space can refer to any point along a line segment in the 3D coordinate space. Unprojecting gets the 3D position of the point along this line segment that intersects the provided plane.

## Parameters

- `point`: A point in the view’s coordinate system.
- `planeTransform`: The transform used to define the coordinate system of the plane. The coordinate system’s positive y-axis is assumed to be the normal of the plane.
- `relativeToCamera`: If the plane transform is relative to camera space or world space.

## See Also

### Mapping between coordinate spaces
- [func project(SIMD3<Float>) -> CGPoint?](./project%28_%29.md)
  Projects a point from the 3D world coordinate system of the scene to the 2D pixel coordinate system of the view.
- [func unproject(CGPoint, ontoPlane: float4x4) -> SIMD3<Float>?](./unproject%28_,ontoplane%29.md)
  Maps a 2D point from the view’s coordinate system onto the given plane in 3D space.
- [func unproject(CGPoint, viewport: CGRect) -> SIMD3<Float>?](./unproject%28_,viewport%29.md)
  Maps a 2D point from the pixel coordinate system of a viewport into a 3D coordinate space. The point lies on this view’s near clipping plane.
- [func ray(through: CGPoint) -> (origin: SIMD3<Float>, direction: SIMD3<Float>)?](./ray%28through%29.md)
  Determines the position and direction of a ray through the given point in the 2D space of the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/unproject(_:ontoplane:relativetocamera:))*
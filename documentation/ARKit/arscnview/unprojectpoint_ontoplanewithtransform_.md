# unprojectPoint:ontoPlaneWithTransform:

**Framework**: ARKit  
**Kind**: method  
**Role**: Instance Method

Returns the projection of a point from 2D view onto a plane in the 3D world space detected by ARKit.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+

## Declaration

```objc
- (simd_float3) unprojectPoint:(CGPoint) point ontoPlaneWithTransform:(simd_float4x4) planeTransform;
```

## Return Value

The 3D point in world space where a ray projected from the specified 2D point intersects the specified plane. If the ray does not intersect the plane, this method returns a `float3` vector where all elements are `NaN`.

## Parameters

- `point`: The point in 2D view space to project onto a plane.

  The coordinate space for this point has its origin in the upper left corner and a size matching the view’s bounds.
- `planeTransform`: A transform matrix specifying the position and orientation of a plane (with infinite extent) in 3D world space. The plane is the xz-plane of the local coordinate space this transform defines.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arscnview/unprojectpoint:ontoplanewithtransform:)*
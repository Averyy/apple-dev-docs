# unprojectPoint(_:ontoPlane:)

**Framework**: ARKit  
**Kind**: method

Returns the projection of a point from 2D view onto a plane in the 3D world space detected by ARKit.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+

## Declaration

```swift
@MainActor
@nonobjc @preconcurrency func unprojectPoint(_ point: CGPoint, ontoPlane planeTransform: simd_float4x4) -> simd_float3?
```

#### Return Value

The 3D point in world space where a ray projected from the specified 2D point intersects the specified plane. If the ray does not intersect the plane, this method returns `nil`.

## Parameters

- `point`: A point in the 2D coordinate system of the view to project onto a plane.
- `planeTransform`: A transform matrix specifying the position and orientation of a plane (with infinite extent) in 3D world space. The plane is the xz-plane of the local coordinate space this transform defines.

## See Also

- [func anchor(for: SCNNode) -> ARAnchor?](arscnview/anchor(for:).md)
  Returns the AR anchor associated with the specified SceneKit node, if any.
- [func node(for: ARAnchor) -> SCNNode?](arscnview/node(for:).md)
  Returns the SceneKit node associated with the specified AR anchor, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arscnview/unprojectpoint(_:ontoplane:))*
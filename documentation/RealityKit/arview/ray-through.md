# ray(through:)

**Framework**: RealityKit  
**Kind**: method

Determines the position and direction of a ray through the given point in the 2D space of the view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+

## Declaration

```swift
@MainActor
@preconcurrency func ray(through screenPoint: CGPoint) -> (origin: SIMD3<Float>, direction: SIMD3<Float>)?
```

#### Return Value

A tuple that represents a ray in AR coordinates that goes from the camera origin through the specified point on the screen.

## Parameters

- `screenPoint`: A point in the view’s coordinate system.

## See Also

- [func project(SIMD3<Float>) -> CGPoint?](arview/project(_:).md)
  Projects a point from the 3D world coordinate system of the scene to the 2D pixel coordinate system of the view.
- [func unproject(CGPoint, ontoPlane: float4x4, relativeToCamera: Bool) -> SIMD3<Float>?](arview/unproject(_:ontoplane:relativetocamera:).md)
  Unproject a 2D point from the view onto a plane in 3D world coordinates.
- [func unproject(CGPoint, ontoPlane: float4x4) -> SIMD3<Float>?](arview/unproject(_:ontoplane:).md)
  Maps a 2D point from the view’s coordinate system onto the given plane in 3D space.
- [func unproject(CGPoint, viewport: CGRect) -> SIMD3<Float>?](arview/unproject(_:viewport:).md)
  Maps a 2D point from the pixel coordinate system of a viewport into a 3D coordinate space. The point lies on this view’s near clipping plane.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/ray(through:))*
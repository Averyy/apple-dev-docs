# unproject(_:viewport:)

**Framework**: RealityKit  
**Kind**: method

Maps a 2D point from the pixel coordinate system of a viewport into a 3D coordinate space. The point lies on this view’s near clipping plane.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency func unproject(_ point: CGPoint, viewport: CGRect) -> SIMD3<Float>?
```

#### Return Value

A view-space 3D coordinate.

## Parameters

- `point`: A point in  .
- `viewport`: A viewport.

## See Also

- [func project(SIMD3<Float>) -> CGPoint?](arview/project(_:).md)
  Projects a point from the 3D world coordinate system of the scene to the 2D pixel coordinate system of the view.
- [func unproject(CGPoint, ontoPlane: float4x4, relativeToCamera: Bool) -> SIMD3<Float>?](arview/unproject(_:ontoplane:relativetocamera:).md)
  Unproject a 2D point from the view onto a plane in 3D world coordinates.
- [func unproject(CGPoint, ontoPlane: float4x4) -> SIMD3<Float>?](arview/unproject(_:ontoplane:).md)
  Maps a 2D point from the view’s coordinate system onto the given plane in 3D space.
- [func ray(through: CGPoint) -> (origin: SIMD3<Float>, direction: SIMD3<Float>)?](arview/ray(through:).md)
  Determines the position and direction of a ray through the given point in the 2D space of the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/unproject(_:viewport:))*
# unproject(_:viewport:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

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

- `point`: A point in `viewport`.
- `viewport`: A viewport.

## See Also

### Mapping between coordinate spaces
- [func project(SIMD3<Float>) -> CGPoint?](./project%28_%29.md)
  Projects a point from the 3D world coordinate system of the scene to the 2D pixel coordinate system of the view.
- [func unproject(CGPoint, ontoPlane: float4x4, relativeToCamera: Bool) -> SIMD3<Float>?](./unproject%28_,ontoplane,relativetocamera%29.md)
  Unproject a 2D point from the view onto a plane in 3D world coordinates.
- [func unproject(CGPoint, ontoPlane: float4x4) -> SIMD3<Float>?](./unproject%28_,ontoplane%29.md)
  Maps a 2D point from the view’s coordinate system onto the given plane in 3D space.
- [func ray(through: CGPoint) -> (origin: SIMD3<Float>, direction: SIMD3<Float>)?](./ray%28through%29.md)
  Determines the position and direction of a ray through the given point in the 2D space of the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/unproject(_:viewport:))*
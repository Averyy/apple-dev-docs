# project(_:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Projects a point from the 3D world coordinate system of the scene to the 2D pixel coordinate system of the view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency func project(_ point: SIMD3<Float>) -> CGPoint?
```

#### Return Value

A point in the view’s coordinate space.

## Parameters

- `point`: The point in 3D world coordinates.

## See Also

### Mapping between coordinate spaces
- [func unproject(CGPoint, ontoPlane: float4x4, relativeToCamera: Bool) -> SIMD3<Float>?](./unproject%28_,ontoplane,relativetocamera%29.md)
  Unproject a 2D point from the view onto a plane in 3D world coordinates.
- [func unproject(CGPoint, ontoPlane: float4x4) -> SIMD3<Float>?](./unproject%28_,ontoplane%29.md)
  Maps a 2D point from the view’s coordinate system onto the given plane in 3D space.
- [func unproject(CGPoint, viewport: CGRect) -> SIMD3<Float>?](./unproject%28_,viewport%29.md)
  Maps a 2D point from the pixel coordinate system of a viewport into a 3D coordinate space. The point lies on this view’s near clipping plane.
- [func ray(through: CGPoint) -> (origin: SIMD3<Float>, direction: SIMD3<Float>)?](./ray%28through%29.md)
  Determines the position and direction of a ray through the given point in the 2D space of the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/project(_:))*
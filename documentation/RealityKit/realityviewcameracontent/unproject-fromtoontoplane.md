# unproject(_:from:to:ontoPlane:)

**Framework**: RealityKit  
**Kind**: method

Unprojects a point from the view onto a plane in 3D world coordinates.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
func unproject(_ point: CGPoint, from space: some CoordinateSpaceProtocol, to realitySpace: some RealityCoordinateSpace, ontoPlane: float4x4) -> SIMD3<Float>?
```

#### Return Value

3D position in `realitySpace`, or nil if unprojection is not possible.

#### Discussion

A 2D point in the view’s coordinate space can refer to any point along a line segment in the 3D coordinate space. Unprojecting gets the 3D position of the point along this line segment that intersects the provided plane.

> **Note**: Unprojection is not possible if the plane is parallel to the line segment, or if the view does not have a currently active camera.

Unprojection is not possible if the plane is parallel to the line segment, or if the view does not have a currently active camera.

## Parameters

- `point`: A point in the provided coordinate space.
- `space`: The 2D coordinate space in which to interpret the  .
- `realitySpace`: The 3D coordinate space in which    interprets the point.
- `planeTransform`: The transform used to define the coordinate   system of the plane relative to the scene. The coordinate   system’s positive y-axis is assumed to be the normal of the   plane.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewcameracontent/unproject(_:from:to:ontoplane:))*
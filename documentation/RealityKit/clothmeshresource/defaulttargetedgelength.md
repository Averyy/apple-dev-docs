# defaultTargetEdgeLength

**Framework**: RealityKit  
**Kind**: property  
**Role**: Type Property

Default target edge length for mesh generation.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
static let defaultTargetEdgeLength: Float
```

## Discussion

It is convenient to have the same target edge length for all shapes, since self-collision assumes similar edge lengths across the whole simulation.

## See Also

### Creating a cloth mesh
- [convenience init(positions: [SIMD3<Float>], triangleIndices: [UInt32]) throws](./init%28positions,triangleindices%29.md)
  Creates a cloth mesh resource from the given vertex positions and triangle indices.
- [static func patch(size: SIMD2<Float>, targetEdgeLength: Float) throws -> Self](./patch%28size,targetedgelength%29.md)
  Creates a rectangular patch mesh with a topology suitable for cloth simulation.
- [static func box(size: SIMD3<Float>, targetEdgeLength: Float) throws -> Self](./box%28size,targetedgelength%29.md)
  Creates a box mesh with a topology suitable for cloth simulation.
- [static func sphere(radius: Float, targetEdgeLength: Float) throws -> Self](./sphere%28radius,targetedgelength%29.md)
  Creates a sphere mesh with a topology suitable for cloth simulation.
- [static func capsule(height: Float, radius: Float, targetEdgeLength: Float) throws -> Self](./capsule%28height,radius,targetedgelength%29.md)
  Creates a capsule mesh with a topology suitable for cloth simulation.
- [static func cylinder(height: Float, radius: Float, withCaps: Bool, targetEdgeLength: Float) throws -> Self](./cylinder%28height,radius,withcaps,targetedgelength%29.md)
  Creates a cylinder mesh with a topology suitable for cloth simulation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothmeshresource/defaulttargetedgelength)*
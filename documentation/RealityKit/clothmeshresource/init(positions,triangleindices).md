# init(positions:triangleIndices:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Creates a cloth mesh resource from the given vertex positions and triangle indices.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
@MainActor
convenience init(positions: [SIMD3<Float>], triangleIndices: [UInt32]) throws
```

## Parameters

- `positions`: Positions for the vertices of the mesh.
- `triangleIndices`: Indices of the vertices forming the triangle primitives of the mesh.

## See Also

### Creating a cloth mesh
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
- [static let defaultTargetEdgeLength: Float](./defaulttargetedgelength.md)
  Default target edge length for mesh generation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothmeshresource/init(positions:triangleindices:))*
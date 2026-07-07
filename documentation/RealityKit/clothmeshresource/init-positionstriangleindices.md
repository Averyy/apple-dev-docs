# init(positions:triangleIndices:)

**Framework**: RealityKit  
**Kind**: init

Creates a cloth mesh resource from the given vertex positions and triangle indices.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
convenience init(positions: [SIMD3<Float>], triangleIndices: [UInt32]) throws
```

## Parameters

- `positions`: Positions for the vertices of the mesh.
- `triangleIndices`: Indices of the vertices forming the triangle primitives of the mesh.

## See Also

- [static func patch(size: SIMD2<Float>, targetEdgeLength: Float) throws -> Self](clothmeshresource/patch(size:targetedgelength:).md)
  Creates a rectangular patch mesh with a topology suitable for cloth simulation.
- [static func box(size: SIMD3<Float>, targetEdgeLength: Float) throws -> Self](clothmeshresource/box(size:targetedgelength:).md)
  Creates a box mesh with a topology suitable for cloth simulation.
- [static func sphere(radius: Float, targetEdgeLength: Float) throws -> Self](clothmeshresource/sphere(radius:targetedgelength:).md)
  Creates a sphere mesh with a topology suitable for cloth simulation.
- [static func capsule(height: Float, radius: Float, targetEdgeLength: Float) throws -> Self](clothmeshresource/capsule(height:radius:targetedgelength:).md)
  Creates a capsule mesh with a topology suitable for cloth simulation.
- [static func cylinder(height: Float, radius: Float, withCaps: Bool, targetEdgeLength: Float) throws -> Self](clothmeshresource/cylinder(height:radius:withcaps:targetedgelength:).md)
  Creates a cylinder mesh with a topology suitable for cloth simulation.
- [static let defaultTargetEdgeLength: Float](clothmeshresource/defaulttargetedgelength.md)
  Default target edge length for mesh generation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothmeshresource/init(positions:triangleindices:))*
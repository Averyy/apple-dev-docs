# generateConvex(from:)

**Framework**: RealityKit  
**Kind**: method

Creates a convex shape from the given mesh.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency static func generateConvex(from mesh: MeshResource) -> ShapeResource
```

#### Return Value

The new shape.

## Parameters

- `mesh`: A mesh with the shape of the convex polyhedron. Use meshes with   a small number of vertices to avoid hurting performance.

## See Also

- [static func generateConvex(from: [SIMD3<Float>]) -> ShapeResource](shaperesource/generateconvex(from:)-6q0wj.md)
  Creates a convex shape from the given points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shaperesource/generateconvex(from:)-53jm9)*
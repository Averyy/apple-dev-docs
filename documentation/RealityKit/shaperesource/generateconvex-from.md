# generateConvex(from:)

**Framework**: RealityKit  
**Kind**: method

Creates a convex shape from the given mesh.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shaperesource/generateconvex(from:))*
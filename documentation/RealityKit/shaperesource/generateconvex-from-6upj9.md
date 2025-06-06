# generateConvex(from:)

**Framework**: RealityKit  
**Kind**: method

Creates a convex shape from the given mesh.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
nonisolated
static func generateConvex(from mesh: MeshResource) async throws -> ShapeResource
```

#### Return Value

The new shape, defined by the convex hull of the vertices in `mesh`.

#### Discussion

> **Note**: Will throw an error if `mesh` does not define a nonempty convex volume.  For example, will fail if all the vertices in `mesh` are coplanar.

Will throw an error if `mesh` does not define a nonempty convex volume.  For example, will fail if all the vertices in `mesh` are coplanar.

## Parameters

- `mesh`: A mesh with the shape of the convex polyhedron. Use meshes with a small number of vertices to   avoid hurting performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shaperesource/generateconvex(from:)-6upj9)*
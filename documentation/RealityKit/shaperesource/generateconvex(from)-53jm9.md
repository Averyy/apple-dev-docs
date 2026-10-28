# generateConvex(from:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Type Method

Creates a convex shape from the given mesh.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency static func generateConvex(from mesh: MeshResource) -> ShapeResource
```

**Other overloads**:

```swift
@MainActor
@preconcurrency static func generateConvex(from points: [SIMD3<Float>]) -> ShapeResource
```

```swift
nonisolated
static func generateConvex(from mesh: MeshResource) async throws -> ShapeResource
```

```swift
nonisolated
static func generateConvex(from points: [SIMD3<Float>]) async throws -> ShapeResource
```

## Return Value

The new shape.

## Parameters

- `mesh`: A mesh with the shape of the convex polyhedron. Use meshes with a small number of vertices to avoid hurting performance.

## See Also

### Generating convex shapes
- [static func generateConvex(from: [SIMD3<Float>]) -> ShapeResource](./generateconvex%28from%29-6q0wj.md)
  Creates a convex shape from the given points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shaperesource/generateconvex(from:)-53jm9)*
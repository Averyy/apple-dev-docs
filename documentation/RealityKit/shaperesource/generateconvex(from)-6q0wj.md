# generateConvex(from:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Type Method

Creates a convex shape from the given points.

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
@preconcurrency static func generateConvex(from points: [SIMD3<Float>]) -> ShapeResource
```

**Other overloads**:

```swift
@MainActor
@preconcurrency static func generateConvex(from mesh: MeshResource) -> ShapeResource
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

- `points`: An array of 3D points that define the convex polyhedron. Keep the number of points small to avoid hurting performance.

## See Also

### Generating convex shapes
- [static func generateConvex(from: MeshResource) -> ShapeResource](./generateconvex%28from%29-53jm9.md)
  Creates a convex shape from the given mesh.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shaperesource/generateconvex(from:)-6q0wj)*
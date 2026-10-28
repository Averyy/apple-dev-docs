# generateConvex(from:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Type Method

Creates a convex shape from the given points asynchronously.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS

## Declaration

```swift
nonisolated
static func generateConvex(from points: [SIMD3<Float>]) async throws -> ShapeResource
```

**Other overloads**:

```swift
@MainActor
@preconcurrency static func generateConvex(from mesh: MeshResource) -> ShapeResource
```

```swift
@MainActor
@preconcurrency static func generateConvex(from points: [SIMD3<Float>]) -> ShapeResource
```

```swift
nonisolated
static func generateConvex(from mesh: MeshResource) async throws -> ShapeResource
```

## Return Value

A new ShapeResource object defined by the convex hull of `points`.

## Discussion

> **Throws**: Will throw an error if `points` do not define a nonempty convex volume.  For example, will fail if all of the points in `points` are coplanar.

## Parameters

- `points`: An array of 3D points that define the convex polyhedron. Keep the number of points small to avoid hurting performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shaperesource/generateconvex(from:)-1c8f6)*
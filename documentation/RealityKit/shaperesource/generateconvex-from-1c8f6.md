# generateConvex(from:)

**Framework**: Realitykit  
**Kind**: method

Creates a convex shape from the given points asynchronously.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
nonisolated
static func generateConvex(from points: [SIMD3<Float>]) async throws -> ShapeResource
```

#### Return Value

A new ShapeResource object defined by the convex hull of `points`.

#### Discussion

> **Note**: Will throw an error if `points` do not define a nonempty convex volume.  For example, will fail if all of the points in `points` are coplanar.

## Parameters

- `points`: An array of 3D points that define the convex polyhedron. Keep the number of points small to   avoid hurting performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shaperesource/generateconvex(from:)-1c8f6)*
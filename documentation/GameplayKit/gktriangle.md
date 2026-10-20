# GKTriangle

**Framework**: GameplayKit  
**Kind**: struct  
**Role**: Structure

The definition of a triangle in the mesh, available with the [`triangle(at:)`](./gkmeshgraph/triangle%28at%29.md) method.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
struct GKTriangle
```

```c
struct GKTriangle;
```

## Topics

### Initializers
- [init()](./gktriangle/init%28%29.md)
- [init(points: (vector_float3, vector_float3, vector_float3))](./gktriangle/init%28points%29.md)
### Instance Properties
- [var points: (vector_float3, vector_float3, vector_float3)](./gktriangle/points.md)
  A set of three points describing the triangle.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Constants
- [struct GKMeshGraphTriangulationMode](./gkmeshgraphtriangulationmode.md)
  Options for how to place graph nodes when generating the graph, used by the [`triangulationMode`](./gkmeshgraph/triangulationmode.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gktriangle)*
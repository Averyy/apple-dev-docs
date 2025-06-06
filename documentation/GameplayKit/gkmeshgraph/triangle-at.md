# triangle(at:)

**Framework**: GameplayKit  
**Kind**: method

The triangle definition at the specified index.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func triangle(at index: Int) -> GKTriangle
```

#### Return Value

A structure describing the specified triangle.

#### Discussion

This method provides valid results only after calling the [`triangulate()`](gkmeshgraph/triangulate().md) to create a mesh around the current configuration of obstacles. The information this method provides can be useful for drawing your own overlay UI to debug the graphs you create.

## Parameters

- `index`: An index identifying the triangle. Must be less than the value of the   property.

## See Also

- [func triangulate()](gkmeshgraph/triangulate.md)
  Creates or updates the graph with a network of nodes that describes the open space around its obstacles.
- [var triangulationMode: GKMeshGraphTriangulationMode](gkmeshgraph/triangulationmode.md)
  A set of options for how to place graph nodes when triangulating the graph.
- [var triangleCount: Int](gkmeshgraph/trianglecount.md)
  The number of triangles in the mesh.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkmeshgraph/triangle(at:))*
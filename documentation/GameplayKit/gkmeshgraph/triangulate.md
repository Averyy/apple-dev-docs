# triangulate()

**Framework**: GameplayKit  
**Kind**: method

Creates or updates the graph with a network of nodes that describes the open space around its obstacles.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func triangulate()
```

#### Discussion

The [`GKMeshGraph`](gkmeshgraph.md) class adds, removes, and arranges nodes to describe the navigable areas around obstacles  when you call this method. Typically, you add or remove several obstacles, then call the [`triangulate()`](gkmeshgraph/triangulate().md) method to update the graph. You should also call this method after changing the [`triangulationMode`](gkmeshgraph/triangulationmode.md) property.

After triangulating, the graph reflects the navigability of open space around its obstacles and can be used for any number of [`findPath(from:to:)`](gkgraph/findpath(from:to:).md) calls. Changing the list of obstacles requires retriangulating the graph.

## See Also

- [var triangulationMode: GKMeshGraphTriangulationMode](gkmeshgraph/triangulationmode.md)
  A set of options for how to place graph nodes when triangulating the graph.
- [func triangle(at: Int) -> GKTriangle](gkmeshgraph/triangle(at:).md)
  The triangle definition at the specified index.
- [var triangleCount: Int](gkmeshgraph/trianglecount.md)
  The number of triangles in the mesh.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkmeshgraph/triangulate())*
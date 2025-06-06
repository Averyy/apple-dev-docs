# removeObstacles(_:)

**Framework**: GameplayKit  
**Kind**: method

Removes the specified obstacle from the graph.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func removeObstacles(_ obstacles: [GKPolygonObstacle])
```

#### Discussion

Adding or removing obstacles does not update the graph. The [`GKMeshGraph`](gkmeshgraph.md) class adds, removes, and arranges nodes to describe the navigable areas around obstacles  when you call the [`triangulate()`](gkmeshgraph/triangulate().md) method. Typically, you add or remove several obstacles, then call the [`triangulate()`](gkmeshgraph/triangulate().md) method to update the graph.

## Parameters

- `obstacles`: An array of obstacle objects to be removed from the graph.

## See Also

- [var obstacles: [GKPolygonObstacle]](gkmeshgraph/obstacles.md)
  The list of obstacle objects in the graph, each of which describes a polygon-shaped impassable area.
- [func addObstacles([GKPolygonObstacle])](gkmeshgraph/addobstacles(_:).md)
  Adds new obstacles to the graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkmeshgraph/removeobstacles(_:))*
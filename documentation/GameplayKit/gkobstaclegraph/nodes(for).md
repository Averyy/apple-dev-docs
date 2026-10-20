# nodes(for:)

**Framework**: GameplayKit  
**Kind**: method

Returns the group of nodes corresponding to an obstacle in the graph.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func nodes(for obstacle: GKPolygonObstacle) -> [NodeType]
```

#### Return Value

An array of nodes representing the navigable points nearest to each of the obstacle’s vertices.

#### Discussion

Adding obstacles to a graph creates additional graph nodes corresponding to the navigable points nearest to each of the obstacle’s vertices. The [`GKObstacleGraph`](gkobstaclegraph.md) class automatically creates, removes, or rearranges these nodes where necessary, and automatically connects or disconnects other nodes so that no path between nodes passes through an obstacle.

## Parameters

- `obstacle`: An obstacle in the graph.

## See Also

- [var obstacles: [GKPolygonObstacle]](gkobstaclegraph/obstacles.md)
  The list of obstacle objects in the graph, each of which describes a polygon-shaped impassable area.
- [func addObstacles([GKPolygonObstacle])](gkobstaclegraph/addobstacles(_:).md)
  Adds new obstacles to the graph.
- [func removeObstacles([GKPolygonObstacle])](gkobstaclegraph/removeobstacles(_:).md)
  Removes the specified obstacle from the graph.
- [func removeAllObstacles()](gkobstaclegraph/removeallobstacles.md)
  Removes all obstacles from the graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkobstaclegraph/nodes(for:))*
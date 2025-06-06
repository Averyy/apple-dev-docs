# addObstacles(_:)

**Framework**: GameplayKit  
**Kind**: method

Adds new obstacles to the graph.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func addObstacles(_ obstacles: [GKPolygonObstacle])
```

#### Discussion

Adding a new obstacle to the graph has the same effect as if that obstacle were present when creating the graph—that is, the [`GKObstacleGraph`](gkobstaclegraph.md) class automatically creates new nodes and edges where necessary to describe the navigable area around the complete collection of obstacles.

## Parameters

- `obstacles`: An array of obstacle objects to be added to the graph.

## See Also

- [var obstacles: [GKPolygonObstacle]](gkobstaclegraph/obstacles.md)
  The list of obstacle objects in the graph, each of which describes a polygon-shaped impassable area.
- [func removeObstacles([GKPolygonObstacle])](gkobstaclegraph/removeobstacles(_:).md)
  Removes the specified obstacle from the graph.
- [func removeAllObstacles()](gkobstaclegraph/removeallobstacles.md)
  Removes all obstacles from the graph.
- [func nodes(for: GKPolygonObstacle) -> [NodeType]](gkobstaclegraph/nodes(for:).md)
  Returns the group of nodes corresponding to an obstacle in the graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkobstaclegraph/addobstacles(_:))*
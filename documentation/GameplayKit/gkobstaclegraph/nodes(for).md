# nodes(for:)

**Framework**: GameplayKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (NSArray<GKGraphNode2D *> *) nodesForObstacle:(GKPolygonObstacle *) obstacle;
```

## Return Value

An array of nodes representing the navigable points nearest to each of the obstacle’s vertices.

## Discussion

Adding obstacles to a graph creates additional graph nodes corresponding to the navigable points nearest to each of the obstacle’s vertices. The [`GKObstacleGraph`](../gkobstaclegraph.md) class automatically creates, removes, or rearranges these nodes where necessary, and automatically connects or disconnects other nodes so that no path between nodes passes through an obstacle.

## Parameters

- `obstacle`: An obstacle in the graph.

## See Also

### Working with Obstacles
- [var obstacles: [GKPolygonObstacle]](./obstacles.md)
  The list of obstacle objects in the graph, each of which describes a polygon-shaped impassable area.
- [func addObstacles([GKPolygonObstacle])](./addobstacles%28_%29.md)
  Adds new obstacles to the graph.
- [func removeObstacles([GKPolygonObstacle])](./removeobstacles%28_%29.md)
  Removes the specified obstacle from the graph.
- [func removeAllObstacles()](./removeallobstacles%28%29.md)
  Removes all obstacles from the graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkobstaclegraph/nodes(for:))*
# removeObstacles(_:)

**Framework**: GameplayKit  
**Kind**: method  
**Role**: Instance Method

Removes the specified obstacle from the graph.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func removeObstacles(_ obstacles: [GKPolygonObstacle])
```

```objc
- (void) removeObstacles:(NSArray<GKPolygonObstacle *> *) obstacles;
```

## Discussion

After removing obstacles, the [`GKObstacleGraph`](../gkobstaclegraph.md) class automatically creates, removes, or rearranges nodes and edges where necessary to describe the navigable area around the complete collection of obstacles.

## Parameters

- `obstacles`: An array of obstacle objects to be removed from the graph.

## See Also

### Working with Obstacles
- [var obstacles: [GKPolygonObstacle]](./obstacles.md)
  The list of obstacle objects in the graph, each of which describes a polygon-shaped impassable area.
- [func addObstacles([GKPolygonObstacle])](./addobstacles%28_%29.md)
  Adds new obstacles to the graph.
- [func removeAllObstacles()](./removeallobstacles%28%29.md)
  Removes all obstacles from the graph.
- [func nodes(for: GKPolygonObstacle) -> [NodeType]](./nodes%28for%29.md)
  Returns the group of nodes corresponding to an obstacle in the graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkobstaclegraph/removeobstacles(_:))*
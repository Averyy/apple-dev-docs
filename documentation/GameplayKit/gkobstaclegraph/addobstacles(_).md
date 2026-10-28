# addObstacles(_:)

**Framework**: GameplayKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) addObstacles:(NSArray<GKPolygonObstacle *> *) obstacles;
```

## Discussion

Adding a new obstacle to the graph has the same effect as if that obstacle were present when creating the graph—that is, the [`GKObstacleGraph`](../gkobstaclegraph.md) class automatically creates new nodes and edges where necessary to describe the navigable area around the complete collection of obstacles.

## Parameters

- `obstacles`: An array of obstacle objects to be added to the graph.

## See Also

### Working with Obstacles
- [var obstacles: [GKPolygonObstacle]](./obstacles.md)
  The list of obstacle objects in the graph, each of which describes a polygon-shaped impassable area.
- [func removeObstacles([GKPolygonObstacle])](./removeobstacles%28_%29.md)
  Removes the specified obstacle from the graph.
- [func removeAllObstacles()](./removeallobstacles%28%29.md)
  Removes all obstacles from the graph.
- [func nodes(for: GKPolygonObstacle) -> [NodeType]](./nodes%28for%29.md)
  Returns the group of nodes corresponding to an obstacle in the graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkobstaclegraph/addobstacles(_:))*
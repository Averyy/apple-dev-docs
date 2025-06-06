# obstacles

**Framework**: GameplayKit  
**Kind**: property

The list of obstacle objects in the graph, each of which describes a polygon-shaped impassable area.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var obstacles: [GKPolygonObstacle] { get }
```

## See Also

- [func addObstacles([GKPolygonObstacle])](gkobstaclegraph/addobstacles(_:).md)
  Adds new obstacles to the graph.
- [func removeObstacles([GKPolygonObstacle])](gkobstaclegraph/removeobstacles(_:).md)
  Removes the specified obstacle from the graph.
- [func removeAllObstacles()](gkobstaclegraph/removeallobstacles.md)
  Removes all obstacles from the graph.
- [func nodes(for: GKPolygonObstacle) -> [NodeType]](gkobstaclegraph/nodes(for:).md)
  Returns the group of nodes corresponding to an obstacle in the graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkobstaclegraph/obstacles)*
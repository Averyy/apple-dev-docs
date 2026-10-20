# obstacles

**Framework**: GameplayKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly, nonnull) NSArray<GKPolygonObstacle *> * obstacles;
```

## See Also

### Working with Obstacles
- [func addObstacles([GKPolygonObstacle])](./addobstacles%28_%29.md)
  Adds new obstacles to the graph.
- [func removeObstacles([GKPolygonObstacle])](./removeobstacles%28_%29.md)
  Removes the specified obstacle from the graph.
- [func removeAllObstacles()](./removeallobstacles%28%29.md)
  Removes all obstacles from the graph.
- [func nodes(for: GKPolygonObstacle) -> [NodeType]](./nodes%28for%29.md)
  Returns the group of nodes corresponding to an obstacle in the graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkobstaclegraph/obstacles)*
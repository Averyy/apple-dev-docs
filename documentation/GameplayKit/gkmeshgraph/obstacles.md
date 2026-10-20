# obstacles

**Framework**: GameplayKit  
**Kind**: property  
**Role**: Instance Property

The list of obstacle objects in the graph, each of which describes a polygon-shaped impassable area.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkmeshgraph/obstacles)*
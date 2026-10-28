# addObstacles(_:)

**Framework**: GameplayKit  
**Kind**: method  
**Role**: Instance Method

Adds new obstacles to the graph.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func addObstacles(_ obstacles: [GKPolygonObstacle])
```

```objc
- (void) addObstacles:(NSArray<GKPolygonObstacle *> *) obstacles;
```

## Discussion

Adding or removing obstacles does not update the graph. The [`GKMeshGraph`](../gkmeshgraph.md) class adds, removes, and arranges nodes to describe the navigable areas around obstacles *only* when you call the [`triangulate()`](./triangulate%28%29.md) method. Typically, you add or remove several obstacles, then call the [`triangulate()`](./triangulate%28%29.md) method to update the graph.

## Parameters

- `obstacles`: An array of obstacle objects to be added to the graph.

## See Also

### Working with Obstacles
- [var obstacles: [GKPolygonObstacle]](./obstacles.md)
  The list of obstacle objects in the graph, each of which describes a polygon-shaped impassable area.
- [func removeObstacles([GKPolygonObstacle])](./removeobstacles%28_%29.md)
  Removes the specified obstacle from the graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkmeshgraph/addobstacles(_:))*
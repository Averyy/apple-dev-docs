# init(obstacles:bufferRadius:)

**Framework**: GameplayKit  
**Kind**: init

Initializes a graph with the specified list of obstacles.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(obstacles: [GKPolygonObstacle], bufferRadius: Float)
```

#### Return Value

A new obstacle graph.

#### Discussion

This method generates a graph that can be traversed in all directions, except into the areas occupied by obstacles.

Use the `bufferRadius` parameter to take the size of potential travelers into account when determining navigability. For example, if a game character that will use pathfinding has a radius of 20 units (in the same coordinate space you use to define obstacles), specify a buffer radius of 20. As a result, the graph will consider any points within 20 units of an obstacle non-navigable—that is, pathfinding in the graph will not result in any positions that lie inside this buffer region, so you can safely set the character’s center point to the location of a node returned from the [`findPath(from:to:)`](gkgraph/findpath(from:to:).md) method without the character overlapping any obstacles.

This initializer is equivalent to the [`init(obstacles:bufferRadius:nodeClass:)`](gkobstaclegraph/init(obstacles:bufferradius:nodeclass:).md) initializer, but uses the default [`GKGraphNode2D`](gkgraphnode2d.md) node class.

## Parameters

- `obstacles`: An array of obstacle objects, each of which describes a polygon-shaped impassable area.
- `bufferRadius`: The distance from obstacle edges that should also be considered impassable.

## See Also

- [init(obstacles: [GKPolygonObstacle], bufferRadius: Float, nodeClass: AnyClass)](gkobstaclegraph/init(obstacles:bufferradius:nodeclass:).md)
  Initializes a graph with the specified list of obstacles, using the specified node class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkobstaclegraph/init(obstacles:bufferradius:))*
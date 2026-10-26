# graphWithObstacles:bufferRadius:nodeClass:

**Framework**: GameplayKit  
**Kind**: method  
**Role**: Type Method

Creates a graph with the specified list of obstacles, using the specified node class.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```objc
+ (instancetype) graphWithObstacles:(NSArray<GKPolygonObstacle *> *) obstacles bufferRadius:(float) bufferRadius nodeClass:(Class) nodeClass;
```

#### Return Value

A new obstacle graph.

#### Discussion

This method generates a graph that can be traversed in all directions, except into the areas occupied by obstacles.

Use the `bufferRadius` parameter to take the size of potential travelers into account when determining navigability. For example, if a game character that will use pathfinding has a radius of 20 units (in the same coordinate space you use to define obstacles), specify a buffer radius of 20. As a result, the graph will consider any points within 20 units of an obstacle non-navigable—that is, pathfinding in the graph will not result in any positions that lie inside this buffer region, so you can safely set the character’s center point to the location of a node returned from the [`findPath(from:to:)`](../gkgraph/findpath%28from,to%29.md) method without the character overlapping any obstacles.

Use the `nodeClass` parameter to create a graph using a custom subclass of [`GKGraphNode2D`](../gkgraphnode2d.md). For example, your custom node class might override the [`cost(to:)`](../gkgraphnode/cost%28to%29.md) method so that some nodes are more costly than others to travel through. Pathfinding in such a graph would favor indirect routes when a direct route has a higher cost.

## Parameters

- `obstacles`: An array of obstacle objects, each of which describes a polygon-shaped impassable area.
- `bufferRadius`: The distance from obstacle edges that should also be considered impassable.
- `nodeClass`: The [`GKGraphNode2D`](../gkgraphnode2d.md) subclass to use for nodes in the graph.

## See Also

### Creating a Graph
- [init(obstacles: [GKPolygonObstacle], bufferRadius: Float, nodeClass: AnyClass)](./init%28obstacles,bufferradius,nodeclass%29.md)
  Initializes a graph with the specified list of obstacles, using the specified node class.
- [init(obstacles: [GKPolygonObstacle], bufferRadius: Float)](./init%28obstacles,bufferradius%29.md)
  Initializes a graph with the specified list of obstacles.
- [+ graphWithObstacles:bufferRadius:](./graphwithobstacles_bufferradius_.md)
  Creates a graph with the specified list of obstacles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkobstaclegraph/graphwithobstacles:bufferradius:nodeclass:)*
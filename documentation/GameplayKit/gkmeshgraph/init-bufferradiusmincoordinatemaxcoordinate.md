# init(bufferRadius:minCoordinate:maxCoordinate:)

**Framework**: GameplayKit  
**Kind**: init

Initializes a graph to cover the specified area.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
init(bufferRadius: Float, minCoordinate min: vector_float2, maxCoordinate max: vector_float2)
```

#### Return Value

A new mesh graph.

#### Discussion

A newly created graph contains no obstacles and no graph nodes. First, use the [`addObstacles(_:)`](gkmeshgraph/addobstacles(_:).md) method to add obstacles. Next, use the [`triangulate()`](gkmeshgraph/triangulate().md) method to fill the open space between obstacles with a web of graph nodes, allowing pathfinding operations to result in smooth paths around obstacles.

Use the `bufferRadius` parameter to take the size of potential travelers into account when determining navigability. For example, if a game character that will use pathfinding has a radius of 20 units (in the same coordinate space you use to define obstacles), specify a buffer radius of 20. As a result, the graph will consider any points within 20 units of an obstacle non-navigable—that is, pathfinding in the graph will not result in any positions that lie inside this buffer region, so you can safely set the character’s center point to the location of a node returned from the [`findPath(from:to:)`](gkgraph/findpath(from:to:).md) method without the character overlapping any obstacles.

## Parameters

- `bufferRadius`: The distance from obstacle edges that should also be considered impassable.
- `min`: The minimum coordinate of the space to be covered by the graph.
- `max`: The maximum coordinate of the space to be covered by the graph.

## See Also

- [init(bufferRadius: Float, minCoordinate: vector_float2, maxCoordinate: vector_float2, nodeClass: AnyClass)](gkmeshgraph/init(bufferradius:mincoordinate:maxcoordinate:nodeclass:).md)
  Initializes a graph to cover the specified area, using the specified node class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkmeshgraph/init(bufferradius:mincoordinate:maxcoordinate:))*
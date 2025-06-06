# connectUsingObstacles(node:ignoring:)

**Framework**: GameplayKit  
**Kind**: method

Adds the specified node to the graph, connecting it to its nearest neighbors while ignoring the area occupied by the specified obstacles.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func connectUsingObstacles(node: NodeType, ignoring obstaclesToIgnore: [GKPolygonObstacle])
```

#### Discussion

The [`GKObstacleGraph`](gkobstaclegraph.md) class automatically maintains a network of nodes that describes the navigable areas around its collection of obstacles. Adding a new node to the graph connects it to these nodes, such that the resulting network can be used to find paths around the obstacles to the position of the new node. GameplayKit adds new connections only if those connections do not represent a path through any obstacles (or through the buffer region around them, as specified by the [`bufferRadius`](gkobstaclegraph/bufferradius.md) property.)

Call this method when you need to to connect a node to the graph without taking certain obstacles into account. For example, you might add a node representing the destination for a game character to move toward, but place that node inside an existing obstacle, so that the resulting path gets the character as near to that obstacle as possible.

## Parameters

- `node`: A graph node object containing 2D coordinate information.
- `obstaclesToIgnore`: An array of obstacles to be ignored when adding the node to the graph.

## See Also

- [func connectUsingObstacles(node: NodeType)](gkobstaclegraph/connectusingobstacles(node:).md)
  Adds the specified node to the graph, connecting it to its nearest neighbors without creating connections that pass through obstacles or their buffer regions.
- [func connectUsingObstacles(node: NodeType, ignoringBufferRadiusOf: [GKPolygonObstacle])](gkobstaclegraph/connectusingobstacles(node:ignoringbufferradiusof:).md)
  Adds the specified node to the graph, connecting it to its nearest neighbors while ignoring the buffer regions around the specified obstacles.
- [var bufferRadius: Float](gkobstaclegraph/bufferradius.md)
  The distance from obstacle edges that should also be considered impassable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkobstaclegraph/connectusingobstacles(node:ignoring:))*
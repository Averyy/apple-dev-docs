# connectUsingObstacles(node:)

**Framework**: GameplayKit  
**Kind**: method

Adds the specified node to the graph, connecting it to its nearest neighbors without creating connections that pass through obstacles or their buffer regions.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func connectUsingObstacles(node: NodeType)
```

#### Discussion

The [`GKObstacleGraph`](gkobstaclegraph.md) class automatically maintains a network of nodes that describes the navigable areas around its collection of obstacles. Adding a new node to the graph connects it to these nodes, such that the resulting network can be used to find paths around the obstacles to the position of the new node. GameplayKit adds new connections only if those connections do not represent a path through any obstacles (or through the buffer region around them, as specified by the [`bufferRadius`](gkobstaclegraph/bufferradius.md) property.)

Calling this method is equivalent to calling the [`connectUsingObstacles(node:ignoring:)`](gkobstaclegraph/connectusingobstacles(node:ignoring:).md) and passing an empty array for the `obstaclesToIgnore` parameter.

## Parameters

- `node`: A graph node object containing 2D coordinate information.

## See Also

- [func connectUsingObstacles(node: NodeType, ignoring: [GKPolygonObstacle])](gkobstaclegraph/connectusingobstacles(node:ignoring:).md)
  Adds the specified node to the graph, connecting it to its nearest neighbors while ignoring the area occupied by the specified obstacles.
- [func connectUsingObstacles(node: NodeType, ignoringBufferRadiusOf: [GKPolygonObstacle])](gkobstaclegraph/connectusingobstacles(node:ignoringbufferradiusof:).md)
  Adds the specified node to the graph, connecting it to its nearest neighbors while ignoring the buffer regions around the specified obstacles.
- [var bufferRadius: Float](gkobstaclegraph/bufferradius.md)
  The distance from obstacle edges that should also be considered impassable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkobstaclegraph/connectusingobstacles(node:))*
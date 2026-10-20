# connectUsingObstacles(node:)

**Framework**: GameplayKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) connectNodeUsingObstacles:(NodeType) node;
```

#### Discussion

The [`GKObstacleGraph`](../gkobstaclegraph.md) class automatically maintains a network of nodes that describes the navigable areas around its collection of obstacles. Adding a new node to the graph connects it to these nodes, such that the resulting network can be used to find paths around the obstacles to the position of the new node. GameplayKit adds new connections only if those connections do not represent a path through any obstacles (or through the buffer region around them, as specified by the [`bufferRadius`](./bufferradius.md) property.)

Calling this method is equivalent to calling the [`connectUsingObstacles(node:ignoring:)`](./connectusingobstacles%28node,ignoring%29.md) and passing an empty array for the `obstaclesToIgnore` parameter.

## Parameters

- `node`: A graph node object containing 2D coordinate information.

## See Also

### Working with Nodes
- [func connectUsingObstacles(node: NodeType, ignoring: [GKPolygonObstacle])](./connectusingobstacles%28node,ignoring%29.md)
  Adds the specified node to the graph, connecting it to its nearest neighbors while ignoring the area occupied by the specified obstacles.
- [func connectUsingObstacles(node: NodeType, ignoringBufferRadiusOf: [GKPolygonObstacle])](./connectusingobstacles%28node,ignoringbufferradiusof%29.md)
  Adds the specified node to the graph, connecting it to its nearest neighbors while ignoring the buffer regions around the specified obstacles.
- [var bufferRadius: Float](./bufferradius.md)
  The distance from obstacle edges that should also be considered impassable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkobstaclegraph/connectusingobstacles(node:))*
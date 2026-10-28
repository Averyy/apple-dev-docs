# bufferRadius

**Framework**: GameplayKit  
**Kind**: property  
**Role**: Instance Property

The distance from obstacle edges that should also be considered impassable.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var bufferRadius: Float { get }
```

```objc
@property (nonatomic, readonly) float bufferRadius;
```

## Discussion

You set this property when creating a graph with the [`init(obstacles:bufferRadius:)`](./init%28obstacles,bufferradius%29.md) initializer. Use the `bufferRadius` initializer parameter to take the size of potential travelers into account when determining navigability. After initialization, you can use this property to examine the buffer radius the graph was created with—for example, to draw a debugging overlay in your game UI that indicates passable and impassable areas.

## See Also

### Working with Nodes
- [func connectUsingObstacles(node: NodeType)](./connectusingobstacles%28node%29.md)
  Adds the specified node to the graph, connecting it to its nearest neighbors without creating connections that pass through obstacles or their buffer regions.
- [func connectUsingObstacles(node: NodeType, ignoring: [GKPolygonObstacle])](./connectusingobstacles%28node,ignoring%29.md)
  Adds the specified node to the graph, connecting it to its nearest neighbors while ignoring the area occupied by the specified obstacles.
- [func connectUsingObstacles(node: NodeType, ignoringBufferRadiusOf: [GKPolygonObstacle])](./connectusingobstacles%28node,ignoringbufferradiusof%29.md)
  Adds the specified node to the graph, connecting it to its nearest neighbors while ignoring the buffer regions around the specified obstacles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkobstaclegraph/bufferradius)*
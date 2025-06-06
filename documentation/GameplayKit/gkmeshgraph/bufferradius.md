# bufferRadius

**Framework**: GameplayKit  
**Kind**: property

The distance from obstacle edges that should also be considered impassable.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var bufferRadius: Float { get }
```

#### Discussion

You set this property when creating a graph with the [`init(bufferRadius:minCoordinate:maxCoordinate:)`](gkmeshgraph/init(bufferradius:mincoordinate:maxcoordinate:).md) or [`init(bufferRadius:minCoordinate:maxCoordinate:nodeClass:)`](gkmeshgraph/init(bufferradius:mincoordinate:maxcoordinate:nodeclass:).md) initializer. Use the `bufferRadius` initializer parameter to take the size of potential travelers into account when determining navigability. After initialization, you can use this property to examine the buffer radius the graph was created with—for example, to draw a debugging overlay in your game UI that indicates passable and impassable areas.

## See Also

- [func connectUsingObstacles(node: NodeType)](gkmeshgraph/connectusingobstacles(node:).md)
  Adds the specified node to the graph, connecting it to its nearest neighbors without creating connections that pass through obstacles or their buffer regions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkmeshgraph/bufferradius)*
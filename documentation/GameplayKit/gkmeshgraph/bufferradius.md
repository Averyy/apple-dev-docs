# bufferRadius

**Framework**: GameplayKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) float bufferRadius;
```

#### Discussion

You set this property when creating a graph with the [`init(bufferRadius:minCoordinate:maxCoordinate:)`](./init%28bufferradius,mincoordinate,maxcoordinate%29.md) or [`init(bufferRadius:minCoordinate:maxCoordinate:nodeClass:)`](./init%28bufferradius,mincoordinate,maxcoordinate,nodeclass%29.md) initializer. Use the `bufferRadius` initializer parameter to take the size of potential travelers into account when determining navigability. After initialization, you can use this property to examine the buffer radius the graph was created with—for example, to draw a debugging overlay in your game UI that indicates passable and impassable areas.

## See Also

### Working with Nodes
- [func connectUsingObstacles(node: NodeType)](./connectusingobstacles%28node%29.md)
  Adds the specified node to the graph, connecting it to its nearest neighbors without creating connections that pass through obstacles or their buffer regions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkmeshgraph/bufferradius)*
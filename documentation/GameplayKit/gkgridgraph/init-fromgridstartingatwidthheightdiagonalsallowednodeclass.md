# init(fromGridStartingAt:width:height:diagonalsAllowed:nodeClass:)

**Framework**: GameplayKit  
**Kind**: init

Initializes a graph that describes an integer grid with the specified dimensions, using the specified node class.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(fromGridStartingAt position: vector_int2, width: Int32, height: Int32, diagonalsAllowed: Bool, nodeClass: AnyClass)
```

#### Return Value

A new grid graph.

#### Discussion

Use the `nodeClass` parameter to create a graph using a custom subclass of [`GKGridGraphNode`](gkgridgraphnode.md). For example, your custom node class might override the [`cost(to:)`](gkgraphnode/cost(to:).md) method so that some nodes are more costly than others to travel through. Pathfinding in such a graph would favor indirect routes when a direct route has a higher cost.

All connections created through this method are bidirectional.

For more information, see [`GameplayKit Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

## Parameters

- `position`: The lowest x- and y-coordinates to appear in the grid.
- `width`: The number of possible x-coordinates in the grid.
- `height`: The number of possible y-coordinates in the grid.
- `diagonalsAllowed`:   to connect nodes in the grid to their diagonal neighbors;   to connect nodes only to their horizontal and vertical neighbors.
- `nodeClass`: The   subclass to use for nodes in the graph.

## See Also

- [init(fromGridStartingAt: vector_int2, width: Int32, height: Int32, diagonalsAllowed: Bool)](gkgridgraph/init(fromgridstartingat:width:height:diagonalsallowed:).md)
  Initializes a graph that describes an integer grid with the specified dimensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkgridgraph/init(fromgridstartingat:width:height:diagonalsallowed:nodeclass:))*
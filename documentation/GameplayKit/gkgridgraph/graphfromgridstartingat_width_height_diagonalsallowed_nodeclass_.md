# graphFromGridStartingAt:width:height:diagonalsAllowed:nodeClass:

**Framework**: GameplayKit  
**Kind**: method  
**Role**: Type Method

Creates a graph that describes an integer grid with the specified dimensions, using the specified node class.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```objc
+ (instancetype) graphFromGridStartingAt:(vector_int2) position width:(int) width height:(int) height diagonalsAllowed:(BOOL) diagonalsAllowed nodeClass:(Class) nodeClass;
```

## Return Value

A new grid graph.

## Discussion

Use the `nodeClass` parameter to create a graph using a custom subclass of [`GKGridGraphNode`](../gkgridgraphnode.md). For example, your custom node class might override the [`cost(to:)`](../gkgraphnode/cost%28to%29.md) method so that some nodes are more costly than others to travel through. Pathfinding in such a graph would favor indirect routes when a direct route has a higher cost.

All connections created through this method are bidirectional.

## Parameters

- `position`: The lowest x- and y-coordinates to appear in the grid.
- `width`: The number of possible x-coordinates in the grid.
- `height`: The number of possible y-coordinates in the grid.
- `diagonalsAllowed`: [`true`](../../Swift/true.md) to connect nodes in the grid to their diagonal neighbors; [`false`](../../Swift/false.md) to connect nodes only to their horizontal and vertical neighbors.
- `nodeClass`: The [`GKGridGraphNode`](../gkgridgraphnode.md) subclass to use for nodes in the graph.

## See Also

### Creating a Graph
- [init(fromGridStartingAt: vector_int2, width: Int32, height: Int32, diagonalsAllowed: Bool, nodeClass: AnyClass)](./init%28fromgridstartingat,width,height,diagonalsallowed,nodeclass%29.md)
  Initializes a graph that describes an integer grid with the specified dimensions, using the specified node class.
- [init(fromGridStartingAt: vector_int2, width: Int32, height: Int32, diagonalsAllowed: Bool)](./init%28fromgridstartingat,width,height,diagonalsallowed%29.md)
  Initializes a graph that describes an integer grid with the specified dimensions.
- [+ graphFromGridStartingAt:width:height:diagonalsAllowed:](./graphfromgridstartingat_width_height_diagonalsallowed_.md)
  Creates a graph that describes an integer grid with the specified dimensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkgridgraph/graphfromgridstartingat:width:height:diagonalsallowed:nodeclass:)*
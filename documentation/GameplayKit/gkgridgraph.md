# GKGridGraph

**Framework**: GameplayKit  
**Kind**: class

A navigation graph for 2D game worlds where movement is constrained to an integer grid.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class GKGridGraph<NodeType> where NodeType : GKGridGraphNode
```

#### Overview

Use this class to generate a graph containing [`GKGridGraphNode`](gkgridgraphnode.md) objects representing a specified grid. Then use methods of the superclass [`GKGraph`](gkgraph.md) to find routes through the graph.

To learn more about graphs and pathfinding, see [`Pathfinding`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/Pathfinding.html#//apple_ref/doc/uid/TP40015172-CH3) in [`GameplayKit Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

## Topics

### Creating a Graph
- [init(fromGridStartingAt: vector_int2, width: Int32, height: Int32, diagonalsAllowed: Bool, nodeClass: AnyClass)](gkgridgraph/init(fromgridstartingat:width:height:diagonalsallowed:nodeclass:).md)
  Initializes a graph that describes an integer grid with the specified dimensions, using the specified node class.
- [init(fromGridStartingAt: vector_int2, width: Int32, height: Int32, diagonalsAllowed: Bool)](gkgridgraph/init(fromgridstartingat:width:height:diagonalsallowed:).md)
  Initializes a graph that describes an integer grid with the specified dimensions.
### Working with Nodes
- [func node(atGridPosition: vector_int2) -> NodeType?](gkgridgraph/node(atgridposition:).md)
  Returns the node in the graph at the specified grid coordinates.
- [func connectToAdjacentNodes(node: GKGridGraphNode)](gkgridgraph/connecttoadjacentnodes(node:).md)
  Adds the specified node to the graph, connecting it to its nearest neighbors in the grid.
### Inspecting a Graph
- [var diagonalsAllowed: Bool](gkgridgraph/diagonalsallowed.md)
  A Boolean value that indicates whether nodes in the grid are connected to their diagonal neighbors.
- [var gridOrigin: vector_int2](gkgridgraph/gridorigin.md)
  The lowest x- and y-coordinates that appear in the grid.
- [var gridWidth: Int](gkgridgraph/gridwidth.md)
  The number of possible x-coordinates in the grid.
- [var gridHeight: Int](gkgridgraph/gridheight.md)
  The number of possible y-coordinates in the grid.
### Instance Methods
- [func classForGenericArgument(at: Int) -> AnyClass](gkgridgraph/classforgenericargument(at:).md)

## Relationships

### Inherits From
- [GKGraph](gkgraph.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class GKGraph](gkgraph.md)
  A collection of nodes that describes the navigability of a game world and provides  methods to search for routes through that space.
- [class GKObstacleGraph](gkobstaclegraph.md)
  A navigation graph for 2D game worlds that creates a minimal network for precise pathfinding around obstacles.
- [class GKMeshGraph](gkmeshgraph.md)
  A navigation graph for 2D game worlds that creates a space-filling network for smooth pathfinding around obstacles.
- [class GKGraphNode](gkgraphnode.md)
  A single node in a navigation graph for use in pathfinding.
- [class GKGraphNode2D](gkgraphnode2d.md)
  A node in a navigation graph, associated with a point in continuous 2D space.
- [class GKGraphNode3D](gkgraphnode3d.md)
  A node in a navigation graph, associated with a point in continuous 3D space.
- [class GKGridGraphNode](gkgridgraphnode.md)
  A node in a navigation graph, associated with a position on a discrete two-dimensional grid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkgridgraph)*
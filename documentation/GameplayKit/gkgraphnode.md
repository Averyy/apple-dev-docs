# GKGraphNode

**Framework**: GameplayKit  
**Kind**: class

A single node in a navigation graph for use in pathfinding.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class GKGraphNode
```

#### Overview

A set of connected nodes form a graph that describes the navigability of a game world. Use graph nodes together with a [`GKGraph`](gkgraph.md) object (or one of its subclasses) to perform actions that relate to the network of nodes as a whole, such as pathfinding to determine routes through the network.

This class describes the general features of graph nodes, but does not contain geometry information that relates the graph to a game world. You can construct a graph with this class or any of its subclasses:

- On its own, the [`GKGraphNode`](gkgraphnode.md) class is useful for worlds such as board games, where the connections between nodes are important but their spatial position has no effect on gameplay.
- Create [`GKGridGraphNode`](gkgridgraphnode.md) objects (for use with the [`GKGridGraph`](gkgridgraph.md) class) to model worlds where movement is constrained to a two-dimensional integer grid.
- Create [`GKGraphNode2D`](gkgraphnode2d.md) objects to model worlds that allow full freedom of movement in a two-dimensional plane. Use these nodes together with the [`GKObstacleGraph`](gkobstaclegraph.md) or [`GKMeshGraph`](gkmeshgraph.md) class to create graphs that route around impassable obstacles.
- Create [`GKGraphNode3D`](gkgraphnode3d.md) objects to model worlds that allow full freedom of movement in three-dimensional space.

To learn more about graphs and pathfinding, see [`Pathfinding`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/Pathfinding.html#//apple_ref/doc/uid/TP40015172-CH3) in [`GameplayKit Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

## Topics

### Working with Connections
- [var connectedNodes: [GKGraphNode]](gkgraphnode/connectednodes.md)
  The list of other nodes connected to this node.
- [func addConnections(to: [GKGraphNode], bidirectional: Bool)](gkgraphnode/addconnections(to:bidirectional:).md)
  Connects this node to all nodes in the specified list.
- [func removeConnections(to: [GKGraphNode], bidirectional: Bool)](gkgraphnode/removeconnections(to:bidirectional:).md)
  Removes the connections from this node to the specified nodes.
### Computing Traversal Costs
- [func cost(to: GKGraphNode) -> Float](gkgraphnode/cost(to:).md)
  Returns the cost to travel from this node to the specified, directly connected, node.
- [func estimatedCost(to: GKGraphNode) -> Float](gkgraphnode/estimatedcost(to:).md)
  Returns an underestimate of the cost of travel from this node to the specified node.
### Finding Paths
- [func findPath(to: GKGraphNode) -> [GKGraphNode]](gkgraphnode/findpath(to:).md)
  Computes and returns a sequence of nodes that represents the lowest-cost graph traversal from this node to the specified node.
- [func findPath(from: GKGraphNode) -> [GKGraphNode]](gkgraphnode/findpath(from:).md)
  Computes and returns a sequence of nodes that represents the lowest-cost graph traversal from the specified node to this node.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [GKGraphNode2D](gkgraphnode2d.md)
- [GKGraphNode3D](gkgraphnode3d.md)
- [GKGridGraphNode](gkgridgraphnode.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class GKGraph](gkgraph.md)
  A collection of nodes that describes the navigability of a game world and provides  methods to search for routes through that space.
- [class GKObstacleGraph](gkobstaclegraph.md)
  A navigation graph for 2D game worlds that creates a minimal network for precise pathfinding around obstacles.
- [class GKMeshGraph](gkmeshgraph.md)
  A navigation graph for 2D game worlds that creates a space-filling network for smooth pathfinding around obstacles.
- [class GKGridGraph](gkgridgraph.md)
  A navigation graph for 2D game worlds where movement is constrained to an integer grid.
- [class GKGraphNode2D](gkgraphnode2d.md)
  A node in a navigation graph, associated with a point in continuous 2D space.
- [class GKGraphNode3D](gkgraphnode3d.md)
  A node in a navigation graph, associated with a point in continuous 3D space.
- [class GKGridGraphNode](gkgridgraphnode.md)
  A node in a navigation graph, associated with a position on a discrete two-dimensional grid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkgraphnode)*
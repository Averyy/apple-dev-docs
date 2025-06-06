# GKGraph

**Framework**: GameplayKit  
**Kind**: class

A collection of nodes that describes the navigability of a game world and provides  methods to search for routes through that space.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class GKGraph
```

#### Overview

Individual nodes in a graph represent discrete locations that a character or other object in your game can occupy, and the connections between adjacent nodes represent the ability of a game entity to travel from one location to another. Use the [`GKGraph`](gkgraph.md) class to create a general graph, or the [`GKGridGraph`](gkgridgraph.md), [`GKObstacleGraph`](gkobstaclegraph.md), or [`GKMeshGraph`](gkmeshgraph.md) subclass to generate specialized graphs that contain more information about the geometry of your game world.

Each set of graph and node classes can generate graphs for different kinds of spaces:

- The base classes [`GKGraph`](gkgraph.md) and [`GKGraphNode`](gkgraphnode.md) contain functionality general to all graphs and nodes. You can also use these classes on their own to construct graphs that contain no geometry information. This option is useful for games where the connections between spaces are more important than their physical locations, such as board games.
- Use the [`GKGridGraph`](gkgridgraph.md) and [`GKGridGraphNode`](gkgridgraphnode.md) classes to describe game worlds that constrain movement to an integer grid, such as tactical role-playing games.
- Use the [`GKObstacleGraph`](gkobstaclegraph.md) or [`GKMeshGraph`](gkmeshgraph.md) class to describe 2D game worlds that allow continuous movement in open spaces that are interrupted by impassable obstacles ([`GKPolygonObstacle`](gkpolygonobstacle.md) objects). Obstacle graphs automatically generate nodes containing 2D point information ([`GKGraphNode2D`](gkgraphnode2d.md) objects), and you can also add your own such nodes representing locations of interest.

The graphs modeled by this class are always —that is, a connection between two nodes describes one direction of travel between them. To enable travel between two nodes in either direction, you must create a connection in each direction. You can choose to connect both directions at once with the [`connectToLowestCostNode(node:bidirectional:)`](gkgraph/connecttolowestcostnode(node:bidirectional:).md) method (for graphs) or the addConnection:bidirectional: method (for nodes).

Using a graph for pathfinding typically involves three major steps:

1. Create a graph once (for example, when initializing a game level class) with static information about your game world.
2. When you need to find a route between points, connect temporary nodes to the graph at those points. Use the [`connectToLowestCostNode(node:bidirectional:)`](gkgraph/connecttolowestcostnode(node:bidirectional:).md) method to connect nodes using their own geometry information, or the [`connectUsingObstacles(node:)`](gkobstaclegraph/connectusingobstacles(node:).md) or [`connectToAdjacentNodes(node:)`](gkgridgraph/connecttoadjacentnodes(node:).md) method to use the additional constraints of obstacle and grid graphs.
3. Call the [`findPath(from:to:)`](gkgraph/findpath(from:to:).md) method to find a route between locations in the graph. This method returns an array of graph nodes, starting with the requested start point of the path, and proceeding to adjacent nodes in order until it reaches the requested end point. Use the geometry information contained in each node to make use of the route—for example, in a SpriteKit game you might create a sequence of move actions to move a character from point to point along the path.
4. The temporary nodes you created for finding a path typically have little usefulness after a path has been found. Remove those nodes before reusing the graph for future searches.

To learn more about graphs and pathfinding, see [`Pathfinding`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/Pathfinding.html#//apple_ref/doc/uid/TP40015172-CH3) in [`GameplayKit Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

## Topics

### Creating a Graph
- [init([GKGraphNode])](gkgraph/init(_:).md)
  Initializes a graph with the specified list of nodes.
### Working with Nodes in a Graph
- [func add([GKGraphNode])](gkgraph/add(_:).md)
  Adds the specified nodes to the graph.
- [func connectToLowestCostNode(node: GKGraphNode, bidirectional: Bool)](gkgraph/connecttolowestcostnode(node:bidirectional:).md)
  Adds a node to the graph, connecting it to the node already in the graph for which the connection has the lowest cost.
- [func remove([GKGraphNode])](gkgraph/remove(_:).md)
  Removes the specified nodes from the graph.
- [var nodes: [GKGraphNode]?](gkgraph/nodes.md)
  The list of nodes in the graph.
### Pathfinding with a Graph
- [func findPath(from: GKGraphNode, to: GKGraphNode) -> [GKGraphNode]](gkgraph/findpath(from:to:).md)
  Computes and returns a sequence of nodes that represents the shortest traversal of the graph between the specified nodes.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [GKGridGraph](gkgridgraph.md)
- [GKMeshGraph](gkmeshgraph.md)
- [GKObstacleGraph](gkobstaclegraph.md)
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

- [class GKObstacleGraph](gkobstaclegraph.md)
  A navigation graph for 2D game worlds that creates a minimal network for precise pathfinding around obstacles.
- [class GKMeshGraph](gkmeshgraph.md)
  A navigation graph for 2D game worlds that creates a space-filling network for smooth pathfinding around obstacles.
- [class GKGridGraph](gkgridgraph.md)
  A navigation graph for 2D game worlds where movement is constrained to an integer grid.
- [class GKGraphNode](gkgraphnode.md)
  A single node in a navigation graph for use in pathfinding.
- [class GKGraphNode2D](gkgraphnode2d.md)
  A node in a navigation graph, associated with a point in continuous 2D space.
- [class GKGraphNode3D](gkgraphnode3d.md)
  A node in a navigation graph, associated with a point in continuous 3D space.
- [class GKGridGraphNode](gkgridgraphnode.md)
  A node in a navigation graph, associated with a position on a discrete two-dimensional grid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkgraph)*
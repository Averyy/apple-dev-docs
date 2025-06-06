# GKObstacleGraph

**Framework**: GameplayKit  
**Kind**: class

A navigation graph for 2D game worlds that creates a minimal network for precise pathfinding around obstacles.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class GKObstacleGraph<NodeType> where NodeType : GKGraphNode2D
```

#### Overview

You create an obstacle graph with a collection of [`GKObstacle`](gkobstacle.md) objects. To use the graph for pathfinding, you add [`GKGraphNode2D`](gkgraphnode2d.md) objects representing points of interest (such as the current position of a game character and the location it needs to find a route to). Then use methods of the superclass [`GKGraph`](gkgraph.md) to find routes through the graph.

Unlike the related [`GKMeshGraph`](gkmeshgraph.md) class, an obstacle graph creates a minimal network of graph nodes, resulting in paths that are efficient but not smooth.

To learn more about graphs and pathfinding, see [`Pathfinding`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/Pathfinding.html#//apple_ref/doc/uid/TP40015172-CH3) in [`GameplayKit Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

## Topics

### Creating a Graph
- [init(obstacles: [GKPolygonObstacle], bufferRadius: Float, nodeClass: AnyClass)](gkobstaclegraph/init(obstacles:bufferradius:nodeclass:).md)
  Initializes a graph with the specified list of obstacles, using the specified node class.
- [init(obstacles: [GKPolygonObstacle], bufferRadius: Float)](gkobstaclegraph/init(obstacles:bufferradius:).md)
  Initializes a graph with the specified list of obstacles.
### Working with Obstacles
- [var obstacles: [GKPolygonObstacle]](gkobstaclegraph/obstacles.md)
  The list of obstacle objects in the graph, each of which describes a polygon-shaped impassable area.
- [func addObstacles([GKPolygonObstacle])](gkobstaclegraph/addobstacles(_:).md)
  Adds new obstacles to the graph.
- [func removeObstacles([GKPolygonObstacle])](gkobstaclegraph/removeobstacles(_:).md)
  Removes the specified obstacle from the graph.
- [func removeAllObstacles()](gkobstaclegraph/removeallobstacles.md)
  Removes all obstacles from the graph.
- [func nodes(for: GKPolygonObstacle) -> [NodeType]](gkobstaclegraph/nodes(for:).md)
  Returns the group of nodes corresponding to an obstacle in the graph.
### Working with Nodes
- [func connectUsingObstacles(node: NodeType)](gkobstaclegraph/connectusingobstacles(node:).md)
  Adds the specified node to the graph, connecting it to its nearest neighbors without creating connections that pass through obstacles or their buffer regions.
- [func connectUsingObstacles(node: NodeType, ignoring: [GKPolygonObstacle])](gkobstaclegraph/connectusingobstacles(node:ignoring:).md)
  Adds the specified node to the graph, connecting it to its nearest neighbors while ignoring the area occupied by the specified obstacles.
- [func connectUsingObstacles(node: NodeType, ignoringBufferRadiusOf: [GKPolygonObstacle])](gkobstaclegraph/connectusingobstacles(node:ignoringbufferradiusof:).md)
  Adds the specified node to the graph, connecting it to its nearest neighbors while ignoring the buffer regions around the specified obstacles.
- [var bufferRadius: Float](gkobstaclegraph/bufferradius.md)
  The distance from obstacle edges that should also be considered impassable.
### Locking Node Connections
- [func lockConnection(from: NodeType, to: NodeType)](gkobstaclegraph/lockconnection(from:to:).md)
  Prevents the specified nodes from being disconnected due to the addition of obstacles.
- [func unlockConnection(from: NodeType, to: NodeType)](gkobstaclegraph/unlockconnection(from:to:).md)
  Allows the specified nodes to be disconnected due to the addition of obstacles.
- [func isConnectionLocked(from: NodeType, to: NodeType) -> Bool](gkobstaclegraph/isconnectionlocked(from:to:).md)
  Returns a Boolean value indicating whether the specified nodes are protected from disconnection due to the addition of obstacles.
### Instance Methods
- [func classForGenericArgument(at: Int) -> AnyClass](gkobstaclegraph/classforgenericargument(at:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkobstaclegraph)*
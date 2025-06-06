# GKGraphNode2D

**Framework**: GameplayKit  
**Kind**: class

A node in a navigation graph, associated with a point in continuous 2D space.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class GKGraphNode2D
```

#### Overview

Together, a network of nodes form a graph that describes the navigability of a game world. Use graph nodes with a [`GKGraph`](gkgraph.md), [`GKObstacleGraph`](gkobstaclegraph.md), or [`GKMeshGraph`](gkmeshgraph.md) object to perform actions that relate to the network of nodes as a whole, such as pathfinding to determine routes through the network.

When you use the [`GKObstacleGraph`](gkobstaclegraph.md) or [`GKMeshGraph`](gkmeshgraph.md) class to describe a game world in terms of open spaces interrupted by obstacles, GameplayKit automatically creates and manages [`GKGraphNode2D`](gkgraphnode2d.md) instances that represent positions along possible paths that navigate around those obstacles.

To learn more about graphs and pathfinding, see [`Pathfinding`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/Pathfinding.html#//apple_ref/doc/uid/TP40015172-CH3) in [`GameplayKit Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

## Topics

### Creating a Graph Node
- [init(point: vector_float2)](gkgraphnode2d/init(point:).md)
  Initializes a graph node with the specified point.
- [class func node(withPoint: vector_float2) -> Self](gkgraphnode2d/node(withpoint:).md)
  Creates a graph node with the specified point.
### Inspecting a Node’s Position
- [var position: vector_float2](gkgraphnode2d/position.md)
  The position of the node in continuous 2D space.

## Relationships

### Inherits From
- [GKGraphNode](gkgraphnode.md)
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
- [class GKGraphNode](gkgraphnode.md)
  A single node in a navigation graph for use in pathfinding.
- [class GKGraphNode3D](gkgraphnode3d.md)
  A node in a navigation graph, associated with a point in continuous 3D space.
- [class GKGridGraphNode](gkgridgraphnode.md)
  A node in a navigation graph, associated with a position on a discrete two-dimensional grid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkgraphnode2d)*
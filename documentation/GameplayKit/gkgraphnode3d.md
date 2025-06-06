# GKGraphNode3D

**Framework**: GameplayKit  
**Kind**: class

A node in a navigation graph, associated with a point in continuous 3D space.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class GKGraphNode3D
```

#### Overview

Together, a network of nodes form a graph that describes the navigability of a game world. Use graph nodes with a [`GKGraph`](gkgraph.md) object to perform actions that relate to the network of nodes as a whole, such as pathfinding to determine routes through the network.

To learn more about graphs and pathfinding, see [`Pathfinding`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/Pathfinding.html#//apple_ref/doc/uid/TP40015172-CH3) in [`GameplayKit Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

## Topics

### Creating a Graph Node
- [init(point: vector_float3)](gkgraphnode3d/init(point:).md)
  Initializes a graph node with the specified point.
- [class func node(withPoint: vector_float3) -> Self](gkgraphnode3d/node(withpoint:).md)
  Creates a graph node with the specified point.
### Inspecting a Node’s Position
- [var position: vector_float3](gkgraphnode3d/position.md)
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
- [class GKGraphNode2D](gkgraphnode2d.md)
  A node in a navigation graph, associated with a point in continuous 2D space.
- [class GKGridGraphNode](gkgridgraphnode.md)
  A node in a navigation graph, associated with a position on a discrete two-dimensional grid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkgraphnode3d)*
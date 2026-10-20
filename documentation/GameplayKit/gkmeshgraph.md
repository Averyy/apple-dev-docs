# GKMeshGraph

**Framework**: GameplayKit  
**Kind**: class  
**Role**: Class

A navigation graph for 2D game worlds that creates a space-filling network for smooth pathfinding around obstacles.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class GKMeshGraph<NodeType> where NodeType : GKGraphNode2D
```

```objc
@interface GKMeshGraph : GKGraph
```

#### Overview

To use a mesh graph for pathfinding, add a collection of [`GKObstacle`](./gkobstacle.md) objects representing impassable areas and [`GKGraphNode2D`](./gkgraphnode2d.md) objects representing points of interest (such as the current position of a game character and the location it needs to find a route to). Then use methods of the superclass [`GKGraph`](./gkgraph.md) to find routes through the graph.

Unlike the related [`GKObstacleGraph`](./gkobstaclegraph.md) class, a mesh graph creates a space-filling network of graph nodes, resulting in paths that are smooth but not the most efficient.

To learn more about graphs and pathfinding, see [Pathfinding](https://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/Pathfinding.html#//apple_ref/doc/uid/TP40015172-CH3) in [GameplayKit Programming Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

## Topics

### Creating a Graph
- [init(bufferRadius: Float, minCoordinate: vector_float2, maxCoordinate: vector_float2, nodeClass: AnyClass)](./gkmeshgraph/init%28bufferradius,mincoordinate,maxcoordinate,nodeclass%29.md)
  Initializes a graph to cover the specified area, using the specified node class.
- [init(bufferRadius: Float, minCoordinate: vector_float2, maxCoordinate: vector_float2)](./gkmeshgraph/init%28bufferradius,mincoordinate,maxcoordinate%29.md)
  Initializes a graph to cover the specified area.
### Working with Obstacles
- [var obstacles: [GKPolygonObstacle]](./gkmeshgraph/obstacles.md)
  The list of obstacle objects in the graph, each of which describes a polygon-shaped impassable area.
- [func addObstacles([GKPolygonObstacle])](./gkmeshgraph/addobstacles%28_%29.md)
  Adds new obstacles to the graph.
- [func removeObstacles([GKPolygonObstacle])](./gkmeshgraph/removeobstacles%28_%29.md)
  Removes the specified obstacle from the graph.
### Working with Nodes
- [func connectUsingObstacles(node: NodeType)](./gkmeshgraph/connectusingobstacles%28node%29.md)
  Adds the specified node to the graph, connecting it to its nearest neighbors without creating connections that pass through obstacles or their buffer regions.
- [var bufferRadius: Float](./gkmeshgraph/bufferradius.md)
  The distance from obstacle edges that should also be considered impassable.
### Managing the Mesh
- [func triangulate()](./gkmeshgraph/triangulate%28%29.md)
  Creates or updates the graph with a network of nodes that describes the open space around its obstacles.
- [var triangulationMode: GKMeshGraphTriangulationMode](./gkmeshgraph/triangulationmode.md)
  A set of options for how to place graph nodes when triangulating the graph.
- [func triangle(at: Int) -> GKTriangle](./gkmeshgraph/triangle%28at%29.md)
  The triangle definition at the specified index.
- [var triangleCount: Int](./gkmeshgraph/trianglecount.md)
  The number of triangles in the mesh.
### Constants
- [struct GKMeshGraphTriangulationMode](./gkmeshgraphtriangulationmode.md)
  Options for how to place graph nodes when generating the graph, used by the [`triangulationMode`](./gkmeshgraph/triangulationmode.md) property.
- [struct GKTriangle](./gktriangle.md)
  The definition of a triangle in the mesh, available with the [`triangle(at:)`](./gkmeshgraph/triangle%28at%29.md) method.
### Instance Methods
- [func classForGenericArgument(at: Int) -> AnyClass](./gkmeshgraph/classforgenericargument%28at%29.md)
### Initializers
- [convenience init(nodes: [GKGraphNode])](./gkmeshgraph/init%28nodes%29.md)

## Relationships

### Inherits From
- [GKGraph](./gkgraph.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Pathfinding
- [class GKGraph](./gkgraph.md)
  A collection of nodes that describes the navigability of a game world and provides *pathfinding* methods to search for routes through that space.
- [class GKObstacleGraph](./gkobstaclegraph.md)
  A navigation graph for 2D game worlds that creates a minimal network for precise pathfinding around obstacles.
- [class GKGridGraph](./gkgridgraph.md)
  A navigation graph for 2D game worlds where movement is constrained to an integer grid.
- [class GKGraphNode](./gkgraphnode.md)
  A single node in a navigation graph for use in pathfinding.
- [class GKGraphNode2D](./gkgraphnode2d.md)
  A node in a navigation graph, associated with a point in continuous 2D space.
- [class GKGraphNode3D](./gkgraphnode3d.md)
  A node in a navigation graph, associated with a point in continuous 3D space.
- [class GKGridGraphNode](./gkgridgraphnode.md)
  A node in a navigation graph, associated with a position on a discrete two-dimensional grid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkmeshgraph)*
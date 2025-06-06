# init(graphNodes:radius:)

**Framework**: GameplayKit  
**Kind**: init

Initializes a path using the positions of the specified graph nodes.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(graphNodes: [GKGraphNode], radius: Float)
```

#### Return Value

A new path object.

#### Discussion

Use this initializer to turn a list of nodes from a navigation graph (as returned by the [`GKGraph`](gkgraph.md) [`findPath(from:to:)`](gkgraph/findpath(from:to:).md) method) into a path-following goal for an agent. If the nodes are [`GKGraphNode2D`](gkgraphnode2d.md) objects, this initializer creates a 2D path; if the nodes are [`GKGraphNode3D`](gkgraphnode3d.md) objects, this initializer creates a 3D path.

The `radius` parameter defines the space occupied by the path—think of this space as the area created by sweeping a circle (or sphere, for 3D paths) of the specified radius along the path from vertex to vertex. Agents with path-related goals will attempt to move to or stay within this area.

To use the newly created path to constrain an agent’s behavior, create a goal with the [`init(toStayOn:maxPredictionTime:)`](gkgoal/init(tostayon:maxpredictiontime:).md) or [`init(toFollow:maxPredictionTime:forward:)`](gkgoal/init(tofollow:maxpredictiontime:forward:).md) method.

## Parameters

- `graphNodes`: An array of graph node objects containing 2D points.
- `radius`: The radius of the path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkpath/init(graphnodes:radius:))*
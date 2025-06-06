# GKPath

**Framework**: Gameplaykit  
**Kind**: class

A polygonal path that can be followed by an agent.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class GKPath
```

#### Overview

To make an agent move to or stay within the area defined by a path, create a goal with the [`init(toStayOn:maxPredictionTime:)`](gkgoal/init(tostayon:maxpredictiontime:).md) method; to make an agent traverse along a path, create a goal with the [`init(toFollow:maxPredictionTime:forward:)`](gkgoal/init(tofollow:maxpredictiontime:forward:).md) method.

A path can be expressed as a sequence of either 2D points or 3D points. Use the former to create paths for use by [`GKAgent2D`](gkagent2d.md) objects, and the latter to create paths for [`GKAgent3D`](gkagent3d.md) objects to follow.

> **Note**:  The coordinate system in which you express the path’s vertices and radius is arbitrary; you may choose how to map agent positions and sizes into your game scene. It often makes sense to use the same coordinate system as your game engine—for example, when using agents in a SpriteKit-based game, you’d typically specify a path in screen points.

To learn more about using goals and agents, see [`Agents, Goals, and Behaviors`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/Agent.html#//apple_ref/doc/uid/TP40015172-CH8) in [`GameplayKit Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

## Topics

### Creating a Path
- [init(graphNodes: [GKGraphNode], radius: Float)](gkpath/init(graphnodes:radius:).md)
  Initializes a path using the positions of the specified graph nodes.
### Managing a Path’s Attributes
- [var radius: Float](gkpath/radius.md)
  The radius of the path.
- [var isCyclical: Bool](gkpath/iscyclical.md)
  A Boolean value that determines whether the path loops around on itself (that is, the path’s end point connects to its start point).
### Inspecting a Path’s Shape
- [var numPoints: Int](gkpath/numpoints.md)
  The number of vertices in the path.
- [func float2(at: Int) -> vector_float2](gkpath/float2(at:).md)
  Returns the 2D point at the specified index in the path’s list of vertices.
- [func float3(at: Int) -> vector_float3](gkpath/float3(at:).md)
  Returns the 3D point at the specified index in the path’s list of vertices.
- [func point(at: Int) -> vector_float2](gkpath/point(at:).md)
  Returns the 2D point at the specified index in the path’s list of vertices.
### Initializers
- [convenience init(points: [SIMD3<Float>], radius: Float, cyclical: Bool)](gkpath/init(points:radius:cyclical:)-6qqn4.md)
- [convenience init(points: [SIMD2<Float>], radius: Float, cyclical: Bool)](gkpath/init(points:radius:cyclical:)-2iv4v.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class GKAgent](gkagent.md)
  A component that moves a game entity according to a set of goals and realistic constraints.
- [class GKAgent2D](gkagent2d.md)
  An agent that operates in a two-dimensional space.
- [class GKAgent3D](gkagent3d.md)
  An agent that operates in a three-dimensional space.
- [class GKGoal](gkgoal.md)
  An influence that motivates the movement of one or more agents.
- [class GKBehavior](gkbehavior.md)
  A set of goals that together influence the movement of an agent.
- [class GKCompositeBehavior](gkcompositebehavior.md)
  A set of behaviors, each of which is a set of goals, that together influence the movement of an agent.
- [protocol GKAgentDelegate](gkagentdelegate.md)
  Implement this protocol to synchronize the state of an agent with its visual representation in your game.


---

*[View on Apple Developer](https://developer.apple.com/documentation/GameplayKit/gkpath)*
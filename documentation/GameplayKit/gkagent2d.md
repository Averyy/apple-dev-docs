# GKAgent2D

**Framework**: GameplayKit  
**Kind**: class

An agent that operates in a two-dimensional space.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class GKAgent2D
```

#### Overview

Agents are game entities that move according to realistic constraints and whose behavior is determined by goals that motivate movement. The general functionality of an agent is defined by the abstract superclass [`GKAgent`](gkagent.md); however, you use instances of the [`GKAgent2D`](gkagent2d.md) class to implement agent-based gameplay in a 2D game (or in a 3D game where gameplay-relevant movement is restricted to two dimensions).

To learn more about using goals and agents, see [`Agents, Goals, and Behaviors`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/Agent.html#//apple_ref/doc/uid/TP40015172-CH8) in [`GameplayKit Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

## Topics

### Managing an Agent’s Position and Orientation
- [var position: vector_float2](gkagent2d/position.md)
  The current position of the agent in 2D space.
- [var rotation: Float](gkagent2d/rotation.md)
  The rotation of the agent around the z-axis.
### Running the Agent Simulation
- [func update(deltaTime: TimeInterval)](gkagent2d/update(deltatime:).md)
  Causes the agent to evaluate its goals and update its position, rotation, and velocity accordingly.
- [var velocity: vector_float2](gkagent2d/velocity.md)
  The current velocity of the agent in 2D space.

## Relationships

### Inherits From
- [GKAgent](gkagent.md)
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

- [class GKAgent](gkagent.md)
  A component that moves a game entity according to a set of goals and realistic constraints.
- [class GKAgent3D](gkagent3d.md)
  An agent that operates in a three-dimensional space.
- [class GKGoal](gkgoal.md)
  An influence that motivates the movement of one or more agents.
- [class GKBehavior](gkbehavior.md)
  A set of goals that together influence the movement of an agent.
- [class GKCompositeBehavior](gkcompositebehavior.md)
  A set of behaviors, each of which is a set of goals, that together influence the movement of an agent.
- [class GKPath](gkpath.md)
  A polygonal path that can be followed by an agent.
- [protocol GKAgentDelegate](gkagentdelegate.md)
  Implement this protocol to synchronize the state of an agent with its visual representation in your game.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkagent2d)*
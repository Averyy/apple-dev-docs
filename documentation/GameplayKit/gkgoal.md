# GKGoal

**Framework**: GameplayKit  
**Kind**: class

An influence that motivates the movement of one or more agents.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class GKGoal
```

#### Overview

Goals can motivate agents ([`GKAgent`](gkagent.md) objects) to actions such as moving toward a target, following a path, or staying aligned with a group of other agents. To give an agent one or more goals, combine those goals in a [`GKBehavior`](gkbehavior.md) object (which includes weights for the relative influence of each goal) and assign that object to the agent’s [`behavior`](gkagent/behavior.md) property.

Each time an agent’s [`update(deltaTime:)`](gkcomponent/update(deltatime:).md) method runs, the agent evaluates each goal in its behavior to find the change in direction and speed necessary to move toward fulfilling that goal (within the limits of the time delta and the agent’s maximum speed and turn rate). It then combines the effects from all the goals in its behavior, using the weights in the behavior to modulate the influence of each goal, to produce a total change in its direction and speed.

To learn more about using goals and agents, see [`Agents, Goals, and Behaviors`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/Agent.html#//apple_ref/doc/uid/TP40015172-CH8) in [`GameplayKit Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

## Topics

### Creating Goals for General Movement Behavior
- [convenience init(toSeekAgent: GKAgent)](gkgoal/init(toseekagent:).md)
  Creates a goal whose effect is to move an agent toward the current position of the specified other agent.
- [convenience init(toFleeAgent: GKAgent)](gkgoal/init(tofleeagent:).md)
  Creates a goal whose effect is to move an agent away from the current position of the specified other agent.
- [convenience init(toReachTargetSpeed: Float)](gkgoal/init(toreachtargetspeed:).md)
  Creates a goal whose effect is to accelerate or decelerate an agent until it reaches the specified speed.
- [convenience init(toWander: Float)](gkgoal/init(towander:).md)
  Creates a goal whose effect is to make an agent wander aimlessly, moving forward and turning at random.
### Creating Goals for Avoidance and Interception Behavior
- [convenience init(toAvoid: [GKAgent], maxPredictionTime: TimeInterval)](gkgoal/init(toavoid:maxpredictiontime:)-96a0i.md)
  Creates a goal whose effect is to make an agent avoid colliding with the specified other agents, taking into account the other agents’ movement.
- [convenience init(toAvoid: [GKObstacle], maxPredictionTime: TimeInterval)](gkgoal/init(toavoid:maxpredictiontime:)-7oslq.md)
  Creates a goal whose effect is to make an agent avoid colliding with the specified static obstacles.
- [convenience init(toInterceptAgent: GKAgent, maxPredictionTime: TimeInterval)](gkgoal/init(tointerceptagent:maxpredictiontime:).md)
  Creates a goal whose effect is to make an agent pursue the specified other agent, taking into account the target’s movement.
### Creating Goals for Flocking Behavior
- [convenience init(toSeparateFrom: [GKAgent], maxDistance: Float, maxAngle: Float)](gkgoal/init(toseparatefrom:maxdistance:maxangle:).md)
  Creates a goal whose effect is to make an agent maintain the specified distance from other agents in a specified group.
- [convenience init(toAlignWith: [GKAgent], maxDistance: Float, maxAngle: Float)](gkgoal/init(toalignwith:maxdistance:maxangle:).md)
  Creates a goal whose effect is to make an agent align its orientation with that of other agents in a specified group.
- [convenience init(toCohereWith: [GKAgent], maxDistance: Float, maxAngle: Float)](gkgoal/init(tocoherewith:maxdistance:maxangle:).md)
  Creates a goal whose effect is to make an agent stay near the other agents in a specified group.
### Creating Goals for Path-Following Behavior
- [convenience init(toStayOn: GKPath, maxPredictionTime: TimeInterval)](gkgoal/init(tostayon:maxpredictiontime:).md)
  Creates a goal whose effect is to maintain an agent’s position within the specified path.
- [convenience init(toFollow: GKPath, maxPredictionTime: TimeInterval, forward: Bool)](gkgoal/init(tofollow:maxpredictiontime:forward:).md)
  Creates a goal whose effect is to both maintain position on and traverse the specified path.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class GKAgent](gkagent.md)
  A component that moves a game entity according to a set of goals and realistic constraints.
- [class GKAgent2D](gkagent2d.md)
  An agent that operates in a two-dimensional space.
- [class GKAgent3D](gkagent3d.md)
  An agent that operates in a three-dimensional space.
- [class GKBehavior](gkbehavior.md)
  A set of goals that together influence the movement of an agent.
- [class GKCompositeBehavior](gkcompositebehavior.md)
  A set of behaviors, each of which is a set of goals, that together influence the movement of an agent.
- [class GKPath](gkpath.md)
  A polygonal path that can be followed by an agent.
- [protocol GKAgentDelegate](gkagentdelegate.md)
  Implement this protocol to synchronize the state of an agent with its visual representation in your game.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkgoal)*
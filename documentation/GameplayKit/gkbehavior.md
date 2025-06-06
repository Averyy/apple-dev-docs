# GKBehavior

**Framework**: GameplayKit  
**Kind**: class

A set of goals that together influence the movement of an agent.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class GKBehavior
```

#### Overview

By combining multiple goals ([`GKGoal`](gkgoal.md) objects) you can create complex behavior, such as groups of agents  ([`GKAgent`](gkagent.md) objects) that move together naturally. To assign a set of goals to an agent, use its [`behavior`](gkagent/behavior.md) property.

To learn more about using goals and agents, see [`Agents, Goals, and Behaviors`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/Agent.html#//apple_ref/doc/uid/TP40015172-CH8) in [`GameplayKit Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

## Topics

### Creating a Behavior
- [convenience init(goal: GKGoal, weight: Float)](gkbehavior/init(goal:weight:).md)
  Creates a behavior with a single goal.
- [convenience init(goals: [GKGoal])](gkbehavior/init(goals:).md)
  Creates a behavior with the specified goals.
- [convenience init(goals: [GKGoal], andWeights: [NSNumber])](gkbehavior/init(goals:andweights:).md)
  Creates a behavior with the specified goals and weights.
- [convenience init(weightedGoals: [GKGoal : NSNumber])](gkbehavior/init(weightedgoals:).md)
  Creates a behavior with the specified mapping of goals to their weights.
### Managing a Behavior’s Set of Goals
- [func setWeight(Float, for: GKGoal)](gkbehavior/setweight(_:for:).md)
  Sets the weight for the specified goal’s influence on agents, adding that goal to the behavior if not already present.
- [func weight(for: GKGoal) -> Float](gkbehavior/weight(for:).md)
  Returns the weight for the specified goal’s influence on agents.
- [func remove(GKGoal)](gkbehavior/remove(_:).md)
  Removes the specified goal from the behavior.
- [func removeAllGoals()](gkbehavior/removeallgoals.md)
  Removes all goals from the behavior.
- [var goalCount: Int](gkbehavior/goalcount.md)
  The number of goals in the behavior.
### Working with Goals Using Subscript Syntax
- [subscript(GKGoal) -> NSNumber!](gkbehavior/subscript(_:)-2yvko.md)
  Returns the weight associated with the goal specified by subscript syntax.
- [subscript(Int) -> GKGoal](gkbehavior/subscript(_:)-997a9.md)
  Returns the goal at the specified index in the behavior’s list of goals.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [GKCompositeBehavior](gkcompositebehavior.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSFastEnumeration](../Foundation/NSFastEnumeration.md)
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
- [class GKCompositeBehavior](gkcompositebehavior.md)
  A set of behaviors, each of which is a set of goals, that together influence the movement of an agent.
- [class GKPath](gkpath.md)
  A polygonal path that can be followed by an agent.
- [protocol GKAgentDelegate](gkagentdelegate.md)
  Implement this protocol to synchronize the state of an agent with its visual representation in your game.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkbehavior)*
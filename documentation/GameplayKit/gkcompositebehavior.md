# GKCompositeBehavior

**Framework**: GameplayKit  
**Kind**: class

A set of behaviors, each of which is a set of goals, that together influence the movement of an agent.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class GKCompositeBehavior
```

#### Overview

By composing [`GKGoal`](gkgoal.md) objects into subgroups ([`GKBehavior`](gkbehavior.md) objects) and composing those behaviors into composite behaviors, you can control certain aspects of a [`GKAgent`](gkagent.md) object’s movement in concert. To assign a behavior to an agent, use its [`behavior`](gkagent/behavior.md) property.

For example, you might create a behavior for a set of agents to stay together as a flock (with cohesion, alignment, and separation goals) while loosely following a path. With a single [`GKBehavior`](gkbehavior.md) object, whenever you want to change the importance of the flocking goals relative to the path-following goals, you’d need to individually change the weight of each goal. With a composite behavior, you can adjust the relative influence of a group of goals together, as in the following code.

After constructing this behavior, you can use the [`setWeight(_:for:)`](gkcompositebehavior/setweight(_:for:).md) method to increase or decrease the influence of the `flock` and `meanderOnPath` behaviors relative to one another.

To learn more about using goals and agents, see [`Agents, Goals, and Behaviors`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/Agent.html#//apple_ref/doc/uid/TP40015172-CH8) in [`GameplayKit Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

## Topics

### Creating a Composite Behavior
- [convenience init(behaviors: [GKBehavior])](gkcompositebehavior/init(behaviors:).md)
  Creates a composite behavior from the specified individual behaviors.
- [convenience init(behaviors: [GKBehavior], andWeights: [NSNumber])](gkcompositebehavior/init(behaviors:andweights:).md)
  Creates a behavior with the specified behaviors and weights.
### Managing the Individual Behaviors in a Composite Behavior
- [func setWeight(Float, for: GKBehavior)](gkcompositebehavior/setweight(_:for:).md)
  Sets the weight for the specified individual behavior’s influence on agents, adding that behavior to the composite behavior if it is not already present.
- [func weight(for: GKBehavior) -> Float](gkcompositebehavior/weight(for:).md)
  Returns the weight for the specified individual behavior’s influence on agents.
- [func remove(GKBehavior)](gkcompositebehavior/remove(_:).md)
  Removes the specified individual behavior from the composite behavior.
- [func removeAllBehaviors()](gkcompositebehavior/removeallbehaviors.md)
  Removes all individual behaviors from the composite behavior.
- [var behaviorCount: Int](gkcompositebehavior/behaviorcount.md)
  The number of individual behaviors in the composite behavior.
### Working with Behaviors Using Subscript Syntax
- [subscript(GKBehavior) -> NSNumber](gkcompositebehavior/subscript(_:)-6jng9.md)
  Returns the weight associated with the behavior specified by subscript syntax.
- [subscript(Int) -> GKBehavior](gkcompositebehavior/subscript(_:)-6krdg.md)
  Returns the individual behavior at the specified index in the composite behavior’s list of behaviors.

## Relationships

### Inherits From
- [GKBehavior](gkbehavior.md)
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
- [class GKBehavior](gkbehavior.md)
  A set of goals that together influence the movement of an agent.
- [class GKPath](gkpath.md)
  A polygonal path that can be followed by an agent.
- [protocol GKAgentDelegate](gkagentdelegate.md)
  Implement this protocol to synchronize the state of an agent with its visual representation in your game.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkcompositebehavior)*
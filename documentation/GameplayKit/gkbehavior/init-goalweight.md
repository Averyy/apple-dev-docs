# init(goal:weight:)

**Framework**: GameplayKit  
**Kind**: init

Creates a behavior with a single goal.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(goal: GKGoal, weight: Float)
```

#### Return Value

A new behavior object. To assign a set of goals to an agent, use its [`behavior`](gkagent/behavior.md) property.

#### Discussion

For more information, see [`GameplayKit Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

## Parameters

- `goal`: A goal object.
- `weight`: A weight to be applied to the goal’s influence on an agent’s speed and direction.

## See Also

- [convenience init(goals: [GKGoal])](gkbehavior/init(goals:).md)
  Creates a behavior with the specified goals.
- [convenience init(goals: [GKGoal], andWeights: [NSNumber])](gkbehavior/init(goals:andweights:).md)
  Creates a behavior with the specified goals and weights.
- [convenience init(weightedGoals: [GKGoal : NSNumber])](gkbehavior/init(weightedgoals:).md)
  Creates a behavior with the specified mapping of goals to their weights.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkbehavior/init(goal:weight:))*
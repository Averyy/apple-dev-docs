# init(goals:)

**Framework**: GameplayKit  
**Kind**: init

Creates a behavior with the specified goals.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(goals: [GKGoal])
```

#### Return Value

A new behavior object. To assign a set of goals to an agent, use its [`behavior`](gkagent/behavior.md) property.

#### Discussion

The new behavior contains the specified goals, each with a weight of `1.0`. To change a goal’s weight after creating the behavior, keep a reference to that goal and use the [`setWeight(_:for:)`](gkbehavior/setweight(_:for:).md) method.

## Parameters

- `goals`: An array of goal objects.

## See Also

- [convenience init(goal: GKGoal, weight: Float)](gkbehavior/init(goal:weight:).md)
  Creates a behavior with a single goal.
- [convenience init(goals: [GKGoal], andWeights: [NSNumber])](gkbehavior/init(goals:andweights:).md)
  Creates a behavior with the specified goals and weights.
- [convenience init(weightedGoals: [GKGoal : NSNumber])](gkbehavior/init(weightedgoals:).md)
  Creates a behavior with the specified mapping of goals to their weights.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkbehavior/init(goals:))*
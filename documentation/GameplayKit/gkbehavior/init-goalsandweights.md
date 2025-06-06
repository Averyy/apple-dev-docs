# init(goals:andWeights:)

**Framework**: GameplayKit  
**Kind**: init

Creates a behavior with the specified goals and weights.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(goals: [GKGoal], andWeights weights: [NSNumber])
```

#### Return Value

A new behavior object. To assign a set of goals to an agent, use its [`behavior`](gkagent/behavior.md) property.

## Parameters

- `goals`: An array of goal objects.
- `weights`: An array of numbers, each the weight to be applied to the goal at the corresponding index in the   array.

## See Also

- [convenience init(goal: GKGoal, weight: Float)](gkbehavior/init(goal:weight:).md)
  Creates a behavior with a single goal.
- [convenience init(goals: [GKGoal])](gkbehavior/init(goals:).md)
  Creates a behavior with the specified goals.
- [convenience init(weightedGoals: [GKGoal : NSNumber])](gkbehavior/init(weightedgoals:).md)
  Creates a behavior with the specified mapping of goals to their weights.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkbehavior/init(goals:andweights:))*
# init(weightedGoals:)

**Framework**: GameplayKit  
**Kind**: init

Creates a behavior with the specified mapping of goals to their weights.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(weightedGoals: [GKGoal : NSNumber])
```

#### Return Value

A new behavior object. To assign a set of goals to an agent, use its [`behavior`](gkagent/behavior.md) property.

## Parameters

- `weightedGoals`: A dictionary whose keys are goal objects, where each value is the weight to be applied to the corresponding goal’s influence on an agent’s speed and direction.

## See Also

- [convenience init(goal: GKGoal, weight: Float)](gkbehavior/init(goal:weight:).md)
  Creates a behavior with a single goal.
- [convenience init(goals: [GKGoal])](gkbehavior/init(goals:).md)
  Creates a behavior with the specified goals.
- [convenience init(goals: [GKGoal], andWeights: [NSNumber])](gkbehavior/init(goals:andweights:).md)
  Creates a behavior with the specified goals and weights.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkbehavior/init(weightedgoals:))*
# init(weightedGoals:)

**Framework**: GameplayKit  
**Kind**: init  
**Role**: Initializer

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

```objc
+ (instancetype) behaviorWithWeightedGoals:(NSDictionary<GKGoal *,NSNumber *> *) weightedGoals;
```

#### Return Value

A new behavior object. To assign a set of goals to an agent, use its [`behavior`](../gkagent/behavior.md) property.

## Parameters

- `weightedGoals`: A dictionary whose keys are goal objects, where each value is the weight to be applied to the corresponding goal’s influence on an agent’s speed and direction.

## See Also

### Creating a Behavior
- [convenience init(goal: GKGoal, weight: Float)](./init%28goal,weight%29.md)
  Creates a behavior with a single goal.
- [convenience init(goals: [GKGoal])](./init%28goals%29.md)
  Creates a behavior with the specified goals.
- [convenience init(goals: [GKGoal], andWeights: [NSNumber])](./init%28goals,andweights%29.md)
  Creates a behavior with the specified goals and weights.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkbehavior/init(weightedgoals:))*
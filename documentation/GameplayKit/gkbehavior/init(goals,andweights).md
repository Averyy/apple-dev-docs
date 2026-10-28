# init(goals:andWeights:)

**Framework**: GameplayKit  
**Kind**: init  
**Role**: Initializer

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

```objc
+ (instancetype) behaviorWithGoals:(NSArray<GKGoal *> *) goals andWeights:(NSArray<NSNumber *> *) weights;
```

## Return Value

A new behavior object. To assign a set of goals to an agent, use its [`behavior`](../gkagent/behavior.md) property.

## Parameters

- `goals`: An array of goal objects.
- `weights`: An array of numbers, each the weight to be applied to the goal at the corresponding index in the `goals` array.

## See Also

### Creating a Behavior
- [convenience init(goal: GKGoal, weight: Float)](./init%28goal,weight%29.md)
  Creates a behavior with a single goal.
- [convenience init(goals: [GKGoal])](./init%28goals%29.md)
  Creates a behavior with the specified goals.
- [convenience init(weightedGoals: [GKGoal : NSNumber])](./init%28weightedgoals%29.md)
  Creates a behavior with the specified mapping of goals to their weights.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkbehavior/init(goals:andweights:))*
# remove(_:)

**Framework**: GameplayKit  
**Kind**: method  
**Role**: Instance Method

Removes the specified goal from the behavior.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func remove(_ goal: GKGoal)
```

```objc
- (void) removeGoal:(GKGoal *) goal;
```

## Parameters

- `goal`: A goal object.

## See Also

### Managing a Behavior’s Set of Goals
- [func setWeight(Float, for: GKGoal)](./setweight%28_,for%29.md)
  Sets the weight for the specified goal’s influence on agents, adding that goal to the behavior if not already present.
- [func weight(for: GKGoal) -> Float](./weight%28for%29.md)
  Returns the weight for the specified goal’s influence on agents.
- [func removeAllGoals()](./removeallgoals%28%29.md)
  Removes all goals from the behavior.
- [var goalCount: Int](./goalcount.md)
  The number of goals in the behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkbehavior/remove(_:))*
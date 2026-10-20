# goalCount

**Framework**: GameplayKit  
**Kind**: property  
**Role**: Instance Property

The number of goals in the behavior.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var goalCount: Int { get }
```

```objc
@property (readonly) NSInteger goalCount;
```

## See Also

### Managing a Behavior’s Set of Goals
- [func setWeight(Float, for: GKGoal)](./setweight%28_,for%29.md)
  Sets the weight for the specified goal’s influence on agents, adding that goal to the behavior if not already present.
- [func weight(for: GKGoal) -> Float](./weight%28for%29.md)
  Returns the weight for the specified goal’s influence on agents.
- [func remove(GKGoal)](./remove%28_%29.md)
  Removes the specified goal from the behavior.
- [func removeAllGoals()](./removeallgoals%28%29.md)
  Removes all goals from the behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkbehavior/goalcount)*
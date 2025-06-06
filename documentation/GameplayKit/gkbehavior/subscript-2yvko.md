# subscript(_:)

**Framework**: GameplayKit  
**Kind**: subscript

Returns the weight associated with the goal specified by subscript syntax.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
subscript(goal: GKGoal) -> NSNumber! { get set }
```

#### Return Value

The weight to be applied to the goal’s influence on an agent’s speed and direction, or `0.0` if the goal is not in the behavior.

#### Discussion

This method is equivalent to the [`weight(for:)`](gkbehavior/weight(for:).md) method, but allows access using subscript syntax.

## Parameters

- `goal`: A goal already included in the behavior’s set of goals.

## See Also

- [subscript(Int) -> GKGoal](gkbehavior/subscript(_:)-997a9.md)
  Returns the goal at the specified index in the behavior’s list of goals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkbehavior/subscript(_:)-2yvko)*
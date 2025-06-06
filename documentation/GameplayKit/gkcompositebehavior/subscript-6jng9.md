# subscript(_:)

**Framework**: GameplayKit  
**Kind**: subscript

Returns the weight associated with the behavior specified by subscript syntax.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
subscript(behavior: GKBehavior) -> NSNumber { get set }
```

#### Return Value

The weight applied to that behavior’s influence on an agent’s speed and direction, or `0.0` if that behavior is not in the composite behavior.

#### Discussion

This method is equivalent to the [`weight(for:)`](gkcompositebehavior/weight(for:).md) method, but allows access using subscript syntax.

## Parameters

- `behavior`: An individual behavior already included in the composite behavior’s set of behaviors.

## See Also

- [subscript(Int) -> GKBehavior](gkcompositebehavior/subscript(_:)-6krdg.md)
  Returns the individual behavior at the specified index in the composite behavior’s list of behaviors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkcompositebehavior/subscript(_:)-6jng9)*
# addAnimationCompletion(criteria:_:)

**Framework**: SwiftUI  
**Kind**: method

Adds a completion to run when the animations created with this transaction are all complete.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
mutating func addAnimationCompletion(criteria: AnimationCompletionCriteria = .logicallyComplete, _ completion: @escaping () -> Void)
```

#### Discussion

The completion callback will always be fired exactly one time. If no animations are created by the changes in `body`, then the callback will be called immediately after `body`.

## See Also

- [var animation: Animation?](transaction/animation.md)
  The animation, if any, associated with the current state change.
- [var disablesAnimations: Bool](transaction/disablesanimations.md)
  A Boolean value that indicates whether views should disable animations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/transaction/addanimationcompletion(criteria:_:))*
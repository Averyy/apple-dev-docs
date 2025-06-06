# withAnimation(_:completionCriteria:_:completion:)

**Framework**: SwiftUI  
**Kind**: func

Returns the result of recomputing the view’s body with the provided animation, and runs the completion when all animations are complete.

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
func withAnimation<Result>(_ animation: Animation? = .default, completionCriteria: AnimationCompletionCriteria = .logicallyComplete, _ body: () throws -> Result, completion: @escaping () -> Void) rethrows -> Result
```

#### Discussion

This function sets the given [`Animation`](animation.md) as the [`animation`](transaction/animation.md) property of the thread’s current [`Transaction`](transaction.md) as well as calling `Transaction/addAnimationCompletion` with the specified completion.

The completion callback will always be fired exactly one time. If no animations are created by the changes in `body`, then the callback will be called immediately after `body`.

## See Also

- [func withAnimation<Result>(Animation?, () throws -> Result) rethrows -> Result](withanimation(_:_:).md)
  Returns the result of recomputing the view’s body with the provided animation.
- [struct AnimationCompletionCriteria](animationcompletioncriteria.md)
  The criteria that determines when an animation is considered finished.
- [struct Animation](animation.md)
  The way a view changes over time to create a smooth visual transition from one state to another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/withanimation(_:completioncriteria:_:completion:))*
# withAnimation(_:_:)

**Framework**: SwiftUI  
**Kind**: func

Returns the result of recomputing the view’s body with the provided animation.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func withAnimation<Result>(_ animation: Animation? = .default, _ body: () throws -> Result) rethrows -> Result
```

## Mentions

- [Applying Liquid Glass to custom views](applying-liquid-glass-to-custom-views.md)
- [Managing user interface state](managing-user-interface-state.md)

#### Discussion

This function sets the given [`Animation`](animation.md) as the [`animation`](transaction/animation.md) property of the thread’s current [`Transaction`](transaction.md).

## See Also

- [func withAnimation<Result>(Animation?, completionCriteria: AnimationCompletionCriteria, () throws -> Result, completion: () -> Void) rethrows -> Result](withanimation(_:completioncriteria:_:completion:).md)
  Returns the result of recomputing the view’s body with the provided animation, and runs the completion when all animations are complete.
- [struct AnimationCompletionCriteria](animationcompletioncriteria.md)
  The criteria that determines when an animation is considered finished.
- [struct Animation](animation.md)
  The way a view changes over time to create a smooth visual transition from one state to another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/withanimation(_:_:))*
# AnimationCompletionCriteria

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

The criteria that determines when an animation is considered finished.

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
struct AnimationCompletionCriteria
```

## Topics

### Getting the completion criteria
- [static let logicallyComplete: AnimationCompletionCriteria](./animationcompletioncriteria/logicallycomplete.md)
  The animation has logically completed, but may still be in its long tail.
- [static let removed: AnimationCompletionCriteria](./animationcompletioncriteria/removed.md)
  The entire animation is finished and will now be removed.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Adding state-based animation to an action
- [func withAnimation<Result>(Animation?, () throws -> Result) rethrows -> Result](./withanimation%28_,_%29.md)
  Returns the result of recomputing the view’s body with the provided animation.
- [func withAnimation<Result>(Animation?, completionCriteria: AnimationCompletionCriteria, () throws -> Result, completion: () -> Void) rethrows -> Result](./withanimation%28_,completioncriteria,_,completion%29.md)
  Returns the result of recomputing the view’s body with the provided animation, and runs the completion when all animations are complete.
- [struct Animation](./animation.md)
  The way a view changes over time to create a smooth visual transition from one state to another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/animationcompletioncriteria)*
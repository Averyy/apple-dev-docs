# isLogicallyComplete

**Framework**: SwiftUI  
**Kind**: property

Set this to `true` to indicate that an animation is logically complete.

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
var isLogicallyComplete: Bool
```

#### Discussion

This controls when AnimationCompletionCriteria.logicallyComplete completion callbacks are fired. This should be set to `true` at most once in the life of an animation, changing back to `false` later will be ignored. If this is never set to `true`, the behavior is equivalent to if this had been set to `true` just as the animation finished (by returning `nil`).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/animationcontext/islogicallycomplete)*
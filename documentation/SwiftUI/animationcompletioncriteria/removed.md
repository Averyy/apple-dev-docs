# removed

**Framework**: SwiftUI  
**Kind**: property

The entire animation is finished and will now be removed.

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
static let removed: AnimationCompletionCriteria
```

#### Discussion

If a subsequent change occurs that creates additional animations on properties with `removed` completion callbacks registered, then those callbacks will only fire when  of the created animations are complete.

## See Also

- [static let logicallyComplete: AnimationCompletionCriteria](animationcompletioncriteria/logicallycomplete.md)
  The animation has logically completed, but may still be in its long tail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/animationcompletioncriteria/removed)*
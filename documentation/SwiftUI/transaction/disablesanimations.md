# disablesAnimations

**Framework**: SwiftUI  
**Kind**: property

A Boolean value that indicates whether views should disable animations.

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
var disablesAnimations: Bool { get set }
```

#### Discussion

This value is `true` during the initial phase of a two-part transition update, to prevent [`animation(_:)`](view/animation(_:).md) from inserting new animations into the transaction.

## See Also

- [var animation: Animation?](transaction/animation.md)
  The animation, if any, associated with the current state change.
- [func addAnimationCompletion(criteria: AnimationCompletionCriteria, () -> Void)](transaction/addanimationcompletion(criteria:_:).md)
  Adds a completion to run when the animations created with this transaction are all complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/transaction/disablesanimations)*
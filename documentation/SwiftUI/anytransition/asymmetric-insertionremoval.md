# asymmetric(insertion:removal:)

**Framework**: SwiftUI  
**Kind**: method

Provides a composite transition that uses a different transition for insertion versus removal.

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
static func asymmetric(insertion: AnyTransition, removal: AnyTransition) -> AnyTransition
```

## See Also

- [func animation(Animation?) -> AnyTransition](anytransition/animation(_:).md)
  Attaches an animation to this transition.
- [func combined(with: AnyTransition) -> AnyTransition](anytransition/combined(with:).md)
  Combines this transition with another, returning a new transition that is the result of both transitions being applied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/anytransition/asymmetric(insertion:removal:))*
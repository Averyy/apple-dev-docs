# combined(with:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Combines this transition with another, returning a new transition that is the result of both transitions being applied.

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
func combined(with other: AnyTransition) -> AnyTransition
```

## See Also

### Combining and configuring transitions
- [func animation(Animation?) -> AnyTransition](./animation%28_%29.md)
  Attaches an animation to this transition.
- [static func asymmetric(insertion: AnyTransition, removal: AnyTransition) -> AnyTransition](./asymmetric%28insertion,removal%29.md)
  Provides a composite transition that uses a different transition for insertion versus removal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/anytransition/combined(with:))*
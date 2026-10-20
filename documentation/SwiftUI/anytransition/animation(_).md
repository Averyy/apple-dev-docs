# animation(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Attaches an animation to this transition.

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
func animation(_ animation: Animation?) -> AnyTransition
```

## See Also

### Combining and configuring transitions
- [static func asymmetric(insertion: AnyTransition, removal: AnyTransition) -> AnyTransition](./asymmetric%28insertion,removal%29.md)
  Provides a composite transition that uses a different transition for insertion versus removal.
- [func combined(with: AnyTransition) -> AnyTransition](./combined%28with%29.md)
  Combines this transition with another, returning a new transition that is the result of both transitions being applied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/anytransition/animation(_:))*
# body(content:phase:)

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Gets the current body of the caller.

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
@ViewBuilder
@MainActor @preconcurrency func body(content: Self.Content, phase: TransitionPhase) -> Self.Body
```

#### Discussion

`content` is a proxy for the view that will have the modifier represented by `Self` applied to it.

## See Also

- [associatedtype Body : View](transition/body.md)
  The type of view representing the body.
- [Transition.Content](transition/content.md)
  The content view type passed to `body()`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/transition/body(content:phase:))*
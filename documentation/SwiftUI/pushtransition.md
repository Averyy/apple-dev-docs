# PushTransition

**Framework**: SwiftUI  
**Kind**: struct

A transition that when added to a view will animate the view’s insertion by moving it in from the specified edge while fading it in, and animate its removal by moving it out towards the opposite edge and fading it out.

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
@MainActor
@preconcurrency struct PushTransition
```

## Topics

### Creating the transition
- [init(edge: Edge)](pushtransition/init(edge:).md)
  Creates a transition that animates a view by moving and fading it.
- [var edge: Edge](pushtransition/edge.md)
  The edge from which the view will be animated in.

## Relationships

### Conforms To
- [Transition](transition.md)

## See Also

- [struct BlurReplaceTransition](blurreplacetransition.md)
  A transition that animates the insertion or removal of a view by combining blurring and scaling effects.
- [struct IdentityTransition](identitytransition.md)
  A transition that returns the input view, unmodified, as the output view.
- [struct MoveTransition](movetransition.md)
  Returns a transition that moves the view away, towards the specified edge of the view.
- [struct OffsetTransition](offsettransition.md)
  Returns a transition that offset the view by the specified amount.
- [struct OpacityTransition](opacitytransition.md)
  A transition from transparent to opaque on insertion, and from opaque to transparent on removal.
- [struct ScaleTransition](scaletransition.md)
  Returns a transition that scales the view.
- [struct SlideTransition](slidetransition.md)
  A transition that inserts by moving in from the leading edge, and removes by moving out towards the trailing edge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/pushtransition)*
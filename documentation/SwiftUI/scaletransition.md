# ScaleTransition

**Framework**: SwiftUI  
**Kind**: struct

Returns a transition that scales the view.

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
struct ScaleTransition
```

## Topics

### Creating the transition
- [init(Double, anchor: UnitPoint)](scaletransition/init(_:anchor:).md)
  Creates a transition that scales the view by the specified amount.
- [var anchor: UnitPoint](scaletransition/anchor.md)
  The anchor point to scale the view around.
- [var scale: Double](scaletransition/scale.md)
  The amount to scale the view by.

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
- [struct PushTransition](pushtransition.md)
  A transition that when added to a view will animate the view’s insertion by moving it in from the specified edge while fading it in, and animate its removal by moving it out towards the opposite edge and fading it out.
- [struct SlideTransition](slidetransition.md)
  A transition that inserts by moving in from the leading edge, and removes by moving out towards the trailing edge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scaletransition)*
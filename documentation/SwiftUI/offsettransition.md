# OffsetTransition

**Framework**: SwiftUI  
**Kind**: struct

Returns a transition that offset the view by the specified amount.

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
struct OffsetTransition
```

## Topics

### Creating the transition
- [init(CGSize)](offsettransition/init(_:).md)
  Creates a transition that offset the view by the specified amount.
- [var offset: CGSize](offsettransition/offset.md)
  The amount to offset the view by.

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
- [struct OpacityTransition](opacitytransition.md)
  A transition from transparent to opaque on insertion, and from opaque to transparent on removal.
- [struct PushTransition](pushtransition.md)
  A transition that when added to a view will animate the view’s insertion by moving it in from the specified edge while fading it in, and animate its removal by moving it out towards the opposite edge and fading it out.
- [struct ScaleTransition](scaletransition.md)
  Returns a transition that scales the view.
- [struct SlideTransition](slidetransition.md)
  A transition that inserts by moving in from the leading edge, and removes by moving out towards the trailing edge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/offsettransition)*
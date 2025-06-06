# blurReplace(_:)

**Framework**: SwiftUI  
**Kind**: method

A transition that animates the insertion or removal of a view by combining blurring and scaling effects.

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
@preconcurrency static func blurReplace(_ config: BlurReplaceTransition.Configuration = .downUp) -> Self
```

## See Also

- [static var blurReplace: BlurReplaceTransition](transition/blurreplace.md)
  A transition that animates the insertion or removal of a view by combining blurring and scaling effects.
- [static var identity: IdentityTransition](transition/identity.md)
  A transition that returns the input view, unmodified, as the output view.
- [static func move(edge: Edge) -> Self](transition/move(edge:).md)
  Returns a transition that moves the view away, towards the specified edge of the view.
- [static func offset(CGSize) -> Self](transition/offset(_:).md)
  Returns a transition that offset the view by the specified amount.
- [static func offset(x: CGFloat, y: CGFloat) -> Self](transition/offset(x:y:).md)
  Returns a transition that offset the view by the specified x and y values.
- [static var opacity: OpacityTransition](transition/opacity.md)
  A transition from transparent to opaque on insertion, and from opaque to transparent on removal.
- [static func push(from: Edge) -> Self](transition/push(from:).md)
  Creates a transition that when added to a view will animate the view’s insertion by moving it in from the specified edge while fading it in, and animate its removal by moving it out towards the opposite edge and fading it out.
- [static var scale: ScaleTransition](transition/scale.md)
  Returns a transition that scales the view.
- [static func scale(Double, anchor: UnitPoint) -> Self](transition/scale(_:anchor:).md)
  Returns a transition that scales the view by the specified amount.
- [static var slide: SlideTransition](transition/slide.md)
  A transition that inserts by moving in from the leading edge, and removes by moving out towards the trailing edge.
- [static var symbolEffect: SymbolEffectTransition](transition/symboleffect.md)
  A transition that applies the default symbol effect transition to symbol images within the inserted or removed view hierarchy. Other views are unaffected by this transition.
- [static func symbolEffect<T>(T, options: SymbolEffectOptions) -> SymbolEffectTransition](transition/symboleffect(_:options:).md)
  Creates a transition that applies the provided effect to symbol images within the inserted or removed view hierarchy. Other views are unaffected by this transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/transition/blurreplace(_:))*
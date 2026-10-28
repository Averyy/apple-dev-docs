# push(from:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

Creates a transition that when added to a view will animate the view’s insertion by moving it in from the specified edge while fading it in, and animate its removal by moving it out towards the opposite edge and fading it out.

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
@export(implementation) @preconcurrency static func push(from edge: Edge) -> Self
```

Available when `Self` is `PushTransition`.

## Return Value

A transition that animates a view by moving and fading it.

## Parameters

- `edge`: The edge from which the view will be animated in.

## See Also

### Getting built-in transitions
- [static var blurReplace: BlurReplaceTransition](./blurreplace.md)
  A transition that animates the insertion or removal of a view by combining blurring and scaling effects.
- [static func blurReplace(BlurReplaceTransition.Configuration) -> Self](./blurreplace%28_%29.md)
  A transition that animates the insertion or removal of a view by combining blurring and scaling effects.
- [static var identity: IdentityTransition](./identity.md)
  A transition that returns the input view, unmodified, as the output view.
- [static func move(edge: Edge) -> Self](./move%28edge%29.md)
  Returns a transition that moves the view away, towards the specified edge of the view.
- [static func offset(CGSize) -> Self](./offset%28_%29.md)
  Returns a transition that offset the view by the specified amount.
- [static func offset(x: CGFloat, y: CGFloat) -> Self](./offset%28x,y%29.md)
  Returns a transition that offset the view by the specified x and y values.
- [static var opacity: OpacityTransition](./opacity.md)
  A transition from transparent to opaque on insertion, and from opaque to transparent on removal.
- [static var scale: ScaleTransition](./scale.md)
  Returns a transition that scales the view.
- [static func scale(Double, anchor: UnitPoint) -> Self](./scale%28_,anchor%29.md)
  Returns a transition that scales the view by the specified amount.
- [static var slide: SlideTransition](./slide.md)
  A transition that inserts by moving in from the leading edge, and removes by moving out towards the trailing edge.
- [static var symbolEffect: SymbolEffectTransition](./symboleffect.md)
  A transition that applies the default symbol effect transition to symbol images within the inserted or removed view hierarchy. Other views are unaffected by this transition.
- [static func symbolEffect<T>(T, options: SymbolEffectOptions) -> SymbolEffectTransition](./symboleffect%28_,options%29.md)
  Creates a transition that applies the provided effect to symbol images within the inserted or removed view hierarchy. Other views are unaffected by this transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/transition/push(from:))*
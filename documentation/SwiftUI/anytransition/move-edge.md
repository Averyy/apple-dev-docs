# move(edge:)

**Framework**: SwiftUI  
**Kind**: method

Returns a transition that moves the view away, towards the specified edge of the view.

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
static func move(edge: Edge) -> AnyTransition
```

## See Also

- [static var identity: AnyTransition](anytransition/identity.md)
  A transition that returns the input view, unmodified, as the output view.
- [static func offset(CGSize) -> AnyTransition](anytransition/offset(_:).md)
- [static func offset(x: CGFloat, y: CGFloat) -> AnyTransition](anytransition/offset(x:y:).md)
- [static let opacity: AnyTransition](anytransition/opacity.md)
  A transition from transparent to opaque on insertion, and from opaque to transparent on removal.
- [static func push(from: Edge) -> AnyTransition](anytransition/push(from:).md)
  Creates a transition that when added to a view will animate the view’s insertion by moving it in from the specified edge while fading it in, and animate its removal by moving it out towards the opposite edge and fading it out.
- [static var scale: AnyTransition](anytransition/scale.md)
  Returns a transition that scales the view.
- [static func scale(scale: CGFloat, anchor: UnitPoint) -> AnyTransition](anytransition/scale(scale:anchor:).md)
  Returns a transition that scales the view by the specified amount.
- [static var slide: AnyTransition](anytransition/slide.md)
  A transition that inserts by moving in from the leading edge, and removes by moving out towards the trailing edge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/anytransition/move(edge:))*
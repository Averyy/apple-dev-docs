# push(from:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

Creates a transition that when added to a view will animate the view’s insertion by moving it in from the specified edge while fading it in, and animate its removal by moving it out towards the opposite edge and fading it out.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static func push(from edge: Edge) -> AnyTransition
```

## Return Value

A transition that animates a view by moving and fading it.

## Parameters

- `edge`: The edge from which the view will be animated in.

## See Also

### Getting built-in transitions
- [static var identity: AnyTransition](./identity.md)
  A transition that returns the input view, unmodified, as the output view.
- [static func move(edge: Edge) -> AnyTransition](./move%28edge%29.md)
  Returns a transition that moves the view away, towards the specified edge of the view.
- [static func offset(CGSize) -> AnyTransition](./offset%28_%29.md)
- [static func offset(x: CGFloat, y: CGFloat) -> AnyTransition](./offset%28x,y%29.md)
- [static let opacity: AnyTransition](./opacity.md)
  A transition from transparent to opaque on insertion, and from opaque to transparent on removal.
- [static var scale: AnyTransition](./scale.md)
  Returns a transition that scales the view.
- [static func scale(scale: CGFloat, anchor: UnitPoint) -> AnyTransition](./scale%28scale,anchor%29.md)
  Returns a transition that scales the view by the specified amount.
- [static var slide: AnyTransition](./slide.md)
  A transition that inserts by moving in from the leading edge, and removes by moving out towards the trailing edge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/anytransition/push(from:))*
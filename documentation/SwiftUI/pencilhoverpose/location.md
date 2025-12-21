# location

**Framework**: SwiftUI  
**Kind**: property

The location of an Apple Pencil hovering in the area above the view’s bounds, expressed as a point in that view’s coordinate space.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst 17.5+
- macOS 14.5+
- visionOS 26.2+

## Declaration

```swift
let location: CGPoint
```

#### Discussion

Use the [`anchor`](pencilhoverpose/anchor.md) property if you require a normalized anchor point for use with a presentation modifier instead.

## See Also

- [let anchor: UnitPoint](pencilhoverpose/anchor.md)
  The location of an Apple Pencil hovering in the area above the view’s bounds, expressed as a normalized anchor point relative to that view.
- [let zDistance: CGFloat](pencilhoverpose/zdistance.md)
  The normalized distance between the screen and a hovering Apple Pencil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/pencilhoverpose/location)*
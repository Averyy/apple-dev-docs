# zDistance

**Framework**: SwiftUI  
**Kind**: property

The normalized distance between the screen and a hovering Apple Pencil.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst 17.5+
- macOS 14.5+

## Declaration

```swift
let zDistance: CGFloat
```

#### Discussion

This value is `1` at the maximum distance from the screen and approaches `0` as the Apple Pencil gets closer to the screen.

## See Also

- [let anchor: UnitPoint](pencilhoverpose/anchor.md)
  The location of an Apple Pencil hovering in the area above the view’s bounds, expressed as a normalized anchor point relative to that view.
- [let location: CGPoint](pencilhoverpose/location.md)
  The location of an Apple Pencil hovering in the area above the view’s bounds, expressed as a point in that view’s coordinate space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/pencilhoverpose/zdistance)*
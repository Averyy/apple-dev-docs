# anchor

**Framework**: SwiftUI  
**Kind**: property

The location of an Apple Pencil hovering in the area above the view’s bounds, expressed as a normalized anchor point relative to that view.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst 17.5+
- macOS 14.5+
- visionOS 26.2+

## Declaration

```swift
let anchor: UnitPoint
```

#### Discussion

You can pass this anchor point directly to a presentation modifier like [`popover(isPresented:attachmentAnchor:arrowEdge:content:)`](view/popover(ispresented:attachmentanchor:arrowedge:content:).md) or use the [`location`](pencilhoverpose/location.md) property if you require an absolute point instead.

## See Also

- [let location: CGPoint](pencilhoverpose/location.md)
  The location of an Apple Pencil hovering in the area above the view’s bounds, expressed as a point in that view’s coordinate space.
- [let zDistance: CGFloat](pencilhoverpose/zdistance.md)
  The normalized distance between the screen and a hovering Apple Pencil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/pencilhoverpose/anchor)*
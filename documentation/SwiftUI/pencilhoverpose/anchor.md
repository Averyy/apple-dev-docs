# anchor

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

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

## Discussion

You can pass this anchor point directly to a presentation modifier like [`popover(isPresented:attachmentAnchor:arrowEdge:content:)`](../view/popover%28ispresented,attachmentanchor,arrowedge,content%29.md) or use the [`location`](./location.md) property if you require an absolute point instead.

## See Also

### Getting the hover characteristics
- [let altitude: Angle](./altitude.md)
  A value that represents the altitude angle of the hovering Apple Pencil.
- [let azimuth: Angle](./azimuth.md)
  A value that represents the azimuth angle of a hovering Apple Pencil.
- [let location: CGPoint](./location.md)
  The location of an Apple Pencil hovering in the area above the view’s bounds, expressed as a point in that view’s coordinate space.
- [let roll: Angle](./roll.md)
  A value that represents the barrel roll angle of the hovering Apple Pencil.
- [let zDistance: CGFloat](./zdistance.md)
  The normalized distance between the screen and a hovering Apple Pencil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/pencilhoverpose/anchor)*
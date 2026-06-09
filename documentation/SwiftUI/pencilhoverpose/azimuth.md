# azimuth

**Framework**: SwiftUI  
**Kind**: property

A value that represents the azimuth angle of a hovering Apple Pencil.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst 17.5+
- macOS 14.5+
- visionOS 26.2+

## Declaration

```swift
let azimuth: Angle
```

#### Discussion

This value is `.zero` when the Apple Pencil points along the view’s positive x-axis.

## See Also

- [let altitude: Angle](pencilhoverpose/altitude.md)
  A value that represents the altitude angle of the hovering Apple Pencil.
- [let anchor: UnitPoint](pencilhoverpose/anchor.md)
  The location of an Apple Pencil hovering in the area above the view’s bounds, expressed as a normalized anchor point relative to that view.
- [let location: CGPoint](pencilhoverpose/location.md)
  The location of an Apple Pencil hovering in the area above the view’s bounds, expressed as a point in that view’s coordinate space.
- [let roll: Angle](pencilhoverpose/roll.md)
  A value that represents the barrel roll angle of the hovering Apple Pencil.
- [let zDistance: CGFloat](pencilhoverpose/zdistance.md)
  The normalized distance between the screen and a hovering Apple Pencil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/pencilhoverpose/azimuth)*
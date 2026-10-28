# altitude

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

A value that represents the altitude angle of the hovering Apple Pencil.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst 17.5+
- macOS 14.5+
- visionOS 26.2+

## Declaration

```swift
let altitude: Angle
```

## Discussion

This value is `.zero` when the Apple Pencil is parallel to the view’s surface, and is 90 degrees (π/2 radians) when the Apple Pencil is perpendicular to the view’s surface.

## See Also

### Getting the hover characteristics
- [let anchor: UnitPoint](./anchor.md)
  The location of an Apple Pencil hovering in the area above the view’s bounds, expressed as a normalized anchor point relative to that view.
- [let azimuth: Angle](./azimuth.md)
  A value that represents the azimuth angle of a hovering Apple Pencil.
- [let location: CGPoint](./location.md)
  The location of an Apple Pencil hovering in the area above the view’s bounds, expressed as a point in that view’s coordinate space.
- [let roll: Angle](./roll.md)
  A value that represents the barrel roll angle of the hovering Apple Pencil.
- [let zDistance: CGFloat](./zdistance.md)
  The normalized distance between the screen and a hovering Apple Pencil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/pencilhoverpose/altitude)*
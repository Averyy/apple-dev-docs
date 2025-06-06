# Path.Element.move(to:)

**Framework**: SwiftUI  
**Kind**: case

A path element that terminates the current subpath (without closing it) and defines a new current point.

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
case move(to: CGPoint)
```

## See Also

- [Path.Element.closeSubpath](path/element/closesubpath.md)
  A line from the start point of the current subpath (if any) to the current point, which terminates the subpath.
- [case curve(to: CGPoint, control1: CGPoint, control2: CGPoint)](path/element/curve(to:control1:control2:).md)
  A cubic Bézier curve from the previous current point to the given end-point, using the two control points to define the curve.
- [Path.Element.line(to:)](path/element/line(to:).md)
  A line from the previous current point to the given point, which becomes the new current point.
- [case quadCurve(to: CGPoint, control: CGPoint)](path/element/quadcurve(to:control:).md)
  A quadratic Bézier curve from the previous current point to the given end-point, using the single control point to define the curve.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/path/element/move(to:))*
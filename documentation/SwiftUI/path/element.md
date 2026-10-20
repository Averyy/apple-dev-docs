# Path.Element

**Framework**: SwiftUI  
**Kind**: enum  
**Role**: Enumeration

An element of a path.

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
@frozen
enum Element
```

## Topics

### Getting path elements
- [Path.Element.closeSubpath](./element/closesubpath.md)
  A line from the start point of the current subpath (if any) to the current point, which terminates the subpath.
- [case curve(to: CGPoint, control1: CGPoint, control2: CGPoint)](./element/curve%28to,control1,control2%29.md)
  A cubic Bézier curve from the previous current point to the given end-point, using the two control points to define the curve.
- [Path.Element.line(to:)](./element/line%28to%29.md)
  A line from the previous current point to the given point, which becomes the new current point.
- [Path.Element.move(to:)](./element/move%28to%29.md)
  A path element that terminates the current subpath (without closing it) and defines a new current point.
- [case quadCurve(to: CGPoint, control: CGPoint)](./element/quadcurve%28to,control%29.md)
  A quadratic Bézier curve from the previous current point to the given end-point, using the single control point to define the curve.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Operating over path elements
- [func forEach((Path.Element) -> Void)](./foreach%28_%29.md)
  Calls `body` with each element in the path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/path/element)*
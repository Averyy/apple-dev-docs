# NSBezierPath.ElementType

**Framework**: AppKit  
**Kind**: enum

Constants that specify basic path element commands.

**Availability**:
- macOS ?+

## Declaration

```swift
enum ElementType
```

#### Overview

These commands are enough to define all of the possible path shapes. Each command has one or more points that contain information needed to position the path element. Most path elements use the current drawing point as the starting point for drawing. For more details, see [`Paths`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaDrawingGuide/Paths/Paths.html#//apple_ref/doc/uid/TP40003290-CH206).

## Topics

### Constants
- [NSBezierPath.ElementType.moveTo](nsbezierpath/elementtype/moveto.md)
  Moves the path object’s current drawing point to the specified point.
- [NSBezierPath.ElementType.lineTo](nsbezierpath/elementtype/lineto.md)
  Creates a straight line from the current drawing point to the specified point.
- [NSBezierPath.ElementType.closePath](nsbezierpath/elementtype/closepath.md)
  Marks the end of the current subpath at the specified point.
- [static var curveTo: NSBezierPath.ElementType](nsbezierpath/elementtype/curveto.md)
  Creates a curved line segment from the current point to the specified endpoint using two control points to define the curve.
- [NSBezierPath.ElementType.cubicCurveTo](nsbezierpath/elementtype/cubiccurveto.md)
- [NSBezierPath.ElementType.quadraticCurveTo](nsbezierpath/elementtype/quadraticcurveto.md)
### Initializers
- [init?(rawValue: UInt)](nsbezierpath/elementtype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [NSBezierPath.LineJoinStyle](nsbezierpath/linejoinstyle-swift.enum.md)
  Constants that specify the shape of the joins between connected segments of a stroked path.
- [NSBezierPath.LineCapStyle](nsbezierpath/linecapstyle-swift.enum.md)
  Constants that specify the shape of endpoints for an open path when it is stroked.
- [NSBezierPath.WindingRule](nsbezierpath/windingrule-swift.enum.md)
  Constants that specify the winding rule a Bézier path uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/elementtype)*
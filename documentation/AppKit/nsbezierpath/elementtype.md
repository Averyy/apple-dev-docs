# NSBezierPath.ElementType

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Constants that specify basic path element commands.

**Availability**:
- macOS

## Declaration

```swift
enum ElementType
```

```c
enum NSBezierPathElement : NSUInteger;
```

## Overview

These commands are enough to define all of the possible path shapes. Each command has one or more points that contain information needed to position the path element. Most path elements use the current drawing point as the starting point for drawing. For more information, see [`NSBezierPath`](../nsbezierpath.md).

## Topics

### Constants
- [NSBezierPath.ElementType.moveTo](./elementtype/moveto.md)
  Moves the path object’s current drawing point to the specified point.
- [NSBezierPath.ElementType.lineTo](./elementtype/lineto.md)
  Creates a straight line from the current drawing point to the specified point.
- [NSBezierPath.ElementType.closePath](./elementtype/closepath.md)
  Marks the end of the current subpath at the specified point.
- [NSBezierPath.ElementType.cubicCurveTo](./elementtype/cubiccurveto.md)
- [NSBezierPath.ElementType.quadraticCurveTo](./elementtype/quadraticcurveto.md)
### Deprecated
- [static var curveTo: NSBezierPath.ElementType](./elementtype/curveto.md)
  Creates a curved line segment from the current point to the specified endpoint using two control points to define the curve.
- [NSMoveToBezierPathElement](../nsmovetobezierpathelement.md)
  Moves the path object’s current drawing point to the specified point.
- [NSLineToBezierPathElement](../nslinetobezierpathelement.md)
  Creates a straight line from the current drawing point to the specified point.
- [NSCurveToBezierPathElement](../nscurvetobezierpathelement.md)
  Creates a curved line segment from the current point to the specified endpoint using two control points to define the curve.
- [NSClosePathBezierPathElement](../nsclosepathbezierpathelement.md)
  Marks the end of the current subpath at the specified point.
### Initializers
- [init?(rawValue: UInt)](./elementtype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Constants
- [NSBezierPath.LineJoinStyle](./linejoinstyle-swift.enum.md)
  Constants that specify the shape of the joins between connected segments of a stroked path.
- [NSBezierPath.LineCapStyle](./linecapstyle-swift.enum.md)
  Constants that specify the shape of endpoints for an open path when it is stroked.
- [NSBezierPath.WindingRule](./windingrule-swift.enum.md)
  Constants that specify the winding rule a Bézier path uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/elementtype)*
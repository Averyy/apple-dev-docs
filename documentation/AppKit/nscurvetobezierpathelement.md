# NSCurveToBezierPathElement

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

Creates a curved line segment from the current point to the specified endpoint using two control points to define the curve.

**Availability**:
- macOS 10.0+ - Deprecated in 11.0

> **Deprecated**: Use [`curveTo`](./nsbezierpath/elementtype/curveto.md) instead.

## Declaration

```c
static const NSBezierPathElement NSCurveToBezierPathElement;
```

#### Discussion

The points are stored in the following order: controlPoint1, controlPoint2, endPoint. Ovals, arcs, and Bezier curves all use curve elements to specify their geometry.

Contains 3 points.

## See Also

### Deprecated
- [NSMoveToBezierPathElement](./nsmovetobezierpathelement.md)
  Moves the path object’s current drawing point to the specified point.
- [NSLineToBezierPathElement](./nslinetobezierpathelement.md)
  Creates a straight line from the current drawing point to the specified point.
- [NSClosePathBezierPathElement](./nsclosepathbezierpathelement.md)
  Marks the end of the current subpath at the specified point.
- [static var curveTo: NSBezierPath.ElementType](./nsbezierpath/elementtype/curveto.md)
  Creates a curved line segment from the current point to the specified endpoint using two control points to define the curve.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscurvetobezierpathelement)*
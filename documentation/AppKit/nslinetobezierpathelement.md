# NSLineToBezierPathElement

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

Creates a straight line from the current drawing point to the specified point.

**Availability**:
- macOS 10.0+ - Deprecated in 11.0

> **Deprecated**: Use [`NSBezierPath.ElementType.lineTo`](./nsbezierpath/elementtype/lineto.md) instead.

## Declaration

```c
static const NSBezierPathElement NSLineToBezierPathElement;
```

## Discussion

Lines and rectangles are specified using this path element.

Contains 1 point.

## See Also

### Deprecated
- [NSMoveToBezierPathElement](./nsmovetobezierpathelement.md)
  Moves the path object’s current drawing point to the specified point.
- [NSCurveToBezierPathElement](./nscurvetobezierpathelement.md)
  Creates a curved line segment from the current point to the specified endpoint using two control points to define the curve.
- [NSClosePathBezierPathElement](./nsclosepathbezierpathelement.md)
  Marks the end of the current subpath at the specified point.
- [static var curveTo: NSBezierPath.ElementType](./nsbezierpath/elementtype/curveto.md)
  Creates a curved line segment from the current point to the specified endpoint using two control points to define the curve.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslinetobezierpathelement)*
# NSMoveToBezierPathElement

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

Moves the path object’s current drawing point to the specified point.

**Availability**:
- macOS 10.0+ - Deprecated in 11.0

> **Deprecated**: Use [`NSBezierPath.ElementType.moveTo`](./nsbezierpath/elementtype/moveto.md) instead.

## Declaration

```c
static const NSBezierPathElement NSMoveToBezierPathElement;
```

#### Discussion

This path element does not result in any drawing. Using this command in the middle of a path results in a disconnected line segment.

Contains 1 point.

## See Also

### Deprecated
- [NSLineToBezierPathElement](./nslinetobezierpathelement.md)
  Creates a straight line from the current drawing point to the specified point.
- [NSCurveToBezierPathElement](./nscurvetobezierpathelement.md)
  Creates a curved line segment from the current point to the specified endpoint using two control points to define the curve.
- [NSClosePathBezierPathElement](./nsclosepathbezierpathelement.md)
  Marks the end of the current subpath at the specified point.
- [static var curveTo: NSBezierPath.ElementType](./nsbezierpath/elementtype/curveto.md)
  Creates a curved line segment from the current point to the specified endpoint using two control points to define the curve.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmovetobezierpathelement)*
# NSClosePathBezierPathElement

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

Marks the end of the current subpath at the specified point.

**Availability**:
- macOS 10.0+ - Deprecated in 11.0

> **Deprecated**: Use [`NSBezierPath.ElementType.closePath`](./nsbezierpath/elementtype/closepath.md) instead.

## Declaration

```c
static const NSBezierPathElement NSClosePathBezierPathElement;
```

#### Discussion

Note that the point specified for the Close Path element is essentially the same as the current point.

## See Also

### Deprecated
- [NSMoveToBezierPathElement](./nsmovetobezierpathelement.md)
  Moves the path object’s current drawing point to the specified point.
- [NSLineToBezierPathElement](./nslinetobezierpathelement.md)
  Creates a straight line from the current drawing point to the specified point.
- [NSCurveToBezierPathElement](./nscurvetobezierpathelement.md)
  Creates a curved line segment from the current point to the specified endpoint using two control points to define the curve.
- [static var curveTo: NSBezierPath.ElementType](./nsbezierpath/elementtype/curveto.md)
  Creates a curved line segment from the current point to the specified endpoint using two control points to define the curve.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsclosepathbezierpathelement)*
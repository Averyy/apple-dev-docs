# curveTo

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Creates a curved line segment from the current point to the specified endpoint using two control points to define the curve.

**Availability**:
- macOS 11.0+ - Deprecated in 14.0 (renamed: NSBezierPath.ElementType.cubicCurveTo)

## Declaration

```swift
static var curveTo: NSBezierPath.ElementType { get }
```

```c
NSBezierPathElementCurveTo
```

## See Also

### Deprecated
- [NSMoveToBezierPathElement](../../nsmovetobezierpathelement.md)
  Moves the path object’s current drawing point to the specified point.
- [NSLineToBezierPathElement](../../nslinetobezierpathelement.md)
  Creates a straight line from the current drawing point to the specified point.
- [NSCurveToBezierPathElement](../../nscurvetobezierpathelement.md)
  Creates a curved line segment from the current point to the specified endpoint using two control points to define the curve.
- [NSClosePathBezierPathElement](../../nsclosepathbezierpathelement.md)
  Marks the end of the current subpath at the specified point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/elementtype/curveto)*
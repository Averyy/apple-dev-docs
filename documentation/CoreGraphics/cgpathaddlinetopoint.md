# CGPathAddLineToPoint

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Appends a line segment to a mutable graphics path.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern void CGPathAddLineToPoint(CGMutablePathRef path, const CGAffineTransform *m, CGFloat x, CGFloat y);
```

#### Discussion

Before returning, this function updates the current point to the specified location `(x,y)`.

## Parameters

- `path`: The mutable path to change. The path must not be empty.
- `m`: A pointer to an affine transformation matrix, or `NULL` if no transformation is needed. If specified, Core Graphics applies the transformation to the line before it is added to the path.
- `x`: The x-coordinate of the end point of the line.
- `y`: The y-coordinate of the end point of the line.

## See Also

### Constructing a Graphics Path
- [CGPathMoveToPoint](./cgpathmovetopoint.md)
  Starts a new subpath at a specified location in a mutable graphics path.
- [CGPathAddLines](./cgpathaddlines.md)
  Appends an array of new line segments to a mutable graphics path.
- [CGPathAddRect](./cgpathaddrect.md)
  Appends a rectangle to a mutable graphics path.
- [CGPathAddRects](./cgpathaddrects.md)
  Appends an array of rectangles to a mutable graphics path.
- [CGPathAddEllipseInRect](./cgpathaddellipseinrect.md)
  Adds to a path an ellipse that fits inside a rectangle.
- [CGPathAddRoundedRect](./cgpathaddroundedrect.md)
  Appends a rounded rectangle to a mutable graphics path.
- [CGPathAddArc](./cgpathaddarc.md)
  Appends an arc to a mutable graphics path, possibly preceded by a straight line segment.
- [CGPathAddArcToPoint](./cgpathaddarctopoint.md)
  Appends an arc to a mutable graphics path, possibly preceded by a straight line segment.
- [CGPathAddRelativeArc](./cgpathaddrelativearc.md)
  Appends an arc to a mutable graphics path, possibly preceded by a straight line segment.
- [CGPathAddCurveToPoint](./cgpathaddcurvetopoint.md)
  Appends a cubic Bézier curve to a mutable graphics path.
- [CGPathAddQuadCurveToPoint](./cgpathaddquadcurvetopoint.md)
  Appends a quadratic Bézier curve to a mutable graphics path.
- [CGPathAddPath](./cgpathaddpath.md)
  Appends a path to onto a mutable graphics path.
- [func closeSubpath()](./cgmutablepath/closesubpath%28%29.md)
  Closes and completes a subpath in a mutable graphics path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpathaddlinetopoint)*
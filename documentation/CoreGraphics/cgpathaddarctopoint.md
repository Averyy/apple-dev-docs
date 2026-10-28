# CGPathAddArcToPoint

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Appends an arc to a mutable graphics path, possibly preceded by a straight line segment.

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
extern void CGPathAddArcToPoint(CGMutablePathRef path, const CGAffineTransform *m, CGFloat x1, CGFloat y1, CGFloat x2, CGFloat y2, CGFloat radius);
```

## Discussion

This function uses a sequence of cubic Bézier curves to create an arc that is tangent to the line from the current point to (x1,y1) and to the line from (x1,y1) to (x2,y2). The start and end points of the arc are located on the first and second tangent lines, respectively. The start and end points of the arc are also the “tangent points” of the lines.

If the current point and the first tangent point of the arc (the starting point) are not equal, Core Graphics appends a straight line segment from the current point to the first tangent point.

The ending point of the arc becomes the new current point of the path.

For another way to draw an arc in a path, see [`CGPathAddArc`](./cgpathaddarc.md).

## Parameters

- `path`: The mutable path to change. The path must not be empty.
- `m`: A pointer to an affine transformation matrix, or `NULL` if no transformation is needed. If specified, Core Graphics applies the transformation to the arc before it is added to the path.
- `x1`: The x-coordinate of the user space for the end point of the first tangent line. The first tangent line is drawn from the current point to `(x1,y1)`.
- `y1`: The y-coordinate of the user space for the end point of the first tangent line. The first tangent line is drawn from the current point to `(x1,y1)`.
- `x2`: The x-coordinate of the user space for the end point of the second tangent line. The second tangent line is drawn from `(x1,y1)` to `(x2,y2)`.
- `y2`: The y-coordinate of the user space for the end point of the second tangent line. The second tangent line is drawn from `(x1,y1)` to `(x2,y2)`.
- `radius`: The radius of the arc, in user space coordinates.

## See Also

### Constructing a Graphics Path
- [CGPathMoveToPoint](./cgpathmovetopoint.md)
  Starts a new subpath at a specified location in a mutable graphics path.
- [CGPathAddLineToPoint](./cgpathaddlinetopoint.md)
  Appends a line segment to a mutable graphics path.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpathaddarctopoint)*
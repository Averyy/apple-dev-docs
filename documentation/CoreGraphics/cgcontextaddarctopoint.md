# CGContextAddArcToPoint

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Adds an arc of a circle to the current path, using a radius and tangent points.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern void CGContextAddArcToPoint(CGContextRef c, CGFloat x1, CGFloat y1, CGFloat x2, CGFloat y2, CGFloat radius);
```

## Discussion

This method calculates two tangent lines—the first from the current point to the point `(x1, y1)`, and the second from the point `(x1, y1)` to the point `(x2, y2)`—then calculates the start and end points for a circular arc of the specified radius such that the arc is tangent to both lines. Finally, this method approximates that arc with a sequence of cubic Bézier curves and appends those curves to the current path.

If the starting point of the arc (that is, the point where a circle of the specified radius must meet the first tangent line in order to also be tangent to the second line) is not the current point, this method appends a straight line segment from the current point to the starting point of the arc.

The ending point of the arc (that is, the point where a circle of the specified radius must meet the second tangent line in order to also be tangent to the first line) becomes the new current point of the path.

## Parameters

- `c`: A graphics context whose current path is not empty.
- `x1`: The x-value, in user space coordinates, for the end point of the first tangent line. The first tangent line is drawn from the current point to (x1,y1).
- `y1`: The y-value, in user space coordinates, for the end point of the first tangent line. The first tangent line is drawn from the current point to (x1,y1).
- `x2`: The x-value, in user space coordinates, for the end point of the second tangent line. The second tangent line is drawn from (x1,y1) to (x2,y2).
- `y2`: The y-value, in user space coordinates, for the end point of the second tangent line. The second tangent line is drawn from (x1,y1) to (x2,y2).
- `radius`: The radius of the arc, in user space coordinates.

## See Also

### Constructing a Current Graphics Path
- [func beginPath()](./cgcontext/beginpath%28%29.md)
  Creates a new empty path in a graphics context.
- [CGContextMoveToPoint](./cgcontextmovetopoint.md)
  Begins a new subpath at the point you specify.
- [CGContextAddLineToPoint](./cgcontextaddlinetopoint.md)
  Appends a straight line segment from the current point to the provided point .
- [CGContextAddLines](./cgcontextaddlines.md)
  Adds a sequence of connected straight-line segments to the current path.
- [func addRect(CGRect)](./cgcontext/addrect%28_%29.md)
  Adds a rectangular path to the current path.
- [CGContextAddRects](./cgcontextaddrects.md)
  Adds a set of rectangular paths to the current path.
- [func addEllipse(in: CGRect)](./cgcontext/addellipse%28in%29.md)
  Adds an ellipse that fits inside the specified rectangle.
- [CGContextAddArc](./cgcontextaddarc.md)
  Adds an arc of a circle to the current path, possibly preceded by a straight line segment
- [CGContextAddCurveToPoint](./cgcontextaddcurvetopoint.md)
  Appends a cubic Bézier curve from the current point, using the provided control points and end point .
- [CGContextAddQuadCurveToPoint](./cgcontextaddquadcurvetopoint.md)
  Appends a quadratic Bézier curve from the current point, using a control point and an end point you specify.
- [func addPath(CGPath)](./cgcontext/addpath%28_%29.md)
  Adds a previously created path object to the current path in a graphics context.
- [func closePath()](./cgcontext/closepath%28%29.md)
  Closes and terminates the current path’s subpath.
- [var path: CGPath?](./cgcontext/path.md)
  Returns a path object built from the current path information in a graphics context.
- [func replacePathWithStrokedPath()](./cgcontext/replacepathwithstrokedpath%28%29.md)
  Replaces the path in the graphics context with the stroked version of the path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontextaddarctopoint)*
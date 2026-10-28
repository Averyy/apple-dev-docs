# CGContextAddRects

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Adds a set of rectangular paths to the current path.

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
extern void CGContextAddRects(CGContextRef c, const CGRect *rects, size_t count);
```

## Discussion

This is a convenience function that adds an array of rectangles to a path, as if it called [`addRect(_:)`](./cgcontext/addrect%28_%29.md) for each rectangle.

## Parameters

- `c`: A graphics context.
- `rects`: An array of rectangles, specified in user space coordinates.
- `count`: The number of rectangles in the `rects` array.

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
- [func addEllipse(in: CGRect)](./cgcontext/addellipse%28in%29.md)
  Adds an ellipse that fits inside the specified rectangle.
- [CGContextAddArc](./cgcontextaddarc.md)
  Adds an arc of a circle to the current path, possibly preceded by a straight line segment
- [CGContextAddArcToPoint](./cgcontextaddarctopoint.md)
  Adds an arc of a circle to the current path, using a radius and tangent points.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontextaddrects)*
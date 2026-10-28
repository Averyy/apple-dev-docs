# CGPathAddRoundedRect

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Appends a rounded rectangle to a mutable graphics path.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern void CGPathAddRoundedRect(CGMutablePathRef path, const CGAffineTransform *transform, CGRect rect, CGFloat cornerWidth, CGFloat cornerHeight);
```

## Discussion

This is a convenience function that adds a path of an rounded rectangle.

Each corner of the rounded rectangle is one-quarter of an ellipse with axes equal to the `cornerWidth` and `cornerHeight` parameters. The rounded rectangle forms a complete subpath and is oriented in the clockwise direction.

## Parameters

- `path`: The mutable path to change.
- `transform`: A pointer to an affine transformation matrix, or `NULL` if no transformation is needed. If specified, Core Graphics applies the transformation to the rectangle before adding it to the path.
- `rect`: The rectangle to add.
- `cornerWidth`: The width of the rounded corner sections.
- `cornerHeight`: The height of the rounded corner sections.

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

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpathaddroundedrect)*
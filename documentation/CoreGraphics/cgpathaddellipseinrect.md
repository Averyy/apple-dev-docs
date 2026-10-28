# CGPathAddEllipseInRect

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Adds to a path an ellipse that fits inside a rectangle.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern void CGPathAddEllipseInRect(CGMutablePathRef path, const CGAffineTransform *m, CGRect rect);
```

## Discussion

The ellipse is approximated by a sequence of Bézier curves. Its center is the midpoint of the rectangle defined by the `rect` parameter. If the rectangle is square, then the ellipse is circular with a radius equal to one-half the width (or height) of the rectangle. If the `rect` parameter specifies a rectangular shape, then the major and minor axes of the ellipse are defined by the width and height of the rectangle.

The ellipse forms a complete subpath of the path—that is, the ellipse drawing starts with a move-to operation and ends with a close-subpath operation, with all moves oriented in the clockwise direction. If you supply an affine transform, then the constructed Bézier curves that define the ellipse are transformed before they are added to the path.

## Parameters

- `path`: The path to modify.
- `m`: An affine transform to apply to the ellipse, or `NULL` if you don’t want to transform the ellipse.
- `rect`: A rectangle to enclose the ellipse.

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

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpathaddellipseinrect)*
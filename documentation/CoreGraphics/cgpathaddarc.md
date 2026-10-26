# CGPathAddArc

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
extern void CGPathAddArc(CGMutablePathRef path, const CGAffineTransform *m, CGFloat x, CGFloat y, CGFloat radius, CGFloat startAngle, CGFloat endAngle, bool clockwise);
```

#### Discussion

An arc is a segment of a circle with radius r centered at a point `(x,y)`. When you call this function, you provide the center point, radius, and two angles in radians. Core Graphics uses this information to determine the end points of the arc, and then approximates the new arc using a sequence of cubic Bézier curves. The `clockwise` parameter determines the direction in which the arc is created. The actual direction may change depending on the coordinate system transformation applied to the path.

A transformation may be applied to the Bézier curves before they are added to the path. If no transform is needed, the second argument should be `NULL`.

If the specified path already contains a subpath, Core Graphics implicitly adds a line connecting the subpath’s current point to the beginning of the arc. If the path is empty, Core Graphics creates a new subpath with a starting point set to the starting point of the arc.

The ending point of the arc becomes the new current point of the path.

## Parameters

- `path`: The mutable graphics path to change.
- `m`: A pointer to an affine transformation matrix, or `NULL` if no transformation is needed. If specified, Core Graphics applies the transformation to the arc before it is added to the path.
- `x`: The x-coordinate of the center point of the arc.
- `y`: The y-coordinate of the center point of the arc.
- `radius`: The radius of the arc.
- `startAngle`: The angle (in radians) that determines the starting point of the arc, measured from the x-axis in the current user space.
- `endAngle`: The angle (in radians) that determines the ending point of the arc, measured from the x-axis in the current user space.
- `clockwise`: A Boolean value that specifies whether or not to draw the arc in the clockwise direction, before applying the transformation matrix.

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

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpathaddarc)*
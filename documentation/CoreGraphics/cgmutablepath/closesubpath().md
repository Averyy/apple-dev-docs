# closeSubpath()

**Framework**: Core Graphics  
**Kind**: method  
**Role**: Instance Method

Closes and completes a subpath in a mutable graphics path.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func closeSubpath()
```

```c
extern void CGPathCloseSubpath(CGMutablePathRef path);
```

## Discussion

Appends a line from the current point to the starting point of the current subpath and ends the subpath.

After closing the subpath, your application can begin a new subpath without first calling [`CGPathMoveToPoint`](../cgpathmovetopoint.md). In this case, a new subpath is implicitly created with a starting and current point equal to the previous subpath’s starting point.

## See Also

### Constructing a Graphics Path
- [func move(to: CGPoint, transform: CGAffineTransform)](./move%28to,transform%29.md)
  Begins a new subpath at the specified point.
- [func addLine(to: CGPoint, transform: CGAffineTransform)](./addline%28to,transform%29.md)
  Appends a straight line segment from the current point to the specified point.
- [func addLines(between: [CGPoint], transform: CGAffineTransform)](./addlines%28between,transform%29.md)
  Adds a sequence of connected straight-line segments to the path.
- [func addRect(CGRect, transform: CGAffineTransform)](./addrect%28_,transform%29.md)
  Adds a rectangular subpath to the path.
- [func addRects([CGRect], transform: CGAffineTransform)](./addrects%28_,transform%29.md)
  Adds a set of rectangular subpaths to the path.
- [func addEllipse(in: CGRect, transform: CGAffineTransform)](./addellipse%28in,transform%29.md)
  Adds an ellipse that fits inside the specified rectangle.
- [func addRoundedRect(in: CGRect, cornerWidth: CGFloat, cornerHeight: CGFloat, transform: CGAffineTransform)](./addroundedrect%28in,cornerwidth,cornerheight,transform%29.md)
  Adds a subpath to the path, in the shape of a rectangle with rounded corners.
- [func addArc(center: CGPoint, radius: CGFloat, startAngle: CGFloat, endAngle: CGFloat, clockwise: Bool, transform: CGAffineTransform)](./addarc%28center,radius,startangle,endangle,clockwise,transform%29.md)
  Adds an arc of a circle to the path, specified with a radius and angles.
- [func addArc(tangent1End: CGPoint, tangent2End: CGPoint, radius: CGFloat, transform: CGAffineTransform)](./addarc%28tangent1end,tangent2end,radius,transform%29.md)
  Adds an arc of a circle to the path, specified with a radius and two tangent lines.
- [func addRelativeArc(center: CGPoint, radius: CGFloat, startAngle: CGFloat, delta: CGFloat, transform: CGAffineTransform)](./addrelativearc%28center,radius,startangle,delta,transform%29.md)
  Adds an arc of a circle to the path, specified with a radius and a difference in angle.
- [func addCurve(to: CGPoint, control1: CGPoint, control2: CGPoint, transform: CGAffineTransform)](./addcurve%28to,control1,control2,transform%29.md)
  Adds a cubic Bézier curve to the path, with the specified end point and control points.
- [func addQuadCurve(to: CGPoint, control: CGPoint, transform: CGAffineTransform)](./addquadcurve%28to,control,transform%29.md)
  Adds a quadratic Bézier curve to the path, with the specified end point and control point.
- [func addPath(CGPath, transform: CGAffineTransform)](./addpath%28_,transform%29.md)
  Appends another path object to the path.
- [CGPathMoveToPoint](../cgpathmovetopoint.md)
  Starts a new subpath at a specified location in a mutable graphics path.
- [CGPathAddLineToPoint](../cgpathaddlinetopoint.md)
  Appends a line segment to a mutable graphics path.
- [CGPathAddLines](../cgpathaddlines.md)
  Appends an array of new line segments to a mutable graphics path.
- [CGPathAddRect](../cgpathaddrect.md)
  Appends a rectangle to a mutable graphics path.
- [CGPathAddRects](../cgpathaddrects.md)
  Appends an array of rectangles to a mutable graphics path.
- [CGPathAddEllipseInRect](../cgpathaddellipseinrect.md)
  Adds to a path an ellipse that fits inside a rectangle.
- [CGPathAddRoundedRect](../cgpathaddroundedrect.md)
  Appends a rounded rectangle to a mutable graphics path.
- [CGPathAddArc](../cgpathaddarc.md)
  Appends an arc to a mutable graphics path, possibly preceded by a straight line segment.
- [CGPathAddArcToPoint](../cgpathaddarctopoint.md)
  Appends an arc to a mutable graphics path, possibly preceded by a straight line segment.
- [CGPathAddRelativeArc](../cgpathaddrelativearc.md)
  Appends an arc to a mutable graphics path, possibly preceded by a straight line segment.
- [CGPathAddCurveToPoint](../cgpathaddcurvetopoint.md)
  Appends a cubic Bézier curve to a mutable graphics path.
- [CGPathAddQuadCurveToPoint](../cgpathaddquadcurvetopoint.md)
  Appends a quadratic Bézier curve to a mutable graphics path.
- [CGPathAddPath](../cgpathaddpath.md)
  Appends a path to onto a mutable graphics path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgmutablepath/closesubpath())*
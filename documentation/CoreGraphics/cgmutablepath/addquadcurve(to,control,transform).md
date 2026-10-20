# addQuadCurve(to:control:transform:)

**Framework**: Core Graphics  
**Kind**: method  
**Role**: Instance Method

Adds a quadratic Bézier curve to the path, with the specified end point and control point.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 7.0+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func addQuadCurve(to end: CGPoint, control: CGPoint, transform: CGAffineTransform = .identity)
```

#### Discussion

This method constructs a curve starting from the path’s current point and ending at the specified end point, with curvature defined by the control point. After this method appends that curve to the current path, the end point of the curve becomes the path’s current point.

## Parameters

- `end`: The point, in user space coordinates, at which to end the curve.
- `control`: The control point of the curve, in user space coordinates.
- `transform`: An affine transform to apply to the curve before adding to the path. Defaults to the identity transform if not specified.

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
- [func addPath(CGPath, transform: CGAffineTransform)](./addpath%28_,transform%29.md)
  Appends another path object to the path.
- [func closeSubpath()](./closesubpath%28%29.md)
  Closes and completes a subpath in a mutable graphics path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgmutablepath/addquadcurve(to:control:transform:))*
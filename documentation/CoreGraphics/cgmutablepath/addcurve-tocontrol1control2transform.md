# addCurve(to:control1:control2:transform:)

**Framework**: Core Graphics  
**Kind**: method

Adds a cubic Bézier curve to the path, with the specified end point and control points.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst ?+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func addCurve(to end: CGPoint, control1: CGPoint, control2: CGPoint, transform: CGAffineTransform = .identity)
```

#### Discussion

This method constructs a curve starting from the path’s current point and ending at the specified end point, with curvature defined by the two control points. After this method appends that curve to the current path, the end point of the curve becomes the path’s current point.

## Parameters

- `end`: The point, in user space coordinates, at which to end the curve.
- `control1`: The first control point of the curve, in user space coordinates.
- `control2`: The second control point of the curve, in user space coordinates.
- `transform`: An affine transform to apply to the curve before adding to the path. Defaults to the identity transform if not specified.

## See Also

- [func move(to: CGPoint, transform: CGAffineTransform)](cgmutablepath/move(to:transform:).md)
  Begins a new subpath at the specified point.
- [func addLine(to: CGPoint, transform: CGAffineTransform)](cgmutablepath/addline(to:transform:).md)
  Appends a straight line segment from the current point to the specified point.
- [func addLines(between: [CGPoint], transform: CGAffineTransform)](cgmutablepath/addlines(between:transform:).md)
  Adds a sequence of connected straight-line segments to the path.
- [func addRect(CGRect, transform: CGAffineTransform)](cgmutablepath/addrect(_:transform:).md)
  Adds a rectangular subpath to the path.
- [func addRects([CGRect], transform: CGAffineTransform)](cgmutablepath/addrects(_:transform:).md)
  Adds a set of rectangular subpaths to the path.
- [func addEllipse(in: CGRect, transform: CGAffineTransform)](cgmutablepath/addellipse(in:transform:).md)
  Adds an ellipse that fits inside the specified rectangle.
- [func addRoundedRect(in: CGRect, cornerWidth: CGFloat, cornerHeight: CGFloat, transform: CGAffineTransform)](cgmutablepath/addroundedrect(in:cornerwidth:cornerheight:transform:).md)
  Adds a subpath to the path, in the shape of a rectangle with rounded corners.
- [func addArc(center: CGPoint, radius: CGFloat, startAngle: CGFloat, endAngle: CGFloat, clockwise: Bool, transform: CGAffineTransform)](cgmutablepath/addarc(center:radius:startangle:endangle:clockwise:transform:).md)
  Adds an arc of a circle to the path, specified with a radius and angles.
- [func addArc(tangent1End: CGPoint, tangent2End: CGPoint, radius: CGFloat, transform: CGAffineTransform)](cgmutablepath/addarc(tangent1end:tangent2end:radius:transform:).md)
  Adds an arc of a circle to the path, specified with a radius and two tangent lines.
- [func addRelativeArc(center: CGPoint, radius: CGFloat, startAngle: CGFloat, delta: CGFloat, transform: CGAffineTransform)](cgmutablepath/addrelativearc(center:radius:startangle:delta:transform:).md)
  Adds an arc of a circle to the path, specified with a radius and a difference in angle.
- [func addQuadCurve(to: CGPoint, control: CGPoint, transform: CGAffineTransform)](cgmutablepath/addquadcurve(to:control:transform:).md)
  Adds a quadratic Bézier curve to the path, with the specified end point and control point.
- [func addPath(CGPath, transform: CGAffineTransform)](cgmutablepath/addpath(_:transform:).md)
  Appends another path object to the path.
- [func closeSubpath()](cgmutablepath/closesubpath.md)
  Closes and completes a subpath in a mutable graphics path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgmutablepath/addcurve(to:control1:control2:transform:))*
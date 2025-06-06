# closeSubpath()

**Framework**: Core Graphics  
**Kind**: method

Closes and completes a subpath in a mutable graphics path.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func closeSubpath()
```

#### Discussion

Appends a line from the current point to the starting point of the current subpath and ends the subpath.

After closing the subpath, your application can begin a new subpath without first calling [`CGPathMoveToPoint`](cgpathmovetopoint.md). In this case, a new subpath is implicitly created with a starting and current point equal to the previous subpath’s starting point.

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
- [func addCurve(to: CGPoint, control1: CGPoint, control2: CGPoint, transform: CGAffineTransform)](cgmutablepath/addcurve(to:control1:control2:transform:).md)
  Adds a cubic Bézier curve to the path, with the specified end point and control points.
- [func addQuadCurve(to: CGPoint, control: CGPoint, transform: CGAffineTransform)](cgmutablepath/addquadcurve(to:control:transform:).md)
  Adds a quadratic Bézier curve to the path, with the specified end point and control point.
- [func addPath(CGPath, transform: CGAffineTransform)](cgmutablepath/addpath(_:transform:).md)
  Appends another path object to the path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgmutablepath/closesubpath())*
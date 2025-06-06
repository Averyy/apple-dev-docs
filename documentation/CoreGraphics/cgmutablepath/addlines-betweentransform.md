# addLines(between:transform:)

**Framework**: Core Graphics  
**Kind**: method

Adds a sequence of connected straight-line segments to the path.

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
func addLines(between points: [CGPoint], transform: CGAffineTransform = .identity)
```

#### Discussion

Calling this convenience method is equivalent to calling the [`move(to:transform:)`](cgmutablepath/move(to:transform:).md) method with the first value in the `points` array, then calling the [`addLine(to:transform:)`](cgmutablepath/addline(to:transform:).md) method for each subsequent point until the array is exhausted. After calling this method, the path’s current point is the last point in the array.

## Parameters

- `points`: An array of values that specify the start and end points of the line segments to draw. Each point in the array specifies a position in user space. The first point in the array specifies the initial starting point.
- `transform`: An affine transform to apply to the points before adding to the path. Defaults to the identity transform if not specified.

## See Also

- [func move(to: CGPoint, transform: CGAffineTransform)](cgmutablepath/move(to:transform:).md)
  Begins a new subpath at the specified point.
- [func addLine(to: CGPoint, transform: CGAffineTransform)](cgmutablepath/addline(to:transform:).md)
  Appends a straight line segment from the current point to the specified point.
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
- [func closeSubpath()](cgmutablepath/closesubpath.md)
  Closes and completes a subpath in a mutable graphics path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgmutablepath/addlines(between:transform:))*
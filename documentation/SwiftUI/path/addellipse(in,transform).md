# addEllipse(in:transform:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Adds an ellipse that fits inside the specified rectangle to the path.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
mutating func addEllipse(in rect: CGRect, transform: CGAffineTransform = .identity)
```

## Discussion

The ellipse is approximated by a sequence of Bézier curves. Its center is the midpoint of the rectangle defined by the `rect` parameter. If the rectangle is square, then the ellipse is circular with a radius equal to one-half the width (or height) of the rectangle. If the `rect` parameter specifies a rectangular shape, then the major and minor axes of the ellipse are defined by the width and height of the rectangle.

The ellipse forms a complete subpath of the path— that is, the ellipse drawing starts with a move-to operation and ends with a close-subpath operation, with all moves oriented in the clockwise direction.

- Parameter:

  - rect: A rectangle that defines the area for the ellipse to fit in.
  - transform: An affine transform to apply to the ellipse before adding to the path. Defaults to the identity transform if not specified.

## See Also

### Drawing a path
- [func move(to: CGPoint)](./move%28to%29.md)
  Begins a new subpath at the specified point.
- [func addArc(center: CGPoint, radius: CGFloat, startAngle: Angle, endAngle: Angle, clockwise: Bool, transform: CGAffineTransform)](./addarc%28center,radius,startangle,endangle,clockwise,transform%29.md)
  Adds an arc of a circle to the path, specified with a radius and angles.
- [func addArc(tangent1End: CGPoint, tangent2End: CGPoint, radius: CGFloat, transform: CGAffineTransform)](./addarc%28tangent1end,tangent2end,radius,transform%29.md)
  Adds an arc of a circle to the path, specified with a radius and two tangent lines.
- [func addCurve(to: CGPoint, control1: CGPoint, control2: CGPoint)](./addcurve%28to,control1,control2%29.md)
  Adds a cubic Bézier curve to the path, with the specified end point and control points.
- [func addLine(to: CGPoint)](./addline%28to%29.md)
  Appends a straight line segment from the current point to the specified point.
- [func addLines([CGPoint])](./addlines%28_%29.md)
  Adds a sequence of connected straight-line segments to the path.
- [func addPath(Path, transform: CGAffineTransform)](./addpath%28_,transform%29.md)
  Appends another path value to this path.
- [func addQuadCurve(to: CGPoint, control: CGPoint)](./addquadcurve%28to,control%29.md)
  Adds a quadratic Bézier curve to the path, with the specified end point and control point.
- [func addRect(CGRect, transform: CGAffineTransform)](./addrect%28_,transform%29.md)
  Adds a rectangular subpath to the path.
- [func addRects([CGRect], transform: CGAffineTransform)](./addrects%28_,transform%29.md)
  Adds a set of rectangular subpaths to the path.
- [func addRelativeArc(center: CGPoint, radius: CGFloat, startAngle: Angle, delta: Angle, transform: CGAffineTransform)](./addrelativearc%28center,radius,startangle,delta,transform%29.md)
  Adds an arc of a circle to the path, specified with a radius and a difference in angle.
- [func addRoundedRect(in: CGRect, cornerSize: CGSize, style: RoundedCornerStyle, transform: CGAffineTransform)](./addroundedrect%28in,cornersize,style,transform%29.md)
  Adds a rounded rectangle to the path.
- [func closeSubpath()](./closesubpath%28%29.md)
  Closes and completes the current subpath.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/path/addellipse(in:transform:))*
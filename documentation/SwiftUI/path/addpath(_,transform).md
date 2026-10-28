# addPath(_:transform:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Appends another path value to this path.

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
mutating func addPath(_ path: Path, transform: CGAffineTransform = .identity)
```

## Discussion

If the `path` parameter is a non-empty empty path, its elements are appended in order to this path. Afterward, the start point and current point of this path are those of the last subpath in the `path` parameter.

## Parameters

- `path`: The path to add.
- `transform`: An affine transform to apply to the path parameter before adding to this path. Defaults to the identity transform if not specified.

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
- [func addEllipse(in: CGRect, transform: CGAffineTransform)](./addellipse%28in,transform%29.md)
  Adds an ellipse that fits inside the specified rectangle to the path.
- [func addLine(to: CGPoint)](./addline%28to%29.md)
  Appends a straight line segment from the current point to the specified point.
- [func addLines([CGPoint])](./addlines%28_%29.md)
  Adds a sequence of connected straight-line segments to the path.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/path/addpath(_:transform:))*
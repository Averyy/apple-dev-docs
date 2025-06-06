# addLine(to:)

**Framework**: SwiftUI  
**Kind**: method

Appends a straight line segment from the current point to the specified point.

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
mutating func addLine(to end: CGPoint)
```

#### Discussion

After adding the line segment, the current point is set to the endpoint of the line segment.

## Parameters

- `end`: The location, in user space coordinates, for the   end of the new line segment.

## See Also

- [func move(to: CGPoint)](path/move(to:).md)
  Begins a new subpath at the specified point.
- [func addArc(center: CGPoint, radius: CGFloat, startAngle: Angle, endAngle: Angle, clockwise: Bool, transform: CGAffineTransform)](path/addarc(center:radius:startangle:endangle:clockwise:transform:).md)
  Adds an arc of a circle to the path, specified with a radius and angles.
- [func addArc(tangent1End: CGPoint, tangent2End: CGPoint, radius: CGFloat, transform: CGAffineTransform)](path/addarc(tangent1end:tangent2end:radius:transform:).md)
  Adds an arc of a circle to the path, specified with a radius and two tangent lines.
- [func addCurve(to: CGPoint, control1: CGPoint, control2: CGPoint)](path/addcurve(to:control1:control2:).md)
  Adds a cubic Bézier curve to the path, with the specified end point and control points.
- [func addEllipse(in: CGRect, transform: CGAffineTransform)](path/addellipse(in:transform:).md)
  Adds an ellipse that fits inside the specified rectangle to the path.
- [func addLines([CGPoint])](path/addlines(_:).md)
  Adds a sequence of connected straight-line segments to the path.
- [func addPath(Path, transform: CGAffineTransform)](path/addpath(_:transform:).md)
  Appends another path value to this path.
- [func addQuadCurve(to: CGPoint, control: CGPoint)](path/addquadcurve(to:control:).md)
  Adds a quadratic Bézier curve to the path, with the specified end point and control point.
- [func addRect(CGRect, transform: CGAffineTransform)](path/addrect(_:transform:).md)
  Adds a rectangular subpath to the path.
- [func addRects([CGRect], transform: CGAffineTransform)](path/addrects(_:transform:).md)
  Adds a set of rectangular subpaths to the path.
- [func addRelativeArc(center: CGPoint, radius: CGFloat, startAngle: Angle, delta: Angle, transform: CGAffineTransform)](path/addrelativearc(center:radius:startangle:delta:transform:).md)
  Adds an arc of a circle to the path, specified with a radius and a difference in angle.
- [func addRoundedRect(in: CGRect, cornerSize: CGSize, style: RoundedCornerStyle, transform: CGAffineTransform)](path/addroundedrect(in:cornersize:style:transform:).md)
  Adds a rounded rectangle to the path.
- [func closeSubpath()](path/closesubpath.md)
  Closes and completes the current subpath.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/path/addline(to:))*
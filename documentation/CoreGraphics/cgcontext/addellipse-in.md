# addEllipse(in:)

**Framework**: Core Graphics  
**Kind**: method

Adds an ellipse that fits inside the specified rectangle.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func addEllipse(in rect: CGRect)
```

#### Discussion

The ellipse is approximated by a sequence of Bézier curves. Its center is the midpoint of the rectangle defined by the `rect` parameter. If the rectangle is square, then the ellipse is circular with a radius equal to one-half the width (or height) of the rectangle. If the `rect` parameter specifies a rectangular shape, then the major and minor axes of the ellipse are defined by the width and height of the rectangle.

The ellipse forms a complete subpath of the path—that is, the ellipse drawing starts with a move-to operation and ends with a close-subpath operation, with all moves oriented in the clockwise direction.

## Parameters

- `rect`: A rectangle that defines the area for the ellipse to fit in.

## See Also

- [func beginPath()](cgcontext/beginpath.md)
  Creates a new empty path in a graphics context.
- [func move(to: CGPoint)](cgcontext/move(to:).md)
  Begins a new subpath at the specified point.
- [func addLine(to: CGPoint)](cgcontext/addline(to:).md)
  Appends a straight line segment from the current point to the specified point.
- [func addLines(between: [CGPoint])](cgcontext/addlines(between:).md)
  Adds a sequence of connected straight-line segments to the current path.
- [func addRect(CGRect)](cgcontext/addrect(_:).md)
  Adds a rectangular path to the current path.
- [func addRects([CGRect])](cgcontext/addrects(_:).md)
  Adds a set of rectangular paths to the current path.
- [func addArc(center: CGPoint, radius: CGFloat, startAngle: CGFloat, endAngle: CGFloat, clockwise: Bool)](cgcontext/addarc(center:radius:startangle:endangle:clockwise:).md)
  Adds an arc of a circle to the current path, specified with a radius and angles.
- [func addArc(tangent1End: CGPoint, tangent2End: CGPoint, radius: CGFloat)](cgcontext/addarc(tangent1end:tangent2end:radius:).md)
  Adds an arc of a circle to the current path, specified with a radius and two tangent lines.
- [func addCurve(to: CGPoint, control1: CGPoint, control2: CGPoint)](cgcontext/addcurve(to:control1:control2:).md)
  Adds a cubic Bézier curve to the current path, with the specified end point and control points.
- [func addQuadCurve(to: CGPoint, control: CGPoint)](cgcontext/addquadcurve(to:control:).md)
  Adds a quadratic Bézier curve to the current path, with the specified end point and control point.
- [func addPath(CGPath)](cgcontext/addpath(_:).md)
  Adds a previously created path object to the current path in a graphics context.
- [func closePath()](cgcontext/closepath.md)
  Closes and terminates the current path’s subpath.
- [var path: CGPath?](cgcontext/path.md)
  Returns a path object built from the current path information in a graphics context.
- [func replacePathWithStrokedPath()](cgcontext/replacepathwithstrokedpath.md)
  Replaces the path in the graphics context with the stroked version of the path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/addellipse(in:))*
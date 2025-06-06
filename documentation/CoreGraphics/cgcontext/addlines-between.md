# addLines(between:)

**Framework**: Core Graphics  
**Kind**: method

Adds a sequence of connected straight-line segments to the current path.

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
func addLines(between points: [CGPoint])
```

#### Discussion

Calling this convenience method is equivalent to calling the [`move(to:)`](cgcontext/move(to:).md) method with the first value in the points array, then calling the [`addLine(to:)`](cgcontext/addline(to:).md) method for each subsequent point until the array is exhausted. After calling this method, the path’s current point is the last point in the array.

## Parameters

- `points`: An array of values that specify the start and end points of the line segments to draw. Each point in the array specifies a position in user space. The first point in the array specifies the initial starting point.

## See Also

- [func beginPath()](cgcontext/beginpath.md)
  Creates a new empty path in a graphics context.
- [func move(to: CGPoint)](cgcontext/move(to:).md)
  Begins a new subpath at the specified point.
- [func addLine(to: CGPoint)](cgcontext/addline(to:).md)
  Appends a straight line segment from the current point to the specified point.
- [func addRect(CGRect)](cgcontext/addrect(_:).md)
  Adds a rectangular path to the current path.
- [func addRects([CGRect])](cgcontext/addrects(_:).md)
  Adds a set of rectangular paths to the current path.
- [func addEllipse(in: CGRect)](cgcontext/addellipse(in:).md)
  Adds an ellipse that fits inside the specified rectangle.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/addlines(between:))*
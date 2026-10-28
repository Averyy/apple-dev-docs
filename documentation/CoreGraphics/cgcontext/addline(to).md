# addLine(to:)

**Framework**: Core Graphics  
**Kind**: method  
**Role**: Instance Method

Appends a straight line segment from the current point to the specified point.

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
func addLine(to point: CGPoint)
```

## Discussion

After adding the line segment, the current point is set to the endpoint of the line segment.

## Parameters

- `point`: The location, in user space coordinates, for the end of the new line segment.

## See Also

### Constructing a Current Graphics Path
- [func beginPath()](./beginpath%28%29.md)
  Creates a new empty path in a graphics context.
- [func move(to: CGPoint)](./move%28to%29.md)
  Begins a new subpath at the specified point.
- [func addLines(between: [CGPoint])](./addlines%28between%29.md)
  Adds a sequence of connected straight-line segments to the current path.
- [func addRect(CGRect)](./addrect%28_%29.md)
  Adds a rectangular path to the current path.
- [func addRects([CGRect])](./addrects%28_%29.md)
  Adds a set of rectangular paths to the current path.
- [func addEllipse(in: CGRect)](./addellipse%28in%29.md)
  Adds an ellipse that fits inside the specified rectangle.
- [func addArc(center: CGPoint, radius: CGFloat, startAngle: CGFloat, endAngle: CGFloat, clockwise: Bool)](./addarc%28center,radius,startangle,endangle,clockwise%29.md)
  Adds an arc of a circle to the current path, specified with a radius and angles.
- [func addArc(tangent1End: CGPoint, tangent2End: CGPoint, radius: CGFloat)](./addarc%28tangent1end,tangent2end,radius%29.md)
  Adds an arc of a circle to the current path, specified with a radius and two tangent lines.
- [func addCurve(to: CGPoint, control1: CGPoint, control2: CGPoint)](./addcurve%28to,control1,control2%29.md)
  Adds a cubic Bézier curve to the current path, with the specified end point and control points.
- [func addQuadCurve(to: CGPoint, control: CGPoint)](./addquadcurve%28to,control%29.md)
  Adds a quadratic Bézier curve to the current path, with the specified end point and control point.
- [func addPath(CGPath)](./addpath%28_%29.md)
  Adds a previously created path object to the current path in a graphics context.
- [func closePath()](./closepath%28%29.md)
  Closes and terminates the current path’s subpath.
- [var path: CGPath?](./path.md)
  Returns a path object built from the current path information in a graphics context.
- [func replacePathWithStrokedPath()](./replacepathwithstrokedpath%28%29.md)
  Replaces the path in the graphics context with the stroked version of the path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/addline(to:))*
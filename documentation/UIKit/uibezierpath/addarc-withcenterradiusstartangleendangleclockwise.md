# addArc(withCenter:radius:startAngle:endAngle:clockwise:)

**Framework**: UIKit  
**Kind**: method

Appends an arc to the path.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func addArc(withCenter center: CGPoint, radius: CGFloat, startAngle: CGFloat, endAngle: CGFloat, clockwise: Bool)
```

#### Discussion

This method adds the specified arc beginning at the current point. The created arc lies on the perimeter of the specified circle. When drawn in the default coordinate system, the start and end angles are based on the unit circle shown in the image in [`init(arcCenter:radius:startAngle:endAngle:clockwise:)`](uibezierpath/init(arccenter:radius:startangle:endangle:clockwise:).md). For example, specifying a start angle of `0` radians, an end angle of `π` radians, and setting the `clockwise` parameter to [`true`](https://developer.apple.com/documentation/swift/true) draws the bottom half of the circle. However, specifying the same start and end angles but setting the `clockwise` parameter set to [`false`](https://developer.apple.com/documentation/swift/false) draws the top half of the circle.

After calling this method, the current point is set to the point on the arc at the end angle of the circle.

## Parameters

- `center`: Specifies the center point of the circle (in the current coordinate system) used to define the arc.
- `radius`: Specifies the radius of the circle used to define the arc.
- `startAngle`: Specifies the starting angle of the arc (measured in radians).
- `endAngle`: Specifies the end angle of the arc (measured in radians).
- `clockwise`: The direction in which to draw the arc.

## See Also

- [func move(to: CGPoint)](uibezierpath/move(to:).md)
  Moves the path’s current point to the specified location.
- [func addLine(to: CGPoint)](uibezierpath/addline(to:).md)
  Appends a straight line to the path.
- [func addCurve(to: CGPoint, controlPoint1: CGPoint, controlPoint2: CGPoint)](uibezierpath/addcurve(to:controlpoint1:controlpoint2:).md)
  Appends a cubic Bézier curve to the path.
- [func addQuadCurve(to: CGPoint, controlPoint: CGPoint)](uibezierpath/addquadcurve(to:controlpoint:).md)
  Appends a quadratic Bézier curve to the path.
- [func close()](uibezierpath/close.md)
  Closes the most recent subpath.
- [func removeAllPoints()](uibezierpath/removeallpoints.md)
  Removes all points from the path, effectively deleting all subpaths.
- [func append(UIBezierPath)](uibezierpath/append(_:).md)
  Appends the contents of the specified path object to the path.
- [var cgPath: CGPath](uibezierpath/cgpath.md)
  The Core Graphics representation of the path.
- [var currentPoint: CGPoint](uibezierpath/currentpoint.md)
  The current point in the graphics path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibezierpath/addarc(withcenter:radius:startangle:endangle:clockwise:))*
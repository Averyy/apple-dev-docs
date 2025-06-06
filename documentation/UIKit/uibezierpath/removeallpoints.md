# removeAllPoints()

**Framework**: UIKit  
**Kind**: method

Removes all points from the path, effectively deleting all subpaths.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func removeAllPoints()
```

## See Also

- [func move(to: CGPoint)](uibezierpath/move(to:).md)
  Moves the path’s current point to the specified location.
- [func addLine(to: CGPoint)](uibezierpath/addline(to:).md)
  Appends a straight line to the path.
- [func addArc(withCenter: CGPoint, radius: CGFloat, startAngle: CGFloat, endAngle: CGFloat, clockwise: Bool)](uibezierpath/addarc(withcenter:radius:startangle:endangle:clockwise:).md)
  Appends an arc to the path.
- [func addCurve(to: CGPoint, controlPoint1: CGPoint, controlPoint2: CGPoint)](uibezierpath/addcurve(to:controlpoint1:controlpoint2:).md)
  Appends a cubic Bézier curve to the path.
- [func addQuadCurve(to: CGPoint, controlPoint: CGPoint)](uibezierpath/addquadcurve(to:controlpoint:).md)
  Appends a quadratic Bézier curve to the path.
- [func close()](uibezierpath/close.md)
  Closes the most recent subpath.
- [func append(UIBezierPath)](uibezierpath/append(_:).md)
  Appends the contents of the specified path object to the path.
- [var cgPath: CGPath](uibezierpath/cgpath.md)
  The Core Graphics representation of the path.
- [var currentPoint: CGPoint](uibezierpath/currentpoint.md)
  The current point in the graphics path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibezierpath/removeallpoints())*
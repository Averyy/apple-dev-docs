# addLine(to:)

**Framework**: UIKit  
**Kind**: method

Appends a straight line to the path.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func addLine(to point: CGPoint)
```

#### Discussion

This method creates a straight line segment starting at the current point and ending at the point specified by the `point` parameter. After adding the line segment, this method updates the current point to the value in `point`.

You must set the path’s current point (using the [`move(to:)`](uibezierpath/move(to:).md) method or through the previous creation of a line or curve segment) before you call this method. If the path is empty, this method does nothing.

## Parameters

- `point`: The destination point of the line segment, specified in the current coordinate system.

## See Also

- [func move(to: CGPoint)](uibezierpath/move(to:).md)
  Moves the path’s current point to the specified location.
- [func addArc(withCenter: CGPoint, radius: CGFloat, startAngle: CGFloat, endAngle: CGFloat, clockwise: Bool)](uibezierpath/addarc(withcenter:radius:startangle:endangle:clockwise:).md)
  Appends an arc to the path.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibezierpath/addline(to:))*
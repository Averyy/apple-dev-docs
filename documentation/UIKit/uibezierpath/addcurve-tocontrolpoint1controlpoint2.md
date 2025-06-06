# addCurve(to:controlPoint1:controlPoint2:)

**Framework**: UIKit  
**Kind**: method

Appends a cubic Bézier curve to the path.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func addCurve(to endPoint: CGPoint, controlPoint1: CGPoint, controlPoint2: CGPoint)
```

#### Discussion

This method appends a cubic Bézier curve from the current point to the end point specified by the `endPoint` parameter. The two control points define the curvature of the segment. The following image shows an approximation of a cubic Bézier curve given a set of initial points. The exact curvature of the segment involves a complex mathematical relationship between all of the points and is well documented online.

![None](https://docs-assets.developer.apple.com/published/615a19473ab60e5ab20b0c06477bafd3/media-1965856.jpg)

You must set the path’s current point (using the [`move(to:)`](uibezierpath/move(to:).md) method or through the previous creation of a line or curve segment) before you call this method. If the path is empty, this method does nothing. After adding the curve segment, this method updates the current point to the value in `point`.

## Parameters

- `endPoint`: The end point of the curve.
- `controlPoint1`: The first control point to use when computing the curve.
- `controlPoint2`: The second control point to use when computing the curve.

## See Also

- [func move(to: CGPoint)](uibezierpath/move(to:).md)
  Moves the path’s current point to the specified location.
- [func addLine(to: CGPoint)](uibezierpath/addline(to:).md)
  Appends a straight line to the path.
- [func addArc(withCenter: CGPoint, radius: CGFloat, startAngle: CGFloat, endAngle: CGFloat, clockwise: Bool)](uibezierpath/addarc(withcenter:radius:startangle:endangle:clockwise:).md)
  Appends an arc to the path.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibezierpath/addcurve(to:controlpoint1:controlpoint2:))*
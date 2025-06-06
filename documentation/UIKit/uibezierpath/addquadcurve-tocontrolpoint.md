# addQuadCurve(to:controlPoint:)

**Framework**: UIKit  
**Kind**: method

Appends a quadratic Bézier curve to the path.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func addQuadCurve(to endPoint: CGPoint, controlPoint: CGPoint)
```

#### Discussion

This method appends a quadratic Bézier curve from the current point to the end point specified by the `endPoint` parameter. The relationships between the current point, control point, and end point are what defines the actual curve. The following image shows some examples of quadratic curves and the approximate curve shape based on some sample points. The exact curvature of the segment involves a complex mathematical relationship between the points and is well documented online.

![None](https://docs-assets.developer.apple.com/published/a44987bfb6a4516273a636cbbca7e5d8/media-1965858.jpg)

You must set the path’s current point (using the [`move(to:)`](uibezierpath/move(to:).md) method or through the previous creation of a line or curve segment) before you call this method. If the path is empty, this method does nothing. After adding the curve segment, this method updates the current point to the value in `point`.

## Parameters

- `endPoint`: The end point of the curve.
- `controlPoint`: The control point of the curve.

## See Also

- [func move(to: CGPoint)](uibezierpath/move(to:).md)
  Moves the path’s current point to the specified location.
- [func addLine(to: CGPoint)](uibezierpath/addline(to:).md)
  Appends a straight line to the path.
- [func addArc(withCenter: CGPoint, radius: CGFloat, startAngle: CGFloat, endAngle: CGFloat, clockwise: Bool)](uibezierpath/addarc(withcenter:radius:startangle:endangle:clockwise:).md)
  Appends an arc to the path.
- [func addCurve(to: CGPoint, controlPoint1: CGPoint, controlPoint2: CGPoint)](uibezierpath/addcurve(to:controlpoint1:controlpoint2:).md)
  Appends a cubic Bézier curve to the path.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibezierpath/addquadcurve(to:controlpoint:))*
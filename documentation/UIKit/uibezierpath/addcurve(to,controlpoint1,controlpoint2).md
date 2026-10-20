# addCurve(to:controlPoint1:controlPoint2:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Appends a cubic Bézier curve to the path.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func addCurve(to endPoint: CGPoint, controlPoint1: CGPoint, controlPoint2: CGPoint)
```

```objc
- (void) addCurveToPoint:(CGPoint) endPoint controlPoint1:(CGPoint) controlPoint1 controlPoint2:(CGPoint) controlPoint2;
```

#### Discussion

This method appends a cubic Bézier curve from the current point to the end point specified by the `endPoint` parameter. The two control points define the curvature of the segment. The following image shows an approximation of a cubic Bézier curve given a set of initial points. The exact curvature of the segment involves a complex mathematical relationship between all of the points and is well documented online.

![A diagram of a cubic Bézier curve. A smooth curve runs from a point labeled Start point on the left to a point labeled Endpoint on the right. Dashed lines connect the start point to Control point 1 above the curve and the endpoint to Control point 2 below it.](https://developer.apple.com/tutorials/images/com.apple.uikit/media-1965856.jpg)

You must set the path’s current point (using the [`move(to:)`](./move%28to%29.md) method or through the previous creation of a line or curve segment) before you call this method. If the path is empty, this method does nothing. After adding the curve segment, this method updates the current point to the value in `point`.

## Parameters

- `endPoint`: The end point of the curve.
- `controlPoint1`: The first control point to use when computing the curve.
- `controlPoint2`: The second control point to use when computing the curve.

## See Also

### Constructing a path
- [func move(to: CGPoint)](./move%28to%29.md)
  Moves the path’s current point to the specified location.
- [func addLine(to: CGPoint)](./addline%28to%29.md)
  Appends a straight line to the path.
- [func addArc(withCenter: CGPoint, radius: CGFloat, startAngle: CGFloat, endAngle: CGFloat, clockwise: Bool)](./addarc%28withcenter,radius,startangle,endangle,clockwise%29.md)
  Appends an arc to the path.
- [func addQuadCurve(to: CGPoint, controlPoint: CGPoint)](./addquadcurve%28to,controlpoint%29.md)
  Appends a quadratic Bézier curve to the path.
- [func close()](./close%28%29.md)
  Closes the most recent subpath.
- [func removeAllPoints()](./removeallpoints%28%29.md)
  Removes all points from the path, effectively deleting all subpaths.
- [func append(UIBezierPath)](./append%28_%29.md)
  Appends the contents of the specified path object to the path.
- [var cgPath: CGPath](./cgpath.md)
  The Core Graphics representation of the path.
- [var currentPoint: CGPoint](./currentpoint.md)
  The current point in the graphics path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibezierpath/addcurve(to:controlpoint1:controlpoint2:))*
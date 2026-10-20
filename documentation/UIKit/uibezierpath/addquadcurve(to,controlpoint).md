# addQuadCurve(to:controlPoint:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Appends a quadratic Bézier curve to the path.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func addQuadCurve(to endPoint: CGPoint, controlPoint: CGPoint)
```

```objc
- (void) addQuadCurveToPoint:(CGPoint) endPoint controlPoint:(CGPoint) controlPoint;
```

#### Discussion

This method appends a quadratic Bézier curve from the current point to the end point specified by the `endPoint` parameter. The relationships between the current point, control point, and end point are what defines the actual curve. The following image shows some examples of quadratic curves and the approximate curve shape based on some sample points. The exact curvature of the segment involves a complex mathematical relationship between the points and is well documented online.

![A diagram showing two examples of quadratic Bézier curves, each with a current point labeled A, a control point labeled B, and an endpoint labeled C. In the left example, the control point sits directly above the current point, and the curve bows up and to the left before descending to the endpoint. In the right example, the control point sits above and between the other two points, and the curve forms a symmetrical arch. Dashed lines connect the control point to the current point and the endpoint in each example.](https://developer.apple.com/tutorials/images/com.apple.uikit/media-1965858.jpg)

You must set the path’s current point (using the [`move(to:)`](./move%28to%29.md) method or through the previous creation of a line or curve segment) before you call this method. If the path is empty, this method does nothing. After adding the curve segment, this method updates the current point to the value in `point`.

## Parameters

- `endPoint`: The end point of the curve.
- `controlPoint`: The control point of the curve.

## See Also

### Constructing a path
- [func move(to: CGPoint)](./move%28to%29.md)
  Moves the path’s current point to the specified location.
- [func addLine(to: CGPoint)](./addline%28to%29.md)
  Appends a straight line to the path.
- [func addArc(withCenter: CGPoint, radius: CGFloat, startAngle: CGFloat, endAngle: CGFloat, clockwise: Bool)](./addarc%28withcenter,radius,startangle,endangle,clockwise%29.md)
  Appends an arc to the path.
- [func addCurve(to: CGPoint, controlPoint1: CGPoint, controlPoint2: CGPoint)](./addcurve%28to,controlpoint1,controlpoint2%29.md)
  Appends a cubic Bézier curve to the path.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibezierpath/addquadcurve(to:controlpoint:))*
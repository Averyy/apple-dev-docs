# addLine(to:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Appends a straight line to the path.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func addLine(to point: CGPoint)
```

```objc
- (void) addLineToPoint:(CGPoint) point;
```

## Discussion

This method creates a straight line segment starting at the current point and ending at the point specified by the `point` parameter. After adding the line segment, this method updates the current point to the value in `point`.

You must set the path’s current point (using the [`move(to:)`](./move%28to%29.md) method or through the previous creation of a line or curve segment) before you call this method. If the path is empty, this method does nothing.

## Parameters

- `point`: The destination point of the line segment, specified in the current coordinate system.

## See Also

### Constructing a path
- [func move(to: CGPoint)](./move%28to%29.md)
  Moves the path’s current point to the specified location.
- [func addArc(withCenter: CGPoint, radius: CGFloat, startAngle: CGFloat, endAngle: CGFloat, clockwise: Bool)](./addarc%28withcenter,radius,startangle,endangle,clockwise%29.md)
  Appends an arc to the path.
- [func addCurve(to: CGPoint, controlPoint1: CGPoint, controlPoint2: CGPoint)](./addcurve%28to,controlpoint1,controlpoint2%29.md)
  Appends a cubic Bézier curve to the path.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibezierpath/addline(to:))*
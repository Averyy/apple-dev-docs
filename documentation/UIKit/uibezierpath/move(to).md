# move(to:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Moves the path’s current point to the specified location.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func move(to point: CGPoint)
```

```objc
- (void) moveToPoint:(CGPoint) point;
```

## Discussion

This method implicitly ends the current subpath (if any) and sets the current point to the value in the `point` parameter. When ending the previous subpath, this method does not actually close the subpath. Therefore, the first and last points of the previous subpath are not connected to each other.

For many path operations, you must call this method before issuing any commands that cause a line or curve segment to be drawn.

## Parameters

- `point`: A point in the current coordinate system.

## See Also

### Constructing a path
- [func addLine(to: CGPoint)](./addline%28to%29.md)
  Appends a straight line to the path.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibezierpath/move(to:))*
# append(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Appends the contents of the specified path object to the path.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func append(_ bezierPath: UIBezierPath)
```

```objc
- (void) appendPath:(UIBezierPath *) bezierPath;
```

#### Discussion

This method adds the commands used to create the path in `bezierPath` to the end of the receiver’s path. This method does not explicitly try to connect the subpaths in the two objects, although the operations in `bezierPath` might still cause that effect.

## Parameters

- `bezierPath`: The path to add to the receiver.

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
- [func addQuadCurve(to: CGPoint, controlPoint: CGPoint)](./addquadcurve%28to,controlpoint%29.md)
  Appends a quadratic Bézier curve to the path.
- [func close()](./close%28%29.md)
  Closes the most recent subpath.
- [func removeAllPoints()](./removeallpoints%28%29.md)
  Removes all points from the path, effectively deleting all subpaths.
- [var cgPath: CGPath](./cgpath.md)
  The Core Graphics representation of the path.
- [var currentPoint: CGPoint](./currentpoint.md)
  The current point in the graphics path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibezierpath/append(_:))*
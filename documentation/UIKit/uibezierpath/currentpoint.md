# currentPoint

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The current point in the graphics path.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var currentPoint: CGPoint { get }
```

```objc
@property (nonatomic, readonly) CGPoint currentPoint;
```

## Discussion

The value in this property represents the starting point for new line and curve segments. If the path is currently empty, this property contains the value [`CGPointZero`](../../CoreGraphics/cgpointzero.md).

## See Also

### Related Documentation
- [var isEmpty: Bool](./isempty.md)
  A Boolean value that indicates whether the path has any valid elements.
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
- [func append(UIBezierPath)](./append%28_%29.md)
  Appends the contents of the specified path object to the path.
- [var cgPath: CGPath](./cgpath.md)
  The Core Graphics representation of the path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibezierpath/currentpoint)*
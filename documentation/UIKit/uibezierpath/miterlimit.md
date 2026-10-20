# miterLimit

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The limiting value that helps avoid spikes at junctions between connected line segments.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var miterLimit: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat miterLimit;
```

#### Discussion

The miter limit helps you avoid spikes in paths that use the [`CGLineJoin.miter`](../../CoreGraphics/cglinejoin/miter.md) join style. If the ratio of the miter length—that is, the diagonal length of the miter join—to the line thickness exceeds the miter limit, the joint is converted to a bevel join. The default miter limit is 10, which results in the conversion of miters whose angle at the joint is less than 11 degrees.

## See Also

### Accessing drawing properties
- [var lineWidth: CGFloat](./linewidth.md)
  The line width of the path.
- [var lineCapStyle: CGLineCap](./linecapstyle.md)
  The shape of the endpoints of a stroked path.
- [var lineJoinStyle: CGLineJoin](./linejoinstyle.md)
  The shape of the joints between connected segments of a stroked path.
- [var flatness: CGFloat](./flatness.md)
  The factor that determines the rendering accuracy for curved path segments.
- [var usesEvenOddFillRule: Bool](./usesevenoddfillrule.md)
  A Boolean value that indicates whether the even-odd winding rule is in use for drawing paths.
- [func setLineDash(UnsafePointer<CGFloat>?, count: Int, phase: CGFloat)](./setlinedash%28_,count,phase%29.md)
  Sets the line-stroking pattern for the path.
- [func getLineDash(UnsafeMutablePointer<CGFloat>?, count: UnsafeMutablePointer<Int>?, phase: UnsafeMutablePointer<CGFloat>?)](./getlinedash%28_,count,phase%29.md)
  Retrieves the line-stroking pattern for the path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibezierpath/miterlimit)*
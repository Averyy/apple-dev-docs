# lineCapStyle

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The shape of the endpoints of a stroked path.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var lineCapStyle: CGLineCap { get set }
```

```objc
@property (nonatomic) CGLineCap lineCapStyle;
```

## Discussion

The line cap style is applied to the start and end points of any open subpaths. This property does not affect closed subpaths. The default line cap style is [`CGLineCap.butt`](../../CoreGraphics/cglinecap/butt.md).

## See Also

### Accessing drawing properties
- [var lineWidth: CGFloat](./linewidth.md)
  The line width of the path.
- [var lineJoinStyle: CGLineJoin](./linejoinstyle.md)
  The shape of the joints between connected segments of a stroked path.
- [var miterLimit: CGFloat](./miterlimit.md)
  The limiting value that helps avoid spikes at junctions between connected line segments.
- [var flatness: CGFloat](./flatness.md)
  The factor that determines the rendering accuracy for curved path segments.
- [var usesEvenOddFillRule: Bool](./usesevenoddfillrule.md)
  A Boolean value that indicates whether the even-odd winding rule is in use for drawing paths.
- [func setLineDash(UnsafePointer<CGFloat>?, count: Int, phase: CGFloat)](./setlinedash%28_,count,phase%29.md)
  Sets the line-stroking pattern for the path.
- [func getLineDash(UnsafeMutablePointer<CGFloat>?, count: UnsafeMutablePointer<Int>?, phase: UnsafeMutablePointer<CGFloat>?)](./getlinedash%28_,count,phase%29.md)
  Retrieves the line-stroking pattern for the path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibezierpath/linecapstyle)*
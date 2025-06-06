# flatness

**Framework**: UIKit  
**Kind**: property

The factor that determines the rendering accuracy for curved path segments.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var flatness: CGFloat { get set }
```

#### Discussion

The flatness value measures the largest permissible distance (measured in pixels) between a point on the true curve and a point on the rendered curve. Smaller values result in smoother curves but require more computation time. Larger values result in more jagged curves but are rendered much faster. The default flatness value is `0.6`.

In most cases, you should not change the flatness value. However, you might increase the flatness value temporarily to minimize the amount of time it takes to draw a shape temporarily (such as during scrolling).

## See Also

- [var lineWidth: CGFloat](uibezierpath/linewidth.md)
  The line width of the path.
- [var lineCapStyle: CGLineCap](uibezierpath/linecapstyle.md)
  The shape of the endpoints of a stroked path.
- [var lineJoinStyle: CGLineJoin](uibezierpath/linejoinstyle.md)
  The shape of the joints between connected segments of a stroked path.
- [var miterLimit: CGFloat](uibezierpath/miterlimit.md)
  The limiting value that helps avoid spikes at junctions between connected line segments.
- [var usesEvenOddFillRule: Bool](uibezierpath/usesevenoddfillrule.md)
  A Boolean value that indicates whether the even-odd winding rule is in use for drawing paths.
- [func setLineDash(UnsafePointer<CGFloat>?, count: Int, phase: CGFloat)](uibezierpath/setlinedash(_:count:phase:).md)
  Sets the line-stroking pattern for the path.
- [func getLineDash(UnsafeMutablePointer<CGFloat>?, count: UnsafeMutablePointer<Int>?, phase: UnsafeMutablePointer<CGFloat>?)](uibezierpath/getlinedash(_:count:phase:).md)
  Retrieves the line-stroking pattern for the path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibezierpath/flatness)*
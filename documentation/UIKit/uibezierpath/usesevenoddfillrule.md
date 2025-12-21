# usesEvenOddFillRule

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the even-odd winding rule is in use for drawing paths.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var usesEvenOddFillRule: Bool { get set }
```

#### Discussion

If [`true`](https://developer.apple.com/documentation/Swift/true), the path is filled using the even-odd rule. If [`false`](https://developer.apple.com/documentation/Swift/false), it is filled using the non-zero rule. Both rules are algorithms to determine which areas of a path to fill with the current fill color. A ray is drawn from a point inside a given region to a point anywhere outside the path’s bounds. The total number of crossed path lines (including implicit path lines) and the direction of each path line are then interpreted as follows:

- For the even-odd rule, if the total number of path crossings is odd, the point is considered to be inside the path and the corresponding region is filled. If the number of crossings is even, the point is considered to be outside the path and the region is not filled.
- For the non-zero rule, the crossing of a left-to-right path counts as +1 and the crossing of a right-to-left path counts as -1. If the sum of the crossings is nonzero, the point is considered to be inside the path and the corresponding region is filled. If the sum is 0, the point is outside the path and the region is not filled.

The default value of this property is [`false`](https://developer.apple.com/documentation/Swift/false). For more information about winding rules and how they are applied to subpaths, see [`Quartz 2D Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066).

## See Also

- [var lineWidth: CGFloat](uibezierpath/linewidth.md)
  The line width of the path.
- [var lineCapStyle: CGLineCap](uibezierpath/linecapstyle.md)
  The shape of the endpoints of a stroked path.
- [var lineJoinStyle: CGLineJoin](uibezierpath/linejoinstyle.md)
  The shape of the joints between connected segments of a stroked path.
- [var miterLimit: CGFloat](uibezierpath/miterlimit.md)
  The limiting value that helps avoid spikes at junctions between connected line segments.
- [var flatness: CGFloat](uibezierpath/flatness.md)
  The factor that determines the rendering accuracy for curved path segments.
- [func setLineDash(UnsafePointer<CGFloat>?, count: Int, phase: CGFloat)](uibezierpath/setlinedash(_:count:phase:).md)
  Sets the line-stroking pattern for the path.
- [func getLineDash(UnsafeMutablePointer<CGFloat>?, count: UnsafeMutablePointer<Int>?, phase: UnsafeMutablePointer<CGFloat>?)](uibezierpath/getlinedash(_:count:phase:).md)
  Retrieves the line-stroking pattern for the path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibezierpath/usesevenoddfillrule)*
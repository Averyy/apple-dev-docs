# Shape Fill Mode Values

**Framework**: Core Animation

These constants specify the possible fill modes for [`fillRule`](cashapelayer/fillrule.md).

## Topics

### Constants
- [static let nonZero: CAShapeLayerFillRule](cashapelayerfillrule/nonzero.md)
  Specifies the non-zero winding rule. Count each left-to-right path as +1 and each right-to-left path as -1. If the sum of all crossings is 0, the point is outside the path. If the sum is nonzero, the point is inside the path and the region containing it is filled.
- [static let evenOdd: CAShapeLayerFillRule](cashapelayerfillrule/evenodd.md)
  Specifies the even-odd winding rule. Count the total number of path crossings. If the number of crossings is even, the point is outside the path. If the number of crossings is odd, the point is inside the path and the region containing it should be filled.

## See Also

- [Line Join Values](line-join-values.md)
  These constants specify the shape of the joints between connected segments of a stroked path.
- [Line Cap Values](line-cap-values.md)
  These constants specify the shape of endpoints for an open path when stroked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/shape-fill-mode-values)*
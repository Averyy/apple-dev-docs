# getLineDash(_:count:phase:)

**Framework**: UIKit  
**Kind**: method

Retrieves the line-stroking pattern for the path.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func getLineDash(_ pattern: UnsafeMutablePointer<CGFloat>?, count: UnsafeMutablePointer<Int>?, phase: UnsafeMutablePointer<CGFloat>?)
```

#### Discussion

The array in the `pattern` parameter must be large enough to hold all of the returned values in the pattern. If you are not sure how many values there might be, you can call this method twice. The first time you call it, do not pass a value for `pattern` but use the returned value in the `count` parameter to allocate an array of floating-point numbers that you can then pass in the second time.

## Parameters

- `pattern`: On input, a C-style array of floating point values, or   if you do not want the pattern values. On output, this array contains the lengths (measured in points) of the line segments and gaps in the pattern. The values in the array alternate, starting with the first line segment length, followed by the first gap length, followed by the second line segment length, and so on.
- `count`: On input, a pointer to an integer or   if you do not want the number of pattern entries. On output, the number of entries written to  .
- `phase`: On input, a pointer to a floating point value or   if you do not want the phase. On output, this value contains the offset at which to start drawing the pattern, measured in points along the dashed-line pattern. For example, a phase of 6 in the pattern 5-2-3-2 would cause drawing to begin in the middle of the first gap.

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
- [var usesEvenOddFillRule: Bool](uibezierpath/usesevenoddfillrule.md)
  A Boolean value that indicates whether the even-odd winding rule is in use for drawing paths.
- [func setLineDash(UnsafePointer<CGFloat>?, count: Int, phase: CGFloat)](uibezierpath/setlinedash(_:count:phase:).md)
  Sets the line-stroking pattern for the path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibezierpath/getlinedash(_:count:phase:))*
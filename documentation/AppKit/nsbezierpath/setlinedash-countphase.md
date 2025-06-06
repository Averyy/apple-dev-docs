# setLineDash(_:count:phase:)

**Framework**: AppKit  
**Kind**: method

Sets the line-stroking pattern for the path.

**Availability**:
- macOS ?+

## Declaration

```swift
func setLineDash(_ pattern: UnsafePointer<CGFloat>?, count: Int, phase: CGFloat)
```

#### Discussion

For example, to produce a supermarket coupon type of dashed line:

```objc
array[0] = 5.0; //segment painted with stroke color
array[1] = 2.0; //segment not painted with a color
 
[path setLineDash: array count: 2 phase: 0.0];
```

In the above example, if you set `phase` to 6.0, the line dash would begin exactly six units into `pattern`, which would start the pattern in the middle of the first gap.

## Parameters

- `pattern`: A C-style array of floating point values that contains the lengths (measured in points) of the line segments and gaps in the pattern. The values in the array alternate, starting with the first line segment length, followed by the first gap length, followed by the second line segment length, and so on
- `count`: The number of values in  .
- `phase`: The offset at which to start drawing the pattern, measured in points along the dashed-line pattern. For example, a phase of 6 in the pattern 5-2-3-2 would cause drawing to begin in the middle of the first gap

## See Also

- [var windingRule: NSBezierPath.WindingRule](nsbezierpath/windingrule-swift.property.md)
  The winding rule used to fill the path.
- [var lineCapStyle: NSBezierPath.LineCapStyle](nsbezierpath/linecapstyle-swift.property.md)
  The line cap style for the path.
- [var lineJoinStyle: NSBezierPath.LineJoinStyle](nsbezierpath/linejoinstyle-swift.property.md)
  The line join style for the path.
- [var lineWidth: CGFloat](nsbezierpath/linewidth.md)
  The width of stroked path lines.
- [var miterLimit: CGFloat](nsbezierpath/miterlimit.md)
  The limit at which miter joins are converted to bevel joins.
- [var flatness: CGFloat](nsbezierpath/flatness.md)
  The accuracy with which curves are rendered.
- [func getLineDash(UnsafeMutablePointer<CGFloat>?, count: UnsafeMutablePointer<Int>?, phase: UnsafeMutablePointer<CGFloat>?)](nsbezierpath/getlinedash(_:count:phase:).md)
  Returns the line-stroking pattern for the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/setlinedash(_:count:phase:))*
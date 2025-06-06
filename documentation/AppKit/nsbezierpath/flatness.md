# flatness

**Framework**: AppKit  
**Kind**: property

The accuracy with which curves are rendered.

**Availability**:
- macOS ?+

## Declaration

```swift
var flatness: CGFloat { get set }
```

#### Discussion

The flatness value specifies the accuracy (or smoothness) with which curves are rendered. It is also the maximum error tolerance (measured in pixels) for rendering curves, where smaller numbers give smoother curves at the expense of more computation. The exact interpretation may vary slightly on different rendering devices.

The default value of this property is the value returned by the [`defaultFlatness`](nsbezierpath/defaultflatness.md) method.

## See Also

- [class var defaultFlatness: CGFloat](nsbezierpath/defaultflatness.md)
  The default flatness value for all paths.
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
- [func getLineDash(UnsafeMutablePointer<CGFloat>?, count: UnsafeMutablePointer<Int>?, phase: UnsafeMutablePointer<CGFloat>?)](nsbezierpath/getlinedash(_:count:phase:).md)
  Returns the line-stroking pattern for the receiver.
- [func setLineDash(UnsafePointer<CGFloat>?, count: Int, phase: CGFloat)](nsbezierpath/setlinedash(_:count:phase:).md)
  Sets the line-stroking pattern for the path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/flatness)*
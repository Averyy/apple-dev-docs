# miterLimit

**Framework**: AppKit  
**Kind**: property

The limit at which miter joins are converted to bevel joins.

**Availability**:
- macOS ?+

## Declaration

```swift
var miterLimit: CGFloat { get set }
```

#### Discussion

The miter limit helps you avoid spikes at the junction of two line segments connected by a miter join ([`NSMiterLineJoinStyle`](nsmiterlinejoinstyle.md)). If the ratio of the miter length—the diagonal length of the miter join—to the line thickness exceeds the miter limit, the joint is converted to a bevel join.

The default value of this property is the value returned by the [`defaultMiterLimit`](nsbezierpath/defaultmiterlimit.md) method.

## See Also

- [class var defaultMiterLimit: CGFloat](nsbezierpath/defaultmiterlimit.md)
  Returns the default miter limit for all paths.
- [var windingRule: NSBezierPath.WindingRule](nsbezierpath/windingrule-swift.property.md)
  The winding rule used to fill the path.
- [var lineCapStyle: NSBezierPath.LineCapStyle](nsbezierpath/linecapstyle-swift.property.md)
  The line cap style for the path.
- [var lineJoinStyle: NSBezierPath.LineJoinStyle](nsbezierpath/linejoinstyle-swift.property.md)
  The line join style for the path.
- [var lineWidth: CGFloat](nsbezierpath/linewidth.md)
  The width of stroked path lines.
- [var flatness: CGFloat](nsbezierpath/flatness.md)
  The accuracy with which curves are rendered.
- [func getLineDash(UnsafeMutablePointer<CGFloat>?, count: UnsafeMutablePointer<Int>?, phase: UnsafeMutablePointer<CGFloat>?)](nsbezierpath/getlinedash(_:count:phase:).md)
  Returns the line-stroking pattern for the receiver.
- [func setLineDash(UnsafePointer<CGFloat>?, count: Int, phase: CGFloat)](nsbezierpath/setlinedash(_:count:phase:).md)
  Sets the line-stroking pattern for the path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/miterlimit)*
# windingRule

**Framework**: AppKit  
**Kind**: property

The winding rule used to fill the path.

**Availability**:
- macOS ?+

## Declaration

```swift
var windingRule: NSBezierPath.WindingRule { get set }
```

#### Discussion

This value may be either [`NSNonZeroWindingRule`](nsnonzerowindingrule.md) or [`NSEvenOddWindingRule`](nsevenoddwindingrule.md). This value overrides the default value returned by the [`defaultWindingRule`](nsbezierpath/defaultwindingrule.md) method.

For more information on how winding rules affect the appearance of filled paths, see [`Cocoa Drawing Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaDrawingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40003290).

## See Also

- [func fill()](nsbezierpath/fill.md)
  Paints the region enclosed by the path.
- [class var defaultWindingRule: NSBezierPath.WindingRule](nsbezierpath/defaultwindingrule.md)
  Returns the default winding rule used to fill all paths.
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
- [func setLineDash(UnsafePointer<CGFloat>?, count: Int, phase: CGFloat)](nsbezierpath/setlinedash(_:count:phase:).md)
  Sets the line-stroking pattern for the path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/windingrule-swift.property)*
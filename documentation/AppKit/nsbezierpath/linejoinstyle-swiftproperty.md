# lineJoinStyle

**Framework**: AppKit  
**Kind**: property

The line join style for the path.

**Availability**:
- macOS ?+

## Declaration

```swift
var lineJoinStyle: NSBezierPath.LineJoinStyle { get set }
```

#### Discussion

The line join style specifies the shape of the joints between connected segments of a stroked path. The default value of this property is the value returned by the [`defaultLineJoinStyle`](nsbezierpath/defaultlinejoinstyle.md) method.

## See Also

- [class var defaultLineJoinStyle: NSBezierPath.LineJoinStyle](nsbezierpath/defaultlinejoinstyle.md)
  Returns the default line join style for all paths.
- [NSBezierPath.LineJoinStyle](nsbezierpath/linejoinstyle-swift.enum.md)
  Constants that specify the shape of the joins between connected segments of a stroked path.
- [var windingRule: NSBezierPath.WindingRule](nsbezierpath/windingrule-swift.property.md)
  The winding rule used to fill the path.
- [var lineCapStyle: NSBezierPath.LineCapStyle](nsbezierpath/linecapstyle-swift.property.md)
  The line cap style for the path.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/linejoinstyle-swift.property)*
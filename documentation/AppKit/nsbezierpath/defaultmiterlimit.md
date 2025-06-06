# defaultMiterLimit

**Framework**: AppKit  
**Kind**: property

Returns the default miter limit for all paths.

**Availability**:
- macOS ?+

## Declaration

```swift
class var defaultMiterLimit: CGFloat { get set }
```

#### Return Value

The default miter limit for all paths, or 10.0 if no other value has been set.

## See Also

- [var miterLimit: CGFloat](nsbezierpath/miterlimit.md)
  The limit at which miter joins are converted to bevel joins.
- [class var defaultWindingRule: NSBezierPath.WindingRule](nsbezierpath/defaultwindingrule.md)
  Returns the default winding rule used to fill all paths.
- [class var defaultLineCapStyle: NSBezierPath.LineCapStyle](nsbezierpath/defaultlinecapstyle.md)
  Returns the default line cap style for all paths.
- [class var defaultLineJoinStyle: NSBezierPath.LineJoinStyle](nsbezierpath/defaultlinejoinstyle.md)
  Returns the default line join style for all paths.
- [class var defaultLineWidth: CGFloat](nsbezierpath/defaultlinewidth.md)
  Returns the default line width for the all paths.
- [class var defaultFlatness: CGFloat](nsbezierpath/defaultflatness.md)
  The default flatness value for all paths.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/defaultmiterlimit)*
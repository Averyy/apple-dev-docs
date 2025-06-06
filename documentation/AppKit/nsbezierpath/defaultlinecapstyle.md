# defaultLineCapStyle

**Framework**: AppKit  
**Kind**: property

Returns the default line cap style for all paths.

**Availability**:
- macOS ?+

## Declaration

```swift
class var defaultLineCapStyle: NSBezierPath.LineCapStyle { get set }
```

#### Return Value

The default line cap style or `NSButtLineCapStyle` if no other style has been set. For a list of values, see Constants.

#### Discussion

The default line cap style can be overridden for individual paths by setting a custom style for that path using the [`NSBezierPath`](nsbezierpath.md) method.

## See Also

- [var lineCapStyle: NSBezierPath.LineCapStyle](nsbezierpath/linecapstyle-swift.property.md)
  The line cap style for the path.
- [class var defaultWindingRule: NSBezierPath.WindingRule](nsbezierpath/defaultwindingrule.md)
  Returns the default winding rule used to fill all paths.
- [class var defaultLineJoinStyle: NSBezierPath.LineJoinStyle](nsbezierpath/defaultlinejoinstyle.md)
  Returns the default line join style for all paths.
- [class var defaultLineWidth: CGFloat](nsbezierpath/defaultlinewidth.md)
  Returns the default line width for the all paths.
- [class var defaultMiterLimit: CGFloat](nsbezierpath/defaultmiterlimit.md)
  Returns the default miter limit for all paths.
- [class var defaultFlatness: CGFloat](nsbezierpath/defaultflatness.md)
  The default flatness value for all paths.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/defaultlinecapstyle)*
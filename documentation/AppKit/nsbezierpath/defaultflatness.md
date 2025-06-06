# defaultFlatness

**Framework**: AppKit  
**Kind**: property

The default flatness value for all paths.

**Availability**:
- macOS ?+

## Declaration

```swift
class var defaultFlatness: CGFloat { get set }
```

#### Return Value

The default value for determining the smoothness of curved paths, or 0.6 if no other value has been set.

## See Also

- [var flatness: CGFloat](nsbezierpath/flatness.md)
  The accuracy with which curves are rendered.
- [class var defaultWindingRule: NSBezierPath.WindingRule](nsbezierpath/defaultwindingrule.md)
  Returns the default winding rule used to fill all paths.
- [class var defaultLineCapStyle: NSBezierPath.LineCapStyle](nsbezierpath/defaultlinecapstyle.md)
  Returns the default line cap style for all paths.
- [class var defaultLineJoinStyle: NSBezierPath.LineJoinStyle](nsbezierpath/defaultlinejoinstyle.md)
  Returns the default line join style for all paths.
- [class var defaultLineWidth: CGFloat](nsbezierpath/defaultlinewidth.md)
  Returns the default line width for the all paths.
- [class var defaultMiterLimit: CGFloat](nsbezierpath/defaultmiterlimit.md)
  Returns the default miter limit for all paths.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/defaultflatness)*
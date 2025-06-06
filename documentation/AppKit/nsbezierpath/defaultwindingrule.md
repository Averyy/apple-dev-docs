# defaultWindingRule

**Framework**: AppKit  
**Kind**: property

Returns the default winding rule used to fill all paths.

**Availability**:
- macOS ?+

## Declaration

```swift
class var defaultWindingRule: NSBezierPath.WindingRule { get set }
```

#### Return Value

The current default winding rule or [`NSNonZeroWindingRule`](nsnonzerowindingrule.md) if no default rule has been set. This value may be either [`NSNonZeroWindingRule`](nsnonzerowindingrule.md) or [`NSEvenOddWindingRule`](nsevenoddwindingrule.md).

## See Also

- [var windingRule: NSBezierPath.WindingRule](nsbezierpath/windingrule-swift.property.md)
  The winding rule used to fill the path.
- [class var defaultLineCapStyle: NSBezierPath.LineCapStyle](nsbezierpath/defaultlinecapstyle.md)
  Returns the default line cap style for all paths.
- [class var defaultLineJoinStyle: NSBezierPath.LineJoinStyle](nsbezierpath/defaultlinejoinstyle.md)
  Returns the default line join style for all paths.
- [class var defaultLineWidth: CGFloat](nsbezierpath/defaultlinewidth.md)
  Returns the default line width for the all paths.
- [class var defaultMiterLimit: CGFloat](nsbezierpath/defaultmiterlimit.md)
  Returns the default miter limit for all paths.
- [class var defaultFlatness: CGFloat](nsbezierpath/defaultflatness.md)
  The default flatness value for all paths.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/defaultwindingrule)*
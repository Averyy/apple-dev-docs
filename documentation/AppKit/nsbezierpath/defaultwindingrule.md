# defaultWindingRule

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Returns the default winding rule used to fill all paths.

**Availability**:
- macOS

## Declaration

```swift
class var defaultWindingRule: NSBezierPath.WindingRule { get set }
```

```objc
@property (class) NSWindingRule defaultWindingRule;
```

## Return Value

The current default winding rule or [`NSNonZeroWindingRule`](../nsnonzerowindingrule.md) if no default rule has been set. This value may be either [`NSNonZeroWindingRule`](../nsnonzerowindingrule.md) or [`NSEvenOddWindingRule`](../nsevenoddwindingrule.md).

## See Also

### Related Documentation
- [var windingRule: NSBezierPath.WindingRule](./windingrule-swift.property.md)
  The winding rule used to fill the path.
### Configuring Default Path Attributes
- [class var defaultLineCapStyle: NSBezierPath.LineCapStyle](./defaultlinecapstyle.md)
  Returns the default line cap style for all paths.
- [class var defaultLineJoinStyle: NSBezierPath.LineJoinStyle](./defaultlinejoinstyle.md)
  Returns the default line join style for all paths.
- [class var defaultLineWidth: CGFloat](./defaultlinewidth.md)
  Returns the default line width for the all paths.
- [class var defaultMiterLimit: CGFloat](./defaultmiterlimit.md)
  Returns the default miter limit for all paths.
- [class var defaultFlatness: CGFloat](./defaultflatness.md)
  The default flatness value for all paths.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/defaultwindingrule)*
# defaultMiterLimit

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Returns the default miter limit for all paths.

**Availability**:
- macOS

## Declaration

```swift
class var defaultMiterLimit: CGFloat { get set }
```

```objc
@property (class) CGFloat defaultMiterLimit;
```

#### Return Value

The default miter limit for all paths, or 10.0 if no other value has been set.

## See Also

### Related Documentation
- [var miterLimit: CGFloat](./miterlimit.md)
  The limit at which miter joins are converted to bevel joins.
### Configuring Default Path Attributes
- [class var defaultWindingRule: NSBezierPath.WindingRule](./defaultwindingrule.md)
  Returns the default winding rule used to fill all paths.
- [class var defaultLineCapStyle: NSBezierPath.LineCapStyle](./defaultlinecapstyle.md)
  Returns the default line cap style for all paths.
- [class var defaultLineJoinStyle: NSBezierPath.LineJoinStyle](./defaultlinejoinstyle.md)
  Returns the default line join style for all paths.
- [class var defaultLineWidth: CGFloat](./defaultlinewidth.md)
  Returns the default line width for the all paths.
- [class var defaultFlatness: CGFloat](./defaultflatness.md)
  The default flatness value for all paths.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/defaultmiterlimit)*
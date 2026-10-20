# defaultLineWidth

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Returns the default line width for the all paths.

**Availability**:
- macOS

## Declaration

```swift
class var defaultLineWidth: CGFloat { get set }
```

```objc
@property (class) CGFloat defaultLineWidth;
```

#### Return Value

The default line width, measured in points in the user coordinate space, or 1.0 if no other value has been set.

## See Also

### Related Documentation
- [var lineWidth: CGFloat](./linewidth.md)
  The width of stroked path lines.
### Configuring Default Path Attributes
- [class var defaultWindingRule: NSBezierPath.WindingRule](./defaultwindingrule.md)
  Returns the default winding rule used to fill all paths.
- [class var defaultLineCapStyle: NSBezierPath.LineCapStyle](./defaultlinecapstyle.md)
  Returns the default line cap style for all paths.
- [class var defaultLineJoinStyle: NSBezierPath.LineJoinStyle](./defaultlinejoinstyle.md)
  Returns the default line join style for all paths.
- [class var defaultMiterLimit: CGFloat](./defaultmiterlimit.md)
  Returns the default miter limit for all paths.
- [class var defaultFlatness: CGFloat](./defaultflatness.md)
  The default flatness value for all paths.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/defaultlinewidth)*
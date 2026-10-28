# defaultLineJoinStyle

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Returns the default line join style for all paths.

**Availability**:
- macOS

## Declaration

```swift
class var defaultLineJoinStyle: NSBezierPath.LineJoinStyle { get set }
```

```objc
@property (class) NSLineJoinStyle defaultLineJoinStyle;
```

## Return Value

The default line join style or `NSMiterLineJoinStyle` if no other value has been set. For a list of values, see Constants.

## See Also

### Related Documentation
- [var lineJoinStyle: NSBezierPath.LineJoinStyle](./linejoinstyle-swift.property.md)
  The line join style for the path.
### Configuring Default Path Attributes
- [class var defaultWindingRule: NSBezierPath.WindingRule](./defaultwindingrule.md)
  Returns the default winding rule used to fill all paths.
- [class var defaultLineCapStyle: NSBezierPath.LineCapStyle](./defaultlinecapstyle.md)
  Returns the default line cap style for all paths.
- [class var defaultLineWidth: CGFloat](./defaultlinewidth.md)
  Returns the default line width for the all paths.
- [class var defaultMiterLimit: CGFloat](./defaultmiterlimit.md)
  Returns the default miter limit for all paths.
- [class var defaultFlatness: CGFloat](./defaultflatness.md)
  The default flatness value for all paths.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/defaultlinejoinstyle)*
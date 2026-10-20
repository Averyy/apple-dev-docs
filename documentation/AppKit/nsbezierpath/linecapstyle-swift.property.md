# lineCapStyle

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The line cap style for the path.

**Availability**:
- macOS

## Declaration

```swift
var lineCapStyle: NSBezierPath.LineCapStyle { get set }
```

```objc
@property NSLineCapStyle lineCapStyle;
```

#### Discussion

The line cap style specifies the shape of the endpoints on an open path when stroked. The default value of this property is the value returned by the [`defaultLineCapStyle`](./defaultlinecapstyle.md) method.

## See Also

### Related Documentation
- [class var defaultLineCapStyle: NSBezierPath.LineCapStyle](./defaultlinecapstyle.md)
  Returns the default line cap style for all paths.
- [NSBezierPath.LineCapStyle](./linecapstyle-swift.enum.md)
  Constants that specify the shape of endpoints for an open path when it is stroked.
### Accessing a Path’s Attributes
- [var windingRule: NSBezierPath.WindingRule](./windingrule-swift.property.md)
  The winding rule used to fill the path.
- [var lineJoinStyle: NSBezierPath.LineJoinStyle](./linejoinstyle-swift.property.md)
  The line join style for the path.
- [var lineWidth: CGFloat](./linewidth.md)
  The width of stroked path lines.
- [var miterLimit: CGFloat](./miterlimit.md)
  The limit at which miter joins are converted to bevel joins.
- [var flatness: CGFloat](./flatness.md)
  The accuracy with which curves are rendered.
- [func getLineDash(UnsafeMutablePointer<CGFloat>?, count: UnsafeMutablePointer<Int>?, phase: UnsafeMutablePointer<CGFloat>?)](./getlinedash%28_,count,phase%29.md)
  Returns the line-stroking pattern for the receiver.
- [func setLineDash(UnsafePointer<CGFloat>?, count: Int, phase: CGFloat)](./setlinedash%28_,count,phase%29.md)
  Sets the line-stroking pattern for the path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/linecapstyle-swift.property)*
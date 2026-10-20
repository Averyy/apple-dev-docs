# lineJoinStyle

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The line join style for the path.

**Availability**:
- macOS

## Declaration

```swift
var lineJoinStyle: NSBezierPath.LineJoinStyle { get set }
```

```objc
@property NSLineJoinStyle lineJoinStyle;
```

#### Discussion

The line join style specifies the shape of the joints between connected segments of a stroked path. The default value of this property is the value returned by the [`defaultLineJoinStyle`](./defaultlinejoinstyle.md) method.

## See Also

### Related Documentation
- [class var defaultLineJoinStyle: NSBezierPath.LineJoinStyle](./defaultlinejoinstyle.md)
  Returns the default line join style for all paths.
- [NSBezierPath.LineJoinStyle](./linejoinstyle-swift.enum.md)
  Constants that specify the shape of the joins between connected segments of a stroked path.
### Accessing a Path’s Attributes
- [var windingRule: NSBezierPath.WindingRule](./windingrule-swift.property.md)
  The winding rule used to fill the path.
- [var lineCapStyle: NSBezierPath.LineCapStyle](./linecapstyle-swift.property.md)
  The line cap style for the path.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/linejoinstyle-swift.property)*
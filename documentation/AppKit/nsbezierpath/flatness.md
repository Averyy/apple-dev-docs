# flatness

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The accuracy with which curves are rendered.

**Availability**:
- macOS

## Declaration

```swift
var flatness: CGFloat { get set }
```

```objc
@property CGFloat flatness;
```

## Discussion

The flatness value specifies the accuracy (or smoothness) with which curves are rendered. It is also the maximum error tolerance (measured in pixels) for rendering curves, where smaller numbers give smoother curves at the expense of more computation. The exact interpretation may vary slightly on different rendering devices.

The default value of this property is the value returned by the [`defaultFlatness`](./defaultflatness.md) method.

## See Also

### Related Documentation
- [class var defaultFlatness: CGFloat](./defaultflatness.md)
  The default flatness value for all paths.
### Accessing a Path’s Attributes
- [var windingRule: NSBezierPath.WindingRule](./windingrule-swift.property.md)
  The winding rule used to fill the path.
- [var lineCapStyle: NSBezierPath.LineCapStyle](./linecapstyle-swift.property.md)
  The line cap style for the path.
- [var lineJoinStyle: NSBezierPath.LineJoinStyle](./linejoinstyle-swift.property.md)
  The line join style for the path.
- [var lineWidth: CGFloat](./linewidth.md)
  The width of stroked path lines.
- [var miterLimit: CGFloat](./miterlimit.md)
  The limit at which miter joins are converted to bevel joins.
- [func getLineDash(UnsafeMutablePointer<CGFloat>?, count: UnsafeMutablePointer<Int>?, phase: UnsafeMutablePointer<CGFloat>?)](./getlinedash%28_,count,phase%29.md)
  Returns the line-stroking pattern for the receiver.
- [func setLineDash(UnsafePointer<CGFloat>?, count: Int, phase: CGFloat)](./setlinedash%28_,count,phase%29.md)
  Sets the line-stroking pattern for the path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/flatness)*
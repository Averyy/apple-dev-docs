# lineWidth

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The width of stroked path lines.

**Availability**:
- macOS

## Declaration

```swift
var lineWidth: CGFloat { get set }
```

```objc
@property CGFloat lineWidth;
```

#### Discussion

The line width defines the thickness of the receiver’s stroked path. A width of 0 is interpreted as the thinnest line that can be rendered on a particular device. The actual rendered line width may vary from the specified width by as much as 2 device pixels, depending on the position of the line with respect to the pixel grid and the current anti-aliasing settings. The width of the line may also be affected by scaling factors specified in the current transformation matrix of the active graphics context.

The default value of this property is the value returned by the [`defaultLineWidth`](./defaultlinewidth.md) method.

## See Also

### Related Documentation
- [class var defaultLineWidth: CGFloat](./defaultlinewidth.md)
  Returns the default line width for the all paths.
### Accessing a Path’s Attributes
- [var windingRule: NSBezierPath.WindingRule](./windingrule-swift.property.md)
  The winding rule used to fill the path.
- [var lineCapStyle: NSBezierPath.LineCapStyle](./linecapstyle-swift.property.md)
  The line cap style for the path.
- [var lineJoinStyle: NSBezierPath.LineJoinStyle](./linejoinstyle-swift.property.md)
  The line join style for the path.
- [var miterLimit: CGFloat](./miterlimit.md)
  The limit at which miter joins are converted to bevel joins.
- [var flatness: CGFloat](./flatness.md)
  The accuracy with which curves are rendered.
- [func getLineDash(UnsafeMutablePointer<CGFloat>?, count: UnsafeMutablePointer<Int>?, phase: UnsafeMutablePointer<CGFloat>?)](./getlinedash%28_,count,phase%29.md)
  Returns the line-stroking pattern for the receiver.
- [func setLineDash(UnsafePointer<CGFloat>?, count: Int, phase: CGFloat)](./setlinedash%28_,count,phase%29.md)
  Sets the line-stroking pattern for the path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/linewidth)*
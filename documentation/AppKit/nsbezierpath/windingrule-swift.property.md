# windingRule

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The winding rule used to fill the path.

**Availability**:
- macOS

## Declaration

```swift
var windingRule: NSBezierPath.WindingRule { get set }
```

```objc
@property NSWindingRule windingRule;
```

## Discussion

This value may be either [`NSNonZeroWindingRule`](../nsnonzerowindingrule.md) or [`NSEvenOddWindingRule`](../nsevenoddwindingrule.md). This value overrides the default value returned by the [`defaultWindingRule`](./defaultwindingrule.md) method.

## See Also

### Related Documentation
- [func fill()](./fill%28%29.md)
  Paints the region enclosed by the path.
- [class var defaultWindingRule: NSBezierPath.WindingRule](./defaultwindingrule.md)
  Returns the default winding rule used to fill all paths.
### Accessing a Path’s Attributes
- [var lineCapStyle: NSBezierPath.LineCapStyle](./linecapstyle-swift.property.md)
  The line cap style for the path.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/windingrule-swift.property)*
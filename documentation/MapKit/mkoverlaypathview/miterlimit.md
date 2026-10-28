# miterLimit

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The limiting value that helps avoid spikes at junctions between connected line segments.

**Availability**:
- iOS 4.0+ - Deprecated in 7.0
- iPadOS 4.0+ - Deprecated in 7.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use an [`MKOverlayPathRenderer`](../mkoverlaypathrenderer.md) object instead.

## Declaration

```objc
@property CGFloat miterLimit;
```

## Discussion

The miter limit helps you avoid spikes in paths that use the [`CGLineJoin.miter`](../../CoreGraphics/cglinejoin/miter.md) join style. If the ratio of the miter length—that is, the diagonal length of the miter join—to the line thickness exceeds the miter limit, the joint is converted to a bevel join. The default miter limit is 10, which results in the conversion of miters whose angle at the joint is less than 11 degrees.

## See Also

### Accessing the drawing attributes
- [fillColor](./fillcolor.md)
  The fill color to use for the path.
- [strokeColor](./strokecolor.md)
  The stroke color to use for the path.
- [lineWidth](./linewidth.md)
  The stroke width to use for the path.
- [lineJoin](./linejoin.md)
  The line join style to apply to corners of the path.
- [lineCap](./linecap.md)
  The line cap style to apply to the open ends of the path.
- [lineDashPhase](./linedashphase.md)
  The offset (in points) at which to start drawing the dash pattern.
- [lineDashPattern](./linedashpattern.md)
  An array of numbers indicating the dash pattern for paths.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkoverlaypathview/miterlimit)*
# miterLimit

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The limiting value that helps avoid spikes at junctions between connected line segments.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
var miterLimit: CGFloat { get set }
```

```objc
@property CGFloat miterLimit;
```

## Discussion

The miter limit helps you avoid spikes in paths that use the [`CGLineJoin.miter`](../../CoreGraphics/cglinejoin/miter.md) join style. If the ratio of the miter length to the line thickness — the diagonal length of the miter join — exceeds the miter limit, the renderer converts the joint to a bevel join. The default miter limit is `10`, which results in the conversion of miters with an angle at the joint of less than `11` degrees.

## See Also

### Accessing the drawing attributes
- [var fillColor: UIColor?](./fillcolor.md)
  The fill color to use for the path.
- [var strokeColor: UIColor?](./strokecolor.md)
  The stroke color to use for the path.
- [var lineWidth: CGFloat](./linewidth.md)
  The stroke width to use for the path.
- [var lineJoin: CGLineJoin](./linejoin.md)
  The line join style to apply to the corners of the path.
- [var lineCap: CGLineCap](./linecap.md)
  The line cap style to apply to the open ends of the path.
- [var lineDashPhase: CGFloat](./linedashphase.md)
  The offset (in points) at which to start drawing the dash pattern.
- [var lineDashPattern: [NSNumber]?](./linedashpattern.md)
  An array of numbers specifying the dash pattern to use for the path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer/miterlimit)*
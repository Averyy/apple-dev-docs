# miterLimit

**Framework**: MapKit  
**Kind**: property

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

#### Discussion

The miter limit helps you avoid spikes in paths that use the [`CGLineJoin.miter`](https://developer.apple.com/documentation/CoreGraphics/CGLineJoin/miter) join style. If the ratio of the miter length to the line thickness — the diagonal length of the miter join — exceeds the miter limit, the renderer converts the joint to a bevel join. The default miter limit is `10`, which results in the conversion of miters with an angle at the joint of less than `11` degrees.

## See Also

- [var fillColor: UIColor?](mkoverlaypathrenderer/fillcolor.md)
  The fill color to use for the path.
- [var strokeColor: UIColor?](mkoverlaypathrenderer/strokecolor.md)
  The stroke color to use for the path.
- [var lineWidth: CGFloat](mkoverlaypathrenderer/linewidth.md)
  The stroke width to use for the path.
- [var lineJoin: CGLineJoin](mkoverlaypathrenderer/linejoin.md)
  The line join style to apply to the corners of the path.
- [var lineCap: CGLineCap](mkoverlaypathrenderer/linecap.md)
  The line cap style to apply to the open ends of the path.
- [var lineDashPhase: CGFloat](mkoverlaypathrenderer/linedashphase.md)
  The offset (in points) at which to start drawing the dash pattern.
- [var lineDashPattern: [NSNumber]?](mkoverlaypathrenderer/linedashpattern.md)
  An array of numbers specifying the dash pattern to use for the path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer/miterlimit)*
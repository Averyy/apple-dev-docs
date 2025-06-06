# lineCap

**Framework**: MapKit  
**Kind**: property

The line cap style to apply to the open ends of the path.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
var lineCap: CGLineCap { get set }
```

#### Discussion

The line cap style applies to the start and end points of any open subpaths. This property doesn’t affect closed subpaths. The default line cap style is [`CGLineCap.round`](https://developer.apple.com/documentation/CoreGraphics/CGLineCap/round).

## See Also

- [var fillColor: UIColor?](mkoverlaypathrenderer/fillcolor.md)
  The fill color to use for the path.
- [var strokeColor: UIColor?](mkoverlaypathrenderer/strokecolor.md)
  The stroke color to use for the path.
- [var lineWidth: CGFloat](mkoverlaypathrenderer/linewidth.md)
  The stroke width to use for the path.
- [var lineJoin: CGLineJoin](mkoverlaypathrenderer/linejoin.md)
  The line join style to apply to the corners of the path.
- [var miterLimit: CGFloat](mkoverlaypathrenderer/miterlimit.md)
  The limiting value that helps avoid spikes at junctions between connected line segments.
- [var lineDashPhase: CGFloat](mkoverlaypathrenderer/linedashphase.md)
  The offset (in points) at which to start drawing the dash pattern.
- [var lineDashPattern: [NSNumber]?](mkoverlaypathrenderer/linedashpattern.md)
  An array of numbers specifying the dash pattern to use for the path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer/linecap)*
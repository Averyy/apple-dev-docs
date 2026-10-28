# lineCap

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property CGLineCap lineCap;
```

## Discussion

The line cap style applies to the start and end points of any open subpaths. This property doesn’t affect closed subpaths. The default line cap style is [`CGLineCap.round`](../../CoreGraphics/cglinecap/round.md).

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
- [var miterLimit: CGFloat](./miterlimit.md)
  The limiting value that helps avoid spikes at junctions between connected line segments.
- [var lineDashPhase: CGFloat](./linedashphase.md)
  The offset (in points) at which to start drawing the dash pattern.
- [var lineDashPattern: [NSNumber]?](./linedashpattern.md)
  An array of numbers specifying the dash pattern to use for the path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer/linecap)*
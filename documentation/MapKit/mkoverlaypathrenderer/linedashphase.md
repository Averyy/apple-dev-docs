# lineDashPhase

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The offset (in points) at which to start drawing the dash pattern.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
var lineDashPhase: CGFloat { get set }
```

```objc
@property CGFloat lineDashPhase;
```

## Discussion

Use this property to start drawing a dashed line partway through a segment or gap. For example, a phase value of `6` for the pattern 5-2-3-2 would cause drawing to begin in the middle of the first gap.

The default value of this property is `0`.

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
- [var miterLimit: CGFloat](./miterlimit.md)
  The limiting value that helps avoid spikes at junctions between connected line segments.
- [var lineDashPattern: [NSNumber]?](./linedashpattern.md)
  An array of numbers specifying the dash pattern to use for the path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer/linedashphase)*
# lineDashPattern

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

An array of numbers specifying the dash pattern to use for the path.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
var lineDashPattern: [NSNumber]? { get set }
```

```objc
@property (copy, nullable) NSArray<NSNumber *> * lineDashPattern;
```

#### Discussion

The array contains one or more [`NSNumber`](../../Foundation/nsnumber.md) objects that indicate the lengths (in points) of the line segments and gaps in the pattern. The values in the array alternate, starting with the first line segment length, followed by the first gap length, followed by the second line segment length, and so on.

This property is `nil` by default, which indicates no line dash pattern.

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
- [var lineDashPhase: CGFloat](./linedashphase.md)
  The offset (in points) at which to start drawing the dash pattern.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer/linedashpattern)*
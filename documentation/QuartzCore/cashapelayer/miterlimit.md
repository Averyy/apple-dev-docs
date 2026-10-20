# miterLimit

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

The miter limit used when stroking the shape’s path. Animatable.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var miterLimit: CGFloat { get set }
```

```objc
@property CGFloat miterLimit;
```

#### Discussion

If the current line join style is set to [`miter`](../cashapelayerlinejoin/miter.md) (see [`lineJoin`](./linejoin.md)), the miter limit determines whether the lines should be joined with a bevel instead of a miter. The length of the miter is divided by the line width. If the result is greater than the miter limit, the path is drawn with a bevel.

Default is `10.0`.

## See Also

### Accessing Shape Style Properties
- [var fillColor: CGColor?](./fillcolor.md)
  The color used to fill the shape’s path. Animatable.
- [var fillRule: CAShapeLayerFillRule](./fillrule.md)
  The fill rule used when filling the shape’s path.
- [var lineCap: CAShapeLayerLineCap](./linecap.md)
  Specifies the line cap style for the shape’s path.
- [var lineDashPattern: [NSNumber]?](./linedashpattern.md)
  The dash pattern applied to the shape’s path when stroked.
- [var lineDashPhase: CGFloat](./linedashphase.md)
  The dash phase applied to the shape’s path when stroked. Animatable.
- [var lineJoin: CAShapeLayerLineJoin](./linejoin.md)
  Specifies the line join style for the shape’s path.
- [var lineWidth: CGFloat](./linewidth.md)
  Specifies the line width of the shape’s path. Animatable.
- [var strokeColor: CGColor?](./strokecolor.md)
  The color used to stroke the shape’s path. Animatable.
- [var strokeStart: CGFloat](./strokestart.md)
  The relative location at which to begin stroking the path. Animatable.
- [var strokeEnd: CGFloat](./strokeend.md)
  The relative location at which to stop stroking the path. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cashapelayer/miterlimit)*
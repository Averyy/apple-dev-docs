# lineCap

**Framework**: Core Animation  
**Kind**: property

Specifies the line cap style for the shape’s path.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var lineCap: CAShapeLayerLineCap { get set }
```

#### Discussion

The line cap style specifies the shape of the endpoints of an open path when stroked. The supported values are described in [`Line Cap Values`](line-cap-values.md). The following figure shows the appearance of the available line cap styles.

![None](https://docs-assets.developer.apple.com/published/5639a2a1fdd14a26edcf53a53ca3d86a/media-1965770.gif)

The default is [`butt`](cashapelayerlinecap/butt.md).

## See Also

- [var fillColor: CGColor?](cashapelayer/fillcolor.md)
  The color used to fill the shape’s path. Animatable.
- [var fillRule: CAShapeLayerFillRule](cashapelayer/fillrule.md)
  The fill rule used when filling the shape’s path.
- [var lineDashPattern: [NSNumber]?](cashapelayer/linedashpattern.md)
  The dash pattern applied to the shape’s path when stroked.
- [var lineDashPhase: CGFloat](cashapelayer/linedashphase.md)
  The dash phase applied to the shape’s path when stroked. Animatable.
- [var lineJoin: CAShapeLayerLineJoin](cashapelayer/linejoin.md)
  Specifies the line join style for the shape’s path.
- [var lineWidth: CGFloat](cashapelayer/linewidth.md)
  Specifies the line width of the shape’s path. Animatable.
- [var miterLimit: CGFloat](cashapelayer/miterlimit.md)
  The miter limit used when stroking the shape’s path. Animatable.
- [var strokeColor: CGColor?](cashapelayer/strokecolor.md)
  The color used to stroke the shape’s path. Animatable.
- [var strokeStart: CGFloat](cashapelayer/strokestart.md)
  The relative location at which to begin stroking the path. Animatable.
- [var strokeEnd: CGFloat](cashapelayer/strokeend.md)
  The relative location at which to stop stroking the path. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cashapelayer/linecap)*
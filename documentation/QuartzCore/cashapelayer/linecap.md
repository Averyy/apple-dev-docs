# lineCap

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (copy) CAShapeLayerLineCap lineCap;
```

#### Discussion

The line cap style specifies the shape of the endpoints of an open path when stroked. The supported values are described in [Line Cap Values](../line-cap-values.md). The following figure shows the appearance of the available line cap styles.

![](https://developer.apple.com/tutorials/images/com.apple.quartzcore/media-1965770.gif)

The default is [`butt`](../cashapelayerlinecap/butt.md).

## See Also

### Accessing Shape Style Properties
- [var fillColor: CGColor?](./fillcolor.md)
  The color used to fill the shape’s path. Animatable.
- [var fillRule: CAShapeLayerFillRule](./fillrule.md)
  The fill rule used when filling the shape’s path.
- [var lineDashPattern: [NSNumber]?](./linedashpattern.md)
  The dash pattern applied to the shape’s path when stroked.
- [var lineDashPhase: CGFloat](./linedashphase.md)
  The dash phase applied to the shape’s path when stroked. Animatable.
- [var lineJoin: CAShapeLayerLineJoin](./linejoin.md)
  Specifies the line join style for the shape’s path.
- [var lineWidth: CGFloat](./linewidth.md)
  Specifies the line width of the shape’s path. Animatable.
- [var miterLimit: CGFloat](./miterlimit.md)
  The miter limit used when stroking the shape’s path. Animatable.
- [var strokeColor: CGColor?](./strokecolor.md)
  The color used to stroke the shape’s path. Animatable.
- [var strokeStart: CGFloat](./strokestart.md)
  The relative location at which to begin stroking the path. Animatable.
- [var strokeEnd: CGFloat](./strokeend.md)
  The relative location at which to stop stroking the path. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cashapelayer/linecap)*
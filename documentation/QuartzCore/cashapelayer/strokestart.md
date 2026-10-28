# strokeStart

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

The relative location at which to begin stroking the path. Animatable.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var strokeStart: CGFloat { get set }
```

```objc
@property CGFloat strokeStart;
```

## Discussion

The value of this property must be in the range 0.0 to 1.0. The default value of this property is 0.0.

Combined with the [`strokeEnd`](./strokeend.md) property, this property defines the subregion of the path to stroke. The value in this property indicates the relative point along the path at which to begin stroking while the [`strokeEnd`](./strokeend.md) property defines the end point. A value of 0.0 represents the beginning of the path while a value of 1.0 represents the end of the path. Values in between are interpreted linearly along the path length.

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
- [var miterLimit: CGFloat](./miterlimit.md)
  The miter limit used when stroking the shape’s path. Animatable.
- [var strokeColor: CGColor?](./strokecolor.md)
  The color used to stroke the shape’s path. Animatable.
- [var strokeEnd: CGFloat](./strokeend.md)
  The relative location at which to stop stroking the path. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cashapelayer/strokestart)*
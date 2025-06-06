# fillRule

**Framework**: Core Animation  
**Kind**: property

The fill rule used when filling the shape’s path.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var fillRule: CAShapeLayerFillRule { get set }
```

#### Discussion

The possible values are shown in [`Shape Fill Mode Values`](shape-fill-mode-values.md). The default is [`nonZero`](cashapelayerfillrule/nonzero.md). See [`Winding Rules`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaDrawingGuide/Paths/Paths.html#//apple_ref/doc/uid/TP40003290-CH206-BAJIJJGD) for examples of the two fill rules.

## See Also

- [var fillColor: CGColor?](cashapelayer/fillcolor.md)
  The color used to fill the shape’s path. Animatable.
- [var lineCap: CAShapeLayerLineCap](cashapelayer/linecap.md)
  Specifies the line cap style for the shape’s path.
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

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cashapelayer/fillrule)*
# lineDashPhase

**Framework**: Core Animation  
**Kind**: property

The dash phase applied to the shape’s path when stroked. Animatable.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var lineDashPhase: CGFloat { get set }
```

#### Discussion

Line dash phase specifies how far into the dash pattern the line starts.

Default is `0`.

The following code shows how you can create a “marching ant” effect by adding an animation to a shape layer that animates its [`lineDashPhase`](cashapelayer/linedashphase.md) from `0` to the sum of the segment lengths of its [`lineDashPattern`](cashapelayer/linedashpattern.md).

```swift
let shapeLayer = CAShapeLayer()
shapeLayer.strokeColor = UIColor.black.cgColor
shapeLayer.fillColor = UIColor.clear.cgColor
shapeLayer.lineWidth = 5
shapeLayer.lineDashPattern = [10,5,5,5]
     
let path = CGMutablePath()
path.addLines(between: [CGPoint(x: 0, y: 100),
                        CGPoint(x: 640, y: 100)])
shapeLayer.path = path
     
let lineDashAnimation = CABasicAnimation(keyPath: "lineDashPhase")
lineDashAnimation.fromValue = 0
lineDashAnimation.toValue = shapeLayer.lineDashPattern?.reduce(0) { $0 + $1.intValue }
lineDashAnimation.duration = 1
lineDashAnimation.repeatCount = Float.greatestFiniteMagnitude
     
shapeLayer.add(lineDashAnimation, forKey: nil)
```

## See Also

- [var fillColor: CGColor?](cashapelayer/fillcolor.md)
  The color used to fill the shape’s path. Animatable.
- [var fillRule: CAShapeLayerFillRule](cashapelayer/fillrule.md)
  The fill rule used when filling the shape’s path.
- [var lineCap: CAShapeLayerLineCap](cashapelayer/linecap.md)
  Specifies the line cap style for the shape’s path.
- [var lineDashPattern: [NSNumber]?](cashapelayer/linedashpattern.md)
  The dash pattern applied to the shape’s path when stroked.
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

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cashapelayer/linedashphase)*
# lineDashPattern

**Framework**: Core Animation  
**Kind**: property

The dash pattern applied to the shape’s path when stroked.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var lineDashPattern: [NSNumber]? { get set }
```

#### Discussion

The dash pattern is specified as an array of `NSNumber` objects that specify the lengths of the painted segments and unpainted segments, respectively, of the dash pattern.

For example, passing an array with the values `[2,3]` sets a dash pattern that alternates between a 2-user-space-unit-long painted segment and a 3-user-space-unit-long unpainted segment. Passing the values `[10,5,5,5]` sets the pattern to a 10-unit painted segment, a 5-unit unpainted segment, a 5-unit painted segment, and a 5-unit unpainted segment.

Default is `nil`, a solid line.

The following code shows how how you can create three shape layers using the dash patterns described above. Each shape layer contains a simple path that describes a horizontal line.

```swift
let layer = CALayer()
      
let lineDashPatterns: [[NSNumber]?]  = [nil, [2,3], [10, 5, 5, 5]]
     
for (index, lineDashPattern) in lineDashPatterns.enumerated() {
    
    let shapeLayer = CAShapeLayer()
    shapeLayer.strokeColor = UIColor.black.cgColor
    shapeLayer.lineWidth = 5
    shapeLayer.lineDashPattern = lineDashPattern
    
    let path = CGMutablePath()
    let y = CGFloat(index * 50)
    path.addLines(between: [CGPoint(x: 0, y: y),
                            CGPoint(x: 640, y: y)])
    
    shapeLayer.path = path
    
    layer.addSublayer(shapeLayer)
}
```

The following figure shows three shape layers created with the code above. The top solid line has a `nil` [`lineDashPattern`](cashapelayer/linedashpattern.md), the middle has `[2,3]` and the bottom has `[10,5,5,5]`.

![The effects of different line dash patterns](https://docs-assets.developer.apple.com/published/293471c30f19bccfb3bcfebe7a87871d/media-2825198%402x.png)

## See Also

- [var fillColor: CGColor?](cashapelayer/fillcolor.md)
  The color used to fill the shape’s path. Animatable.
- [var fillRule: CAShapeLayerFillRule](cashapelayer/fillrule.md)
  The fill rule used when filling the shape’s path.
- [var lineCap: CAShapeLayerLineCap](cashapelayer/linecap.md)
  Specifies the line cap style for the shape’s path.
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

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cashapelayer/linedashpattern)*
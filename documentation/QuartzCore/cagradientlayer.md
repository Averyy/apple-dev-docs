# CAGradientLayer

**Framework**: Core Animation  
**Kind**: class

A layer that draws a color gradient over its background color, filling the shape of the layer.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class CAGradientLayer
```

#### Overview

You use a gradient layer to create a color gradient containing an arbitrary number of colors. By default, the colors are spread uniformly across the layer, but you can optionally specify locations for control over the color positions through the gradient.

The following code shows how to create a gradient layer containing four colors that are evenly distributed through the gradient. Rotating the layer by 90° (doc://com.apple.documentation/documentation/corefoundation/cgfloat/1845230-pi `/ 2` radians) gives a horizontal gradient.

```objc
gradientLayer.colors = [UIColor.red.cgColor,
                        UIColor.yellow.cgColor,
                        UIColor.green.cgColor,
                        UIColor.blue.cgColor]
     
gradientLayer.transform = CATransform3DMakeRotation(CGFloat.pi / 2, 0, 0, 1)
```

The following figure shows the appearance of the gradient layer.

![Color gradient layer](https://docs-assets.developer.apple.com/published/44142ddb755d778cdadae1874f04dc62/media-2825193%402x.png)

## Topics

### Gradient Style Properties
- [var colors: [Any]?](cagradientlayer/colors.md)
  An array of `CGColorRef` objects defining the color of each gradient stop. Animatable.
- [var locations: [NSNumber]?](cagradientlayer/locations.md)
  An optional array of NSNumber objects defining the location of each gradient stop. Animatable.
- [var endPoint: CGPoint](cagradientlayer/endpoint.md)
  The end point of the gradient when drawn in the layer’s coordinate space. Animatable.
- [var startPoint: CGPoint](cagradientlayer/startpoint.md)
  The start point of the gradient when drawn in the layer’s coordinate space. Animatable.
- [var type: CAGradientLayerType](cagradientlayer/type.md)
  Style of gradient drawn by the layer.
### Constants
- [Gradient Types](gradient-types.md)
  The style of gradient drawn by the layer.

## Relationships

### Inherits From
- [CALayer](calayer.md)
### Conforms To
- [CAMediaTiming](camediatiming.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class CATextLayer](catextlayer.md)
  A layer that provides simple text layout and rendering of plain or attributed strings.
- [class CAShapeLayer](cashapelayer.md)
  A layer that draws a cubic Bezier spline in its coordinate space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cagradientlayer)*
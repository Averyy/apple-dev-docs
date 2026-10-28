# CAGradientLayer

**Framework**: Core Animation  
**Kind**: class  
**Role**: Class

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

```objc
@interface CAGradientLayer : CALayer
```

## Overview

You use a gradient layer to create a color gradient containing an arbitrary number of colors. By default, the colors are spread uniformly across the layer, but you can optionally specify locations for control over the color positions through the gradient.

The following code shows how to create a gradient layer containing four colors that are evenly distributed through the gradient. Rotating the layer by 90° ([`pi`](../Swift/floatingpoint/pi.md) ⁄ `2` radians) gives a horizontal gradient.

```objc
gradientLayer.colors = [UIColor.red.cgColor,
                        UIColor.yellow.cgColor,
                        UIColor.green.cgColor,
                        UIColor.blue.cgColor]
     
gradientLayer.transform = CATransform3DMakeRotation(CGFloat.pi / 2, 0, 0, 1)
```

The following figure shows the appearance of the gradient layer.

![Color gradient layer](https://developer.apple.com/tutorials/images/com.apple.quartzcore/media-2825193@2x.png)

## Topics

### Gradient Style Properties
- [var colors: [Any]?](./cagradientlayer/colors.md)
  An array of `CGColorRef` objects defining the color of each gradient stop. Animatable.
- [var locations: [NSNumber]?](./cagradientlayer/locations.md)
  An optional array of NSNumber objects defining the location of each gradient stop. Animatable.
- [var endPoint: CGPoint](./cagradientlayer/endpoint.md)
  The end point of the gradient when drawn in the layer’s coordinate space. Animatable.
- [var startPoint: CGPoint](./cagradientlayer/startpoint.md)
  The start point of the gradient when drawn in the layer’s coordinate space. Animatable.
- [var type: CAGradientLayerType](./cagradientlayer/type.md)
  Style of gradient drawn by the layer.
### Constants
- [Gradient Types](./gradient-types.md)
  The style of gradient drawn by the layer.

## Relationships

### Inherits From
- [CALayer](./calayer.md)
### Conforms To
- [CAMediaTiming](./camediatiming.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Text, Shapes, and Gradients
- [class CATextLayer](./catextlayer.md)
  A layer that provides simple text layout and rendering of plain or attributed strings.
- [class CAShapeLayer](./cashapelayer.md)
  A layer that draws a cubic Bezier spline in its coordinate space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cagradientlayer)*
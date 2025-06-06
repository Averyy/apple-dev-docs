# type

**Framework**: Core Animation  
**Kind**: property

Style of gradient drawn by the layer.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var type: CAGradientLayerType { get set }
```

#### Discussion

Defaults to [`axial`](cagradientlayertype/axial.md).

## See Also

- [var colors: [Any]?](cagradientlayer/colors.md)
  An array of `CGColorRef` objects defining the color of each gradient stop. Animatable.
- [var locations: [NSNumber]?](cagradientlayer/locations.md)
  An optional array of NSNumber objects defining the location of each gradient stop. Animatable.
- [var endPoint: CGPoint](cagradientlayer/endpoint.md)
  The end point of the gradient when drawn in the layer’s coordinate space. Animatable.
- [var startPoint: CGPoint](cagradientlayer/startpoint.md)
  The start point of the gradient when drawn in the layer’s coordinate space. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cagradientlayer/type)*
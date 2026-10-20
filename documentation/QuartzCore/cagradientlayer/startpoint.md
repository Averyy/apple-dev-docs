# startPoint

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

The start point of the gradient when drawn in the layer’s coordinate space. Animatable.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var startPoint: CGPoint { get set }
```

```objc
@property CGPoint startPoint;
```

#### Discussion

The start point corresponds to the first stop of the gradient. The point is defined in the unit coordinate space and is then mapped to the layer’s bounds rectangle when drawn.

Default value is `(0.5,0.0)`.

## See Also

### Gradient Style Properties
- [var colors: [Any]?](./colors.md)
  An array of `CGColorRef` objects defining the color of each gradient stop. Animatable.
- [var locations: [NSNumber]?](./locations.md)
  An optional array of NSNumber objects defining the location of each gradient stop. Animatable.
- [var endPoint: CGPoint](./endpoint.md)
  The end point of the gradient when drawn in the layer’s coordinate space. Animatable.
- [var type: CAGradientLayerType](./type.md)
  Style of gradient drawn by the layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cagradientlayer/startpoint)*
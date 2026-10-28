# locations

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

An optional array of NSNumber objects defining the location of each gradient stop. Animatable.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var locations: [NSNumber]? { get set }
```

```objc
@property (copy, nullable) NSArray<NSNumber *> * locations;
```

## Discussion

The gradient stops are specified as values between `0` and `1`. The values must be monotonically increasing. If `nil`, the stops are spread uniformly across the range. Defaults to `nil`.

When rendered, the colors are mapped to the output color space before being interpolated.

## See Also

### Gradient Style Properties
- [var colors: [Any]?](./colors.md)
  An array of `CGColorRef` objects defining the color of each gradient stop. Animatable.
- [var endPoint: CGPoint](./endpoint.md)
  The end point of the gradient when drawn in the layer’s coordinate space. Animatable.
- [var startPoint: CGPoint](./startpoint.md)
  The start point of the gradient when drawn in the layer’s coordinate space. Animatable.
- [var type: CAGradientLayerType](./type.md)
  Style of gradient drawn by the layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cagradientlayer/locations)*
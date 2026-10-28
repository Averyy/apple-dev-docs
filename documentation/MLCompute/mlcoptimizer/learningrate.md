# learningRate

**Framework**: ML Compute  
**Kind**: property  
**Role**: Instance Property

The learning rate.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
var learningRate: Float { get set }
```

```objc
@property (nonatomic, readwrite) float learningRate;
```

## Discussion

This property is readwrite, which enable you to implement a decay during training.

## See Also

### Inspecting an Optimizer
- [var gradientRescale: Float](./gradientrescale.md)
  The rescale value the optimizer applies to gradients during updates.
- [var appliesGradientClipping: Bool](./appliesgradientclipping.md)
  A Boolean value that indicates whether you apply gradient clipping.
- [var gradientClipMax: Float](./gradientclipmax.md)
  The maximum gradient value before the optimizer rescales the gradient, if you enable gradient clipping.
- [var gradientClipMin: Float](./gradientclipmin.md)
  The minimum gradient value before the optimizer rescales the gradient, if you enable gradient clipping.
- [var regularizationScale: Float](./regularizationscale.md)
  The regularization scale.
- [var regularizationType: MLCRegularizationType](./regularizationtype.md)
  The regularization type.
- [var gradientClippingType: MLCGradientClippingType](./gradientclippingtype.md)
  The type of clipping the system applies to the gradient.
- [enum MLCGradientClippingType](../mlcgradientclippingtype.md)
  A clipping type the system applies to a gradient.
- [var maximumClippingNorm: Float](./maximumclippingnorm.md)
  The maximum clipping value.
- [var customGlobalNorm: Float](./customglobalnorm.md)
  A custom norm the system uses in place of the global norm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcoptimizer/learningrate)*
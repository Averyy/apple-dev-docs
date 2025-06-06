# learningRate

**Framework**: ML Compute  
**Kind**: property

The learning rate.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
var learningRate: Float { get set }
```

#### Discussion

This property is readwrite, which enable you to implement a decay during training.

## See Also

- [var gradientRescale: Float](mlcoptimizer/gradientrescale.md)
  The rescale value the optimizer applies to gradients during updates.
- [var appliesGradientClipping: Bool](mlcoptimizer/appliesgradientclipping.md)
  A Boolean value that indicates whether you apply gradient clipping.
- [var gradientClipMax: Float](mlcoptimizer/gradientclipmax.md)
  The maximum gradient value before the optimizer rescales the gradient, if you enable gradient clipping.
- [var gradientClipMin: Float](mlcoptimizer/gradientclipmin.md)
  The minimum gradient value before the optimizer rescales the gradient, if you enable gradient clipping.
- [var regularizationScale: Float](mlcoptimizer/regularizationscale.md)
  The regularization scale.
- [var regularizationType: MLCRegularizationType](mlcoptimizer/regularizationtype.md)
  The regularization type.
- [var gradientClippingType: MLCGradientClippingType](mlcoptimizer/gradientclippingtype.md)
  The type of clipping the system applies to the gradient.
- [enum MLCGradientClippingType](mlcgradientclippingtype.md)
  A clipping type the system applies to a gradient.
- [var maximumClippingNorm: Float](mlcoptimizer/maximumclippingnorm.md)
  The maximum clipping value.
- [var customGlobalNorm: Float](mlcoptimizer/customglobalnorm.md)
  A custom norm the system uses in place of the global norm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcoptimizer/learningrate)*
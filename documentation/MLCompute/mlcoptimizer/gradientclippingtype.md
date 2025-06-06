# gradientClippingType

**Framework**: ML Compute  
**Kind**: property

The type of clipping the system applies to the gradient.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+

## Declaration

```swift
var gradientClippingType: MLCGradientClippingType { get }
```

## See Also

- [var learningRate: Float](mlcoptimizer/learningrate.md)
  The learning rate.
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
- [enum MLCGradientClippingType](mlcgradientclippingtype.md)
  A clipping type the system applies to a gradient.
- [var maximumClippingNorm: Float](mlcoptimizer/maximumclippingnorm.md)
  The maximum clipping value.
- [var customGlobalNorm: Float](mlcoptimizer/customglobalnorm.md)
  A custom norm the system uses in place of the global norm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcoptimizer/gradientclippingtype)*
# regularizationType

**Framework**: ML Compute  
**Kind**: property

The regularization type.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
var regularizationType: MLCRegularizationType { get }
```

## See Also

- [var learningRate: Float](mlcoptimizerdescriptor/learningrate.md)
  The learning rate.
- [var gradientRescale: Float](mlcoptimizerdescriptor/gradientrescale.md)
  The rescale value the optimizer applies to gradients during updates.
- [var appliesGradientClipping: Bool](mlcoptimizerdescriptor/appliesgradientclipping.md)
  A Boolean that indicates whether you apply gradient clipping.
- [var gradientClipMax: Float](mlcoptimizerdescriptor/gradientclipmax.md)
  The maximum gradient value before the optimizer rescales the gradient, if you enabled gradient clipping.
- [var gradientClipMin: Float](mlcoptimizerdescriptor/gradientclipmin.md)
  The minimum gradient value before the optimizer rescales the gradient, if you enabled gradient clipping.
- [var regularizationScale: Float](mlcoptimizerdescriptor/regularizationscale.md)
  The regularization scale.
- [var gradientClippingType: MLCGradientClippingType](mlcoptimizerdescriptor/gradientclippingtype.md)
  The type of clipping the system applies to the gradient.
- [enum MLCGradientClippingType](mlcgradientclippingtype.md)
  A clipping type the system applies to a gradient.
- [var maximumClippingNorm: Float](mlcoptimizerdescriptor/maximumclippingnorm.md)
  The maximum clipping value.
- [var customGlobalNorm: Float](mlcoptimizerdescriptor/customglobalnorm.md)
  A custom norm the system uses in place of the global norm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcoptimizerdescriptor/regularizationtype)*
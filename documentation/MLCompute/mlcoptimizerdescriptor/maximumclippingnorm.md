# maximumClippingNorm

**Framework**: ML Compute  
**Kind**: property

The maximum clipping value.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+

## Declaration

```swift
var maximumClippingNorm: Float { get }
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
- [var regularizationType: MLCRegularizationType](mlcoptimizerdescriptor/regularizationtype.md)
  The regularization type.
- [var gradientClippingType: MLCGradientClippingType](mlcoptimizerdescriptor/gradientclippingtype.md)
  The type of clipping the system applies to the gradient.
- [enum MLCGradientClippingType](mlcgradientclippingtype.md)
  A clipping type the system applies to a gradient.
- [var customGlobalNorm: Float](mlcoptimizerdescriptor/customglobalnorm.md)
  A custom norm the system uses in place of the global norm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcoptimizerdescriptor/maximumclippingnorm)*
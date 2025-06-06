# appliesGradientClipping

**Framework**: ML Compute  
**Kind**: property

A Boolean that indicates whether you apply gradient clipping.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
var appliesGradientClipping: Bool { get }
```

#### Discussion

The default value is `false`.

## See Also

- [var learningRate: Float](mlcoptimizerdescriptor/learningrate.md)
  The learning rate.
- [var gradientRescale: Float](mlcoptimizerdescriptor/gradientrescale.md)
  The rescale value the optimizer applies to gradients during updates.
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
- [var maximumClippingNorm: Float](mlcoptimizerdescriptor/maximumclippingnorm.md)
  The maximum clipping value.
- [var customGlobalNorm: Float](mlcoptimizerdescriptor/customglobalnorm.md)
  A custom norm the system uses in place of the global norm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcoptimizerdescriptor/appliesgradientclipping)*
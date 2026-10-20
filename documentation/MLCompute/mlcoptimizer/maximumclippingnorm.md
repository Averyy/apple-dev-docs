# maximumClippingNorm

**Framework**: ML Compute  
**Kind**: property  
**Role**: Instance Property

The maximum clipping value.

**Availability**:
- iOS 15.0+ - Deprecated in 17.4
- iPadOS 15.0+ - Deprecated in 17.4
- Mac Catalyst 15.0+ - Deprecated in 17.4
- macOS 12.0+ - Deprecated in 14.3
- tvOS 15.0+ - Deprecated in 17.4

## Declaration

```swift
var maximumClippingNorm: Float { get }
```

```objc
@property (nonatomic, readonly) float maximumClippingNorm;
```

## See Also

### Inspecting an Optimizer
- [var learningRate: Float](./learningrate.md)
  The learning rate.
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
- [var customGlobalNorm: Float](./customglobalnorm.md)
  A custom norm the system uses in place of the global norm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcoptimizer/maximumclippingnorm)*
# MLCGradientClippingType

**Framework**: ML Compute  
**Kind**: enum

A clipping type the system applies to a gradient.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+

## Declaration

```swift
enum MLCGradientClippingType
```

## Topics

### Gradient Clipping Types
- [MLCGradientClippingType.byValue](mlcgradientclippingtype/byvalue.md)
  An option that clips by value.
- [MLCGradientClippingType.byNorm](mlcgradientclippingtype/bynorm.md)
  An option that clips by norm.
- [MLCGradientClippingType.byGlobalNorm](mlcgradientclippingtype/byglobalnorm.md)
  An option that clips by global norm.
- [var debugDescription: String](mlcgradientclippingtype/debugdescription.md)
  A textual description of the gradient clipping type, suitable for debugging.
### Initializers
- [init?(rawValue: Int32)](mlcgradientclippingtype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

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
- [var gradientClippingType: MLCGradientClippingType](mlcoptimizer/gradientclippingtype.md)
  The type of clipping the system applies to the gradient.
- [var maximumClippingNorm: Float](mlcoptimizer/maximumclippingnorm.md)
  The maximum clipping value.
- [var customGlobalNorm: Float](mlcoptimizer/customglobalnorm.md)
  A custom norm the system uses in place of the global norm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcgradientclippingtype)*
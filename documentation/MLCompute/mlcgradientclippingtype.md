# MLCGradientClippingType

**Framework**: ML Compute  
**Kind**: enum  
**Role**: Enumeration

A clipping type the system applies to a gradient.

**Availability**:
- iOS 15.0+ - Deprecated in 17.4
- iPadOS 15.0+ - Deprecated in 17.4
- Mac Catalyst 15.0+ - Deprecated in 17.4
- macOS 12.0+ - Deprecated in 14.3
- tvOS 15.0+ - Deprecated in 17.4

## Declaration

```swift
enum MLCGradientClippingType
```

```c
enum MLCGradientClippingType : int32_t;
```

## Topics

### Gradient Clipping Types
- [MLCGradientClippingType.byValue](./mlcgradientclippingtype/byvalue.md)
  An option that clips by value.
- [MLCGradientClippingType.byNorm](./mlcgradientclippingtype/bynorm.md)
  An option that clips by norm.
- [MLCGradientClippingType.byGlobalNorm](./mlcgradientclippingtype/byglobalnorm.md)
  An option that clips by global norm.
- [var debugDescription: String](./mlcgradientclippingtype/debugdescription.md)
  A textual description of the gradient clipping type, suitable for debugging.
### Initializers
- [init?(rawValue: Int32)](./mlcgradientclippingtype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Inspecting an Optimizer
- [var learningRate: Float](./mlcoptimizer/learningrate.md)
  The learning rate.
- [var gradientRescale: Float](./mlcoptimizer/gradientrescale.md)
  The rescale value the optimizer applies to gradients during updates.
- [var appliesGradientClipping: Bool](./mlcoptimizer/appliesgradientclipping.md)
  A Boolean value that indicates whether you apply gradient clipping.
- [var gradientClipMax: Float](./mlcoptimizer/gradientclipmax.md)
  The maximum gradient value before the optimizer rescales the gradient, if you enable gradient clipping.
- [var gradientClipMin: Float](./mlcoptimizer/gradientclipmin.md)
  The minimum gradient value before the optimizer rescales the gradient, if you enable gradient clipping.
- [var regularizationScale: Float](./mlcoptimizer/regularizationscale.md)
  The regularization scale.
- [var regularizationType: MLCRegularizationType](./mlcoptimizer/regularizationtype.md)
  The regularization type.
- [var gradientClippingType: MLCGradientClippingType](./mlcoptimizer/gradientclippingtype.md)
  The type of clipping the system applies to the gradient.
- [var maximumClippingNorm: Float](./mlcoptimizer/maximumclippingnorm.md)
  The maximum clipping value.
- [var customGlobalNorm: Float](./mlcoptimizer/customglobalnorm.md)
  A custom norm the system uses in place of the global norm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcgradientclippingtype)*
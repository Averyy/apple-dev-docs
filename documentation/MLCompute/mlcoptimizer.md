# MLCOptimizer

**Framework**: ML Compute  
**Kind**: class

The base class for all framework optimizers.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
class MLCOptimizer
```

## Topics

### Inspecting an Optimizer
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
- [enum MLCGradientClippingType](mlcgradientclippingtype.md)
  A clipping type the system applies to a gradient.
- [var maximumClippingNorm: Float](mlcoptimizer/maximumclippingnorm.md)
  The maximum clipping value.
- [var customGlobalNorm: Float](mlcoptimizer/customglobalnorm.md)
  A custom norm the system uses in place of the global norm.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [MLCAdamOptimizer](mlcadamoptimizer.md)
- [MLCAdamWOptimizer](mlcadamwoptimizer.md)
- [MLCRMSPropOptimizer](mlcrmspropoptimizer.md)
- [MLCSGDOptimizer](mlcsgdoptimizer.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MLCSGDOptimizer](mlcsgdoptimizer.md)
  An optimizer that represents the stochastic gradient decent algorithm.
- [class MLCRMSPropOptimizer](mlcrmspropoptimizer.md)
  An optimizer that represents the root mean square propagation algorithm.
- [class MLCAdamOptimizer](mlcadamoptimizer.md)
  An optimizer that represents the adaptive moment estimation algorithm.
- [class MLCAdamWOptimizer](mlcadamwoptimizer.md)
  An optimizer that represents the Adam algorithm with weight decay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcoptimizer)*
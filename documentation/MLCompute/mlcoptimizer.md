# MLCOptimizer

**Framework**: ML Compute  
**Kind**: class  
**Role**: Class

The base class for all framework optimizers.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
class MLCOptimizer
```

```objc
@interface MLCOptimizer : NSObject
```

## Topics

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
- [enum MLCGradientClippingType](./mlcgradientclippingtype.md)
  A clipping type the system applies to a gradient.
- [var maximumClippingNorm: Float](./mlcoptimizer/maximumclippingnorm.md)
  The maximum clipping value.
- [var customGlobalNorm: Float](./mlcoptimizer/customglobalnorm.md)
  A custom norm the system uses in place of the global norm.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [MLCAdamOptimizer](./mlcadamoptimizer.md)
- [MLCAdamWOptimizer](./mlcadamwoptimizer.md)
- [MLCRMSPropOptimizer](./mlcrmspropoptimizer.md)
- [MLCSGDOptimizer](./mlcsgdoptimizer.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Optimizer Types
- [class MLCSGDOptimizer](./mlcsgdoptimizer.md)
  An optimizer that represents the stochastic gradient decent algorithm.
- [class MLCRMSPropOptimizer](./mlcrmspropoptimizer.md)
  An optimizer that represents the root mean square propagation algorithm.
- [class MLCAdamOptimizer](./mlcadamoptimizer.md)
  An optimizer that represents the adaptive moment estimation algorithm.
- [class MLCAdamWOptimizer](./mlcadamwoptimizer.md)
  An optimizer that represents the Adam algorithm with weight decay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcoptimizer)*
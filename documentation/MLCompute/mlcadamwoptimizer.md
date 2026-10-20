# MLCAdamWOptimizer

**Framework**: ML Compute  
**Kind**: class  
**Role**: Class

An optimizer that represents the Adam algorithm with weight decay.

**Availability**:
- iOS 15.0+ - Deprecated in 17.4
- iPadOS 15.0+ - Deprecated in 17.4
- Mac Catalyst 15.0+ - Deprecated in 17.4
- macOS 12.0+ - Deprecated in 14.3
- tvOS 15.0+ - Deprecated in 17.4

## Declaration

```swift
class MLCAdamWOptimizer
```

```objc
@interface MLCAdamWOptimizer : MLCOptimizer
```

## Topics

### Creating an AdamW Optimizer
- [convenience init(descriptor: MLCOptimizerDescriptor)](./mlcadamwoptimizer/init%28descriptor%29.md)
  Creates a default optimizer with the descriptor you specify.
- [convenience init(descriptor: MLCOptimizerDescriptor, beta1: Float, beta2: Float, epsilon: Float, usesAMSGrad: Bool, timeStep: Int)](./mlcadamwoptimizer/init%28descriptor,beta1,beta2,epsilon,usesamsgrad,timestep%29.md)
  Creates an AdamW optimizer with the values you specify.
### Inspecting an AdamW Optimizer
- [var beta1: Float](./mlcadamwoptimizer/beta1.md)
  The coefficent for computing running averages of gradient.
- [var beta2: Float](./mlcadamwoptimizer/beta2.md)
  The coefficent for computing running averages of square of gradient.
- [var epsilon: Float](./mlcadamwoptimizer/epsilon.md)
  The epsilon value for improving numerical stability.
- [var timeStep: Int](./mlcadamwoptimizer/timestep.md)
  The initial timestep for the update.
- [var usesAMSGrad: Bool](./mlcadamwoptimizer/usesamsgrad.md)
  A Boolean value that indicates whether to use a variant of the algorithm.

## Relationships

### Inherits From
- [MLCOptimizer](./mlcoptimizer.md)
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
- [class MLCOptimizer](./mlcoptimizer.md)
  The base class for all framework optimizers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcadamwoptimizer)*
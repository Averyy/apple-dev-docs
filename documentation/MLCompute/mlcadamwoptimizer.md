# MLCAdamWOptimizer

**Framework**: ML Compute  
**Kind**: class

An optimizer that represents the Adam algorithm with weight decay.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+

## Declaration

```swift
class MLCAdamWOptimizer
```

## Topics

### Creating an AdamW Optimizer
- [convenience init(descriptor: MLCOptimizerDescriptor)](mlcadamwoptimizer/init(descriptor:).md)
  Creates a default optimizer with the descriptor you specify.
- [convenience init(descriptor: MLCOptimizerDescriptor, beta1: Float, beta2: Float, epsilon: Float, usesAMSGrad: Bool, timeStep: Int)](mlcadamwoptimizer/init(descriptor:beta1:beta2:epsilon:usesamsgrad:timestep:).md)
  Creates an AdamW optimizer with the values you specify.
### Inspecting an AdamW Optimizer
- [var beta1: Float](mlcadamwoptimizer/beta1.md)
  The coefficent for computing running averages of gradient.
- [var beta2: Float](mlcadamwoptimizer/beta2.md)
  The coefficent for computing running averages of square of gradient.
- [var epsilon: Float](mlcadamwoptimizer/epsilon.md)
  The epsilon value for improving numerical stability.
- [var timeStep: Int](mlcadamwoptimizer/timestep.md)
  The initial timestep for the update.
- [var usesAMSGrad: Bool](mlcadamwoptimizer/usesamsgrad.md)
  A Boolean value that indicates whether to use a variant of the algorithm.

## Relationships

### Inherits From
- [MLCOptimizer](mlcoptimizer.md)
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
- [class MLCOptimizer](mlcoptimizer.md)
  The base class for all framework optimizers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcadamwoptimizer)*
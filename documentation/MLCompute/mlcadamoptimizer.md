# MLCAdamOptimizer

**Framework**: ML Compute  
**Kind**: class

An optimizer that represents the adaptive moment estimation algorithm.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
class MLCAdamOptimizer
```

## Topics

### Creating an Adam Optimizer
- [convenience init(descriptor: MLCOptimizerDescriptor)](mlcadamoptimizer/init(descriptor:).md)
  Creates an Adam optimizer with the descriptor you specify.
- [convenience init(descriptor: MLCOptimizerDescriptor, beta1: Float, beta2: Float, epsilon: Float, timeStep: Int)](mlcadamoptimizer/init(descriptor:beta1:beta2:epsilon:timestep:).md)
  Creates an Adam optimizer with the values you specify.
- [convenience init(descriptor: MLCOptimizerDescriptor, beta1: Float, beta2: Float, epsilon: Float, usesAMSGrad: Bool, timeStep: Int)](mlcadamoptimizer/init(descriptor:beta1:beta2:epsilon:usesamsgrad:timestep:).md)
  Creates an Adam optimizer with the values you specify.
### Inspecting an Adam Optimizer
- [var beta1: Float](mlcadamoptimizer/beta1.md)
  The coefficent for computing running averages of gradient.
- [var beta2: Float](mlcadamoptimizer/beta2.md)
  The coefficent for computing running averages of square of gradient.
- [var epsilon: Float](mlcadamoptimizer/epsilon.md)
  The epsilon value for improving numerical stability.
- [var timeStep: Int](mlcadamoptimizer/timestep.md)
  The initial timestep for the update.
- [var usesAMSGrad: Bool](mlcadamoptimizer/usesamsgrad.md)
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
- [class MLCAdamWOptimizer](mlcadamwoptimizer.md)
  An optimizer that represents the Adam algorithm with weight decay.
- [class MLCOptimizer](mlcoptimizer.md)
  The base class for all framework optimizers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcadamoptimizer)*
# MLCSGDOptimizer

**Framework**: ML Compute  
**Kind**: class

An optimizer that represents the stochastic gradient decent algorithm.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
class MLCSGDOptimizer
```

## Topics

### Creating an SGD Optimizer
- [convenience init(descriptor: MLCOptimizerDescriptor)](mlcsgdoptimizer/init(descriptor:).md)
  Creates an SGD optimizer with the descriptor you specify.
- [convenience init(descriptor: MLCOptimizerDescriptor, momentumScale: Float, usesNesterovMomentum: Bool)](mlcsgdoptimizer/init(descriptor:momentumscale:usesnesterovmomentum:).md)
  Create an SGD optimizer with the descriptor, momentum scale, and option to enable Nesterov momentum that you specify.
### Inspecting an SGD Optimizer
- [var momentumScale: Float](mlcsgdoptimizer/momentumscale.md)
  A hyper-parameter specifying the momentum factor.
- [var usesNesterovMomentum: Bool](mlcsgdoptimizer/usesnesterovmomentum.md)
  A Boolean that indicates whether you enable Nesterov momentum.

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

- [class MLCRMSPropOptimizer](mlcrmspropoptimizer.md)
  An optimizer that represents the root mean square propagation algorithm.
- [class MLCAdamOptimizer](mlcadamoptimizer.md)
  An optimizer that represents the adaptive moment estimation algorithm.
- [class MLCAdamWOptimizer](mlcadamwoptimizer.md)
  An optimizer that represents the Adam algorithm with weight decay.
- [class MLCOptimizer](mlcoptimizer.md)
  The base class for all framework optimizers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcsgdoptimizer)*
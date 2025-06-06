# MLCRMSPropOptimizer

**Framework**: ML Compute  
**Kind**: class

An optimizer that represents the root mean square propagation algorithm.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.2+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
class MLCRMSPropOptimizer
```

## Topics

### Creating an RMSProp Optimizer
- [convenience init(descriptor: MLCOptimizerDescriptor)](mlcrmspropoptimizer/init(descriptor:).md)
  Creates an RMSProp optimizer with the descriptor you specify.
- [convenience init(descriptor: MLCOptimizerDescriptor, momentumScale: Float, alpha: Float, epsilon: Float, isCentered: Bool)](mlcrmspropoptimizer/init(descriptor:momentumscale:alpha:epsilon:iscentered:).md)
  Creates an RMSProp optimizer with the descriptor, momentum scale, smoothing, epsilon, and option to compute the centered RMSProp that you specify.
### Inspecting an RMSProp Optimizer
- [var momentumScale: Float](mlcrmspropoptimizer/momentumscale.md)
  A hyper-parameter that specifies the momentum factor.
- [var alpha: Float](mlcrmspropoptimizer/alpha.md)
  The constant for smoothing.
- [var epsilon: Float](mlcrmspropoptimizer/epsilon.md)
  The epsilon value you use to improve numerical stability.
- [var isCentered: Bool](mlcrmspropoptimizer/iscentered.md)
  A Boolean that indicates whether you compute the centered RMSProp.

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
- [class MLCAdamOptimizer](mlcadamoptimizer.md)
  An optimizer that represents the adaptive moment estimation algorithm.
- [class MLCAdamWOptimizer](mlcadamwoptimizer.md)
  An optimizer that represents the Adam algorithm with weight decay.
- [class MLCOptimizer](mlcoptimizer.md)
  The base class for all framework optimizers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcrmspropoptimizer)*
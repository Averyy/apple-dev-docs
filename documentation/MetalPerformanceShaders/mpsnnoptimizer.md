# MPSNNOptimizer

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

The base class for optimization layers.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
class MPSNNOptimizer
```

```objc
@interface MPSNNOptimizer : MPSKernel
```

## Topics

### Instance Properties
- [var applyGradientClipping: Bool](./mpsnnoptimizer/applygradientclipping.md)
- [var gradientClipMax: Float](./mpsnnoptimizer/gradientclipmax.md)
- [var gradientClipMin: Float](./mpsnnoptimizer/gradientclipmin.md)
- [var gradientRescale: Float](./mpsnnoptimizer/gradientrescale.md)
- [var learningRate: Float](./mpsnnoptimizer/learningrate.md)
- [var regularizationScale: Float](./mpsnnoptimizer/regularizationscale.md)
- [var regularizationType: MPSNNRegularizationType](./mpsnnoptimizer/regularizationtype.md)
### Instance Methods
- [func setLearningRate(Float)](./mpsnnoptimizer/setlearningrate%28_%29.md)

## Relationships

### Inherits From
- [MPSKernel](./mpskernel.md)
### Inherited By
- [MPSNNOptimizerAdam](./mpsnnoptimizeradam.md)
- [MPSNNOptimizerRMSProp](./mpsnnoptimizerrmsprop.md)
- [MPSNNOptimizerStochasticGradientDescent](./mpsnnoptimizerstochasticgradientdescent.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Optimization Layers
- [class MPSNNOptimizerAdam](./mpsnnoptimizeradam.md)
  An optimization layer that performs an Adam pdate.
- [class MPSNNOptimizerRMSProp](./mpsnnoptimizerrmsprop.md)
  An optimization layer that performs a root mean square propagation update.
- [class MPSNNOptimizerStochasticGradientDescent](./mpsnnoptimizerstochasticgradientdescent.md)
  An optimization layer that performs a gradient descent with an optional momentum update.
- [class MPSNNOptimizerDescriptor](./mpsnnoptimizerdescriptor.md)
  An object that specifies properties used by an optimizer kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnoptimizer)*
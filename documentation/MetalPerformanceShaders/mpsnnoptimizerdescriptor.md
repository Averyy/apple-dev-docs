# MPSNNOptimizerDescriptor

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

An object that specifies properties used by an optimizer kernel.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
class MPSNNOptimizerDescriptor
```

```objc
@interface MPSNNOptimizerDescriptor : NSObject
```

## Topics

### Initializers
- [init(learningRate: Float, gradientRescale: Float, applyGradientClipping: Bool, gradientClipMax: Float, gradientClipMin: Float, regularizationType: MPSNNRegularizationType, regularizationScale: Float)](./mpsnnoptimizerdescriptor/init%28learningrate,gradientrescale,applygradientclipping,gradientclipmax,gradientclipmin,regularizationtype,regularizationscale%29.md)
- [init(learningRate: Float, gradientRescale: Float, regularizationType: MPSNNRegularizationType, regularizationScale: Float)](./mpsnnoptimizerdescriptor/init%28learningrate,gradientrescale,regularizationtype,regularizationscale%29.md)
### Instance Properties
- [var applyGradientClipping: Bool](./mpsnnoptimizerdescriptor/applygradientclipping.md)
- [var gradientClipMax: Float](./mpsnnoptimizerdescriptor/gradientclipmax.md)
- [var gradientClipMin: Float](./mpsnnoptimizerdescriptor/gradientclipmin.md)
- [var gradientRescale: Float](./mpsnnoptimizerdescriptor/gradientrescale.md)
- [var learningRate: Float](./mpsnnoptimizerdescriptor/learningrate.md)
- [var regularizationScale: Float](./mpsnnoptimizerdescriptor/regularizationscale.md)
- [var regularizationType: MPSNNRegularizationType](./mpsnnoptimizerdescriptor/regularizationtype.md)
### Type Methods
- [+ optimizerDescriptorWithLearningRate:gradientRescale:applyGradientClipping:gradientClipMax:gradientClipMin:regularizationType:regularizationScale:](./mpsnnoptimizerdescriptor/optimizerdescriptorwithlearningrate_gradientrescale_applygradientclipping_gradientclipmax_gradientclipmin_regularizationtype_regularizationscale_.md)
- [+ optimizerDescriptorWithLearningRate:gradientRescale:regularizationType:regularizationScale:](./mpsnnoptimizerdescriptor/optimizerdescriptorwithlearningrate_gradientrescale_regularizationtype_regularizationscale_.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Optimization Layers
- [class MPSNNOptimizerAdam](./mpsnnoptimizeradam.md)
  An optimization layer that performs an Adam pdate.
- [class MPSNNOptimizerRMSProp](./mpsnnoptimizerrmsprop.md)
  An optimization layer that performs a root mean square propagation update.
- [class MPSNNOptimizerStochasticGradientDescent](./mpsnnoptimizerstochasticgradientdescent.md)
  An optimization layer that performs a gradient descent with an optional momentum update.
- [class MPSNNOptimizer](./mpsnnoptimizer.md)
  The base class for optimization layers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnoptimizerdescriptor)*
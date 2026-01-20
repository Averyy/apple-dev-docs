# MPSNNOptimizerRMSProp

**Framework**: Metal Performance Shaders  
**Kind**: class

An optimization layer that performs a root mean square propagation update.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
class MPSNNOptimizerRMSProp
```

## Topics

### Initializers
- [init(device: any MTLDevice, decay: Double, epsilon: Float, optimizerDescriptor: MPSNNOptimizerDescriptor)](mpsnnoptimizerrmsprop/init(device:decay:epsilon:optimizerdescriptor:).md)
- [init(device: any MTLDevice, learningRate: Float)](mpsnnoptimizerrmsprop/init(device:learningrate:).md)
### Instance Properties
- [var decay: Double](mpsnnoptimizerrmsprop/decay.md)
- [var epsilon: Float](mpsnnoptimizerrmsprop/epsilon.md)
### Instance Methods
- [func encode(commandBuffer: any MTLCommandBuffer, batchNormalizationGradientState: MPSCNNBatchNormalizationState, batchNormalizationSourceState: MPSCNNBatchNormalizationState, inputSumOfSquaresVectors: [MPSVector]?, resultState: MPSCNNNormalizationGammaAndBetaState)](mpsnnoptimizerrmsprop/encode(commandbuffer:batchnormalizationgradientstate:batchnormalizationsourcestate:inputsumofsquaresvectors:resultstate:).md)
- [func encode(commandBuffer: any MTLCommandBuffer, batchNormalizationState: MPSCNNBatchNormalizationState, inputSumOfSquaresVectors: [MPSVector]?, resultState: MPSCNNNormalizationGammaAndBetaState)](mpsnnoptimizerrmsprop/encode(commandbuffer:batchnormalizationstate:inputsumofsquaresvectors:resultstate:).md)
- [func encode(commandBuffer: any MTLCommandBuffer, convolutionGradientState: MPSCNNConvolutionGradientState, convolutionSourceState: MPSCNNConvolutionWeightsAndBiasesState, inputSumOfSquaresVectors: [MPSVector]?, resultState: MPSCNNConvolutionWeightsAndBiasesState)](mpsnnoptimizerrmsprop/encode(commandbuffer:convolutiongradientstate:convolutionsourcestate:inputsumofsquaresvectors:resultstate:).md)
- [func encode(commandBuffer: any MTLCommandBuffer, inputGradientMatrix: MPSMatrix, inputValuesMatrix: MPSMatrix, inputSumOfSquaresMatrix: MPSMatrix, resultValuesMatrix: MPSMatrix)](mpsnnoptimizerrmsprop/encode(commandbuffer:inputgradientmatrix:inputvaluesmatrix:inputsumofsquaresmatrix:resultvaluesmatrix:).md)
- [func encode(commandBuffer: any MTLCommandBuffer, inputGradientVector: MPSVector, inputValuesVector: MPSVector, inputSumOfSquaresVector: MPSVector, resultValuesVector: MPSVector)](mpsnnoptimizerrmsprop/encode(commandbuffer:inputgradientvector:inputvaluesvector:inputsumofsquaresvector:resultvaluesvector:).md)

## Relationships

### Inherits From
- [MPSNNOptimizer](mpsnnoptimizer.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class MPSNNOptimizerAdam](mpsnnoptimizeradam.md)
  An optimization layer that performs an Adam pdate.
- [class MPSNNOptimizerStochasticGradientDescent](mpsnnoptimizerstochasticgradientdescent.md)
  An optimization layer that performs a gradient descent with an optional momentum update.
- [class MPSNNOptimizer](mpsnnoptimizer.md)
  The base class for optimization layers.
- [class MPSNNOptimizerDescriptor](mpsnnoptimizerdescriptor.md)
  An object that specifies properties used by an optimizer kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnoptimizerrmsprop)*
# MPSNNOptimizerRMSProp

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

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

```objc
@interface MPSNNOptimizerRMSProp : MPSNNOptimizer
```

## Topics

### Initializers
- [init(device: any MTLDevice, decay: Double, epsilon: Float, optimizerDescriptor: MPSNNOptimizerDescriptor)](./mpsnnoptimizerrmsprop/init%28device,decay,epsilon,optimizerdescriptor%29.md)
- [init(device: any MTLDevice, learningRate: Float)](./mpsnnoptimizerrmsprop/init%28device,learningrate%29.md)
### Instance Properties
- [var decay: Double](./mpsnnoptimizerrmsprop/decay.md)
- [var epsilon: Float](./mpsnnoptimizerrmsprop/epsilon.md)
### Instance Methods
- [func encode(commandBuffer: any MTLCommandBuffer, batchNormalizationGradientState: MPSCNNBatchNormalizationState, batchNormalizationSourceState: MPSCNNBatchNormalizationState, inputSumOfSquaresVectors: [MPSVector]?, resultState: MPSCNNNormalizationGammaAndBetaState)](./mpsnnoptimizerrmsprop/encode%28commandbuffer,batchnormalizationgradientstate,batchnormalizationsourcestate,inputsumofsquaresvectors,resultstate%29.md)
- [func encode(commandBuffer: any MTLCommandBuffer, batchNormalizationState: MPSCNNBatchNormalizationState, inputSumOfSquaresVectors: [MPSVector]?, resultState: MPSCNNNormalizationGammaAndBetaState)](./mpsnnoptimizerrmsprop/encode%28commandbuffer,batchnormalizationstate,inputsumofsquaresvectors,resultstate%29.md)
- [func encode(commandBuffer: any MTLCommandBuffer, convolutionGradientState: MPSCNNConvolutionGradientState, convolutionSourceState: MPSCNNConvolutionWeightsAndBiasesState, inputSumOfSquaresVectors: [MPSVector]?, resultState: MPSCNNConvolutionWeightsAndBiasesState)](./mpsnnoptimizerrmsprop/encode%28commandbuffer,convolutiongradientstate,convolutionsourcestate,inputsumofsquaresvectors,resultstate%29.md)
- [func encode(commandBuffer: any MTLCommandBuffer, inputGradientMatrix: MPSMatrix, inputValuesMatrix: MPSMatrix, inputSumOfSquaresMatrix: MPSMatrix, resultValuesMatrix: MPSMatrix)](./mpsnnoptimizerrmsprop/encode%28commandbuffer,inputgradientmatrix,inputvaluesmatrix,inputsumofsquaresmatrix,resultvaluesmatrix%29.md)
- [func encode(commandBuffer: any MTLCommandBuffer, inputGradientVector: MPSVector, inputValuesVector: MPSVector, inputSumOfSquaresVector: MPSVector, resultValuesVector: MPSVector)](./mpsnnoptimizerrmsprop/encode%28commandbuffer,inputgradientvector,inputvaluesvector,inputsumofsquaresvector,resultvaluesvector%29.md)

## Relationships

### Inherits From
- [MPSNNOptimizer](./mpsnnoptimizer.md)
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
- [class MPSNNOptimizerStochasticGradientDescent](./mpsnnoptimizerstochasticgradientdescent.md)
  An optimization layer that performs a gradient descent with an optional momentum update.
- [class MPSNNOptimizer](./mpsnnoptimizer.md)
  The base class for optimization layers.
- [class MPSNNOptimizerDescriptor](./mpsnnoptimizerdescriptor.md)
  An object that specifies properties used by an optimizer kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnoptimizerrmsprop)*
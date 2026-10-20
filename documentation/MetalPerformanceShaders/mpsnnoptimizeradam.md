# MPSNNOptimizerAdam

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

An optimization layer that performs an Adam pdate.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
class MPSNNOptimizerAdam
```

```objc
@interface MPSNNOptimizerAdam : MPSNNOptimizer
```

## Topics

### Initializers
- [init(device: any MTLDevice, beta1: Double, beta2: Double, epsilon: Float, timeStep: Int, optimizerDescriptor: MPSNNOptimizerDescriptor)](./mpsnnoptimizeradam/init%28device,beta1,beta2,epsilon,timestep,optimizerdescriptor%29.md)
- [init(device: any MTLDevice, learningRate: Float)](./mpsnnoptimizeradam/init%28device,learningrate%29.md)
### Instance Properties
- [var beta1: Double](./mpsnnoptimizeradam/beta1.md)
- [var beta2: Double](./mpsnnoptimizeradam/beta2.md)
- [var epsilon: Float](./mpsnnoptimizeradam/epsilon.md)
- [var timeStep: Int](./mpsnnoptimizeradam/timestep.md)
### Instance Methods
- [func encode(commandBuffer: any MTLCommandBuffer, batchNormalizationGradientState: MPSCNNBatchNormalizationState, batchNormalizationSourceState: MPSCNNBatchNormalizationState, inputMomentumVectors: [MPSVector], inputVelocityVectors: [MPSVector], maximumVelocityVectors: [MPSVector]?, resultState: MPSCNNNormalizationGammaAndBetaState)](./mpsnnoptimizeradam/encode%28commandbuffer,batchnormalizationgradientstate,batchnormalizationsourcestate,inputmomentumvectors,inputvelocityvectors,maximumvelocityvectors,resultstate%29.md)
- [func encode(commandBuffer: any MTLCommandBuffer, batchNormalizationGradientState: MPSCNNBatchNormalizationState, batchNormalizationSourceState: MPSCNNBatchNormalizationState, inputMomentumVectors: [MPSVector]?, inputVelocityVectors: [MPSVector]?, resultState: MPSCNNNormalizationGammaAndBetaState)](./mpsnnoptimizeradam/encode%28commandbuffer,batchnormalizationgradientstate,batchnormalizationsourcestate,inputmomentumvectors,inputvelocityvectors,resultstate%29.md)
- [func encode(commandBuffer: any MTLCommandBuffer, batchNormalizationState: MPSCNNBatchNormalizationState, inputMomentumVectors: [MPSVector], inputVelocityVectors: [MPSVector], maximumVelocityVectors: [MPSVector]?, resultState: MPSCNNNormalizationGammaAndBetaState)](./mpsnnoptimizeradam/encode%28commandbuffer,batchnormalizationstate,inputmomentumvectors,inputvelocityvectors,maximumvelocityvectors,resultstate%29.md)
- [func encode(commandBuffer: any MTLCommandBuffer, batchNormalizationState: MPSCNNBatchNormalizationState, inputMomentumVectors: [MPSVector]?, inputVelocityVectors: [MPSVector]?, resultState: MPSCNNNormalizationGammaAndBetaState)](./mpsnnoptimizeradam/encode%28commandbuffer,batchnormalizationstate,inputmomentumvectors,inputvelocityvectors,resultstate%29.md)
- [func encode(commandBuffer: any MTLCommandBuffer, convolutionGradientState: MPSCNNConvolutionGradientState, convolutionSourceState: MPSCNNConvolutionWeightsAndBiasesState, inputMomentumVectors: [MPSVector], inputVelocityVectors: [MPSVector], maximumVelocityVectors: [MPSVector]?, resultState: MPSCNNConvolutionWeightsAndBiasesState)](./mpsnnoptimizeradam/encode%28commandbuffer,convolutiongradientstate,convolutionsourcestate,inputmomentumvectors,inputvelocityvectors,maximumvelocityvectors,resultstate%29.md)
- [func encode(commandBuffer: any MTLCommandBuffer, convolutionGradientState: MPSCNNConvolutionGradientState, convolutionSourceState: MPSCNNConvolutionWeightsAndBiasesState, inputMomentumVectors: [MPSVector]?, inputVelocityVectors: [MPSVector]?, resultState: MPSCNNConvolutionWeightsAndBiasesState)](./mpsnnoptimizeradam/encode%28commandbuffer,convolutiongradientstate,convolutionsourcestate,inputmomentumvectors,inputvelocityvectors,resultstate%29.md)
- [func encode(commandBuffer: any MTLCommandBuffer, inputGradientMatrix: MPSMatrix, inputValuesMatrix: MPSMatrix, inputMomentumMatrix: MPSMatrix, inputVelocityMatrix: MPSMatrix, maximumVelocityMatrix: MPSMatrix?, resultValuesMatrix: MPSMatrix)](./mpsnnoptimizeradam/encode%28commandbuffer,inputgradientmatrix,inputvaluesmatrix,inputmomentummatrix,inputvelocitymatrix,maximumvelocitymatrix,resultvaluesmatrix%29.md)
- [func encode(commandBuffer: any MTLCommandBuffer, inputGradientMatrix: MPSMatrix, inputValuesMatrix: MPSMatrix, inputMomentumMatrix: MPSMatrix, inputVelocityMatrix: MPSMatrix, resultValuesMatrix: MPSMatrix)](./mpsnnoptimizeradam/encode%28commandbuffer,inputgradientmatrix,inputvaluesmatrix,inputmomentummatrix,inputvelocitymatrix,resultvaluesmatrix%29.md)
- [func encode(commandBuffer: any MTLCommandBuffer, inputGradientVector: MPSVector, inputValuesVector: MPSVector, inputMomentumVector: MPSVector, inputVelocityVector: MPSVector, maximumVelocityVector: MPSVector?, resultValuesVector: MPSVector)](./mpsnnoptimizeradam/encode%28commandbuffer,inputgradientvector,inputvaluesvector,inputmomentumvector,inputvelocityvector,maximumvelocityvector,resultvaluesvector%29.md)
- [func encode(commandBuffer: any MTLCommandBuffer, inputGradientVector: MPSVector, inputValuesVector: MPSVector, inputMomentumVector: MPSVector, inputVelocityVector: MPSVector, resultValuesVector: MPSVector)](./mpsnnoptimizeradam/encode%28commandbuffer,inputgradientvector,inputvaluesvector,inputmomentumvector,inputvelocityvector,resultvaluesvector%29.md)

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
- [class MPSNNOptimizerRMSProp](./mpsnnoptimizerrmsprop.md)
  An optimization layer that performs a root mean square propagation update.
- [class MPSNNOptimizerStochasticGradientDescent](./mpsnnoptimizerstochasticgradientdescent.md)
  An optimization layer that performs a gradient descent with an optional momentum update.
- [class MPSNNOptimizer](./mpsnnoptimizer.md)
  The base class for optimization layers.
- [class MPSNNOptimizerDescriptor](./mpsnnoptimizerdescriptor.md)
  An object that specifies properties used by an optimizer kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnoptimizeradam)*
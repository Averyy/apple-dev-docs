# MPSCNNBatchNormalization

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A batch normalization kernel.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNBatchNormalization
```

```objc
@interface MPSCNNBatchNormalization : MPSCNNKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](./mpscnnbatchnormalization/init%28coder,device%29.md)
- [convenience init(device: any MTLDevice, dataSource: any MPSCNNBatchNormalizationDataSource)](./mpscnnbatchnormalization/init%28device,datasource%29.md)
- [init(device: any MTLDevice, dataSource: any MPSCNNBatchNormalizationDataSource, fusedNeuronDescriptor: MPSNNNeuronDescriptor?)](./mpscnnbatchnormalization/init%28device,datasource,fusedneurondescriptor%29.md)
### Instance Properties
- [var dataSource: any MPSCNNBatchNormalizationDataSource](./mpscnnbatchnormalization/datasource.md)
- [var epsilon: Float](./mpscnnbatchnormalization/epsilon.md)
- [var numberOfFeatureChannels: Int](./mpscnnbatchnormalization/numberoffeaturechannels.md)
### Instance Methods
- [func encode(to: any MTLCommandBuffer, sourceImage: MPSImage, batchNormalizationState: MPSCNNBatchNormalizationState, destinationImage: MPSImage)](./mpscnnbatchnormalization/encode%28to,sourceimage,batchnormalizationstate,destinationimage%29.md)
- [func encodeBatch(to: any MTLCommandBuffer, sourceImages: [MPSImage], batchNormalizationState: MPSCNNBatchNormalizationState, destinationImages: [MPSImage])](./mpscnnbatchnormalization/encodebatch%28to,sourceimages,batchnormalizationstate,destinationimages%29.md)
- [func reloadDataSource(any MPSCNNBatchNormalizationDataSource)](./mpscnnbatchnormalization/reloaddatasource%28_%29.md)
- [func reloadGammaAndBeta(with: any MTLCommandBuffer, gammaAndBetaState: MPSCNNNormalizationGammaAndBetaState)](./mpscnnbatchnormalization/reloadgammaandbeta%28with,gammaandbetastate%29.md)
- [func reloadGammaAndBetaFromDataSource()](./mpscnnbatchnormalization/reloadgammaandbetafromdatasource%28%29.md)
- [func reloadMeanAndVariance(with: any MTLCommandBuffer, meanAndVarianceState: MPSCNNNormalizationMeanAndVarianceState)](./mpscnnbatchnormalization/reloadmeanandvariance%28with,meanandvariancestate%29.md)
- [func reloadMeanAndVarianceFromDataSource()](./mpscnnbatchnormalization/reloadmeanandvariancefromdatasource%28%29.md)
- [func resultState(sourceImage: MPSImage, sourceStates: [MPSState]?, destinationImage: MPSImage) -> MPSCNNBatchNormalizationState?](./mpscnnbatchnormalization/resultstate%28sourceimage,sourcestates,destinationimage%29.md)
- [func temporaryResultState(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, sourceStates: [MPSState]?, destinationImage: MPSImage) -> MPSCNNBatchNormalizationState?](./mpscnnbatchnormalization/temporaryresultstate%28commandbuffer,sourceimage,sourcestates,destinationimage%29.md)

## Relationships

### Inherits From
- [MPSCNNKernel](./mpscnnkernel.md)
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

### Normalization Layers
- [class MPSCNNCrossChannelNormalization](./mpscnncrosschannelnormalization.md)
  A normalization kernel applied across feature channels.
- [class MPSCNNCrossChannelNormalizationGradient](./mpscnncrosschannelnormalizationgradient.md)
  A gradient normalization kernel applied across feature channels.
- [class MPSCNNLocalContrastNormalization](./mpscnnlocalcontrastnormalization.md)
  A local-contrast normalization kernel.
- [class MPSCNNLocalContrastNormalizationGradient](./mpscnnlocalcontrastnormalizationgradient.md)
  A gradient local-contrast normalization kernel.
- [class MPSCNNSpatialNormalization](./mpscnnspatialnormalization.md)
  A spatial normalization kernel.
- [class MPSCNNSpatialNormalizationGradient](./mpscnnspatialnormalizationgradient.md)
  A gradient spatial normalization kernel.
- [class MPSCNNBatchNormalizationGradient](./mpscnnbatchnormalizationgradient.md)
  A gradient batch normalization kernel.
- [class MPSCNNBatchNormalizationState](./mpscnnbatchnormalizationstate.md)
  An object that stores data required to execute batch normalization.
- [class MPSCNNNormalizationMeanAndVarianceState](./mpscnnnormalizationmeanandvariancestate.md)
  An object that stores mean and variance terms used to execute batch normalization.
- [class MPSCNNBatchNormalizationStatistics](./mpscnnbatchnormalizationstatistics.md)
  An object that stores statistics required to execute batch normalization.
- [class MPSCNNBatchNormalizationStatisticsGradient](./mpscnnbatchnormalizationstatisticsgradient.md)
  An object that stores the gradient of the loss function with respect to the batch statistics and batch normalization weights.
- [class MPSCNNInstanceNormalization](./mpscnninstancenormalization.md)
  An instance normalization kernel.
- [class MPSCNNInstanceNormalizationGradient](./mpscnninstancenormalizationgradient.md)
  A gradient instance normalization kernel.
- [class MPSCNNInstanceNormalizationGradientState](./mpscnninstancenormalizationgradientstate.md)
  An object that stores information required to execute a gradient pass for instance normalization.
- [class MPSCNNNormalizationGammaAndBetaState](./mpscnnnormalizationgammaandbetastate.md)
  An object that stores gamma and beta terms used to apply a scale and bias in instance- or batch-normalization operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnbatchnormalization)*
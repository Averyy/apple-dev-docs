# MPSCNNInstanceNormalization

**Framework**: Metal Performance Shaders  
**Kind**: class

An instance normalization kernel.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNInstanceNormalization
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpscnninstancenormalization/init(coder:device:).md)
- [init(device: any MTLDevice, dataSource: any MPSCNNInstanceNormalizationDataSource)](mpscnninstancenormalization/init(device:datasource:).md)
### Instance Properties
- [var dataSource: any MPSCNNInstanceNormalizationDataSource](mpscnninstancenormalization/datasource.md)
- [var epsilon: Float](mpscnninstancenormalization/epsilon.md)
### Instance Methods
- [func reloadDataSource(any MPSCNNInstanceNormalizationDataSource)](mpscnninstancenormalization/reloaddatasource(_:).md)
- [func reloadGammaAndBeta(with: any MTLCommandBuffer, gammaAndBetaState: MPSCNNNormalizationGammaAndBetaState)](mpscnninstancenormalization/reloadgammaandbeta(with:gammaandbetastate:).md)
- [func reloadGammaAndBetaFromDataSource()](mpscnninstancenormalization/reloadgammaandbetafromdatasource.md)
- [func resultState(sourceImage: MPSImage, sourceStates: [MPSState]?, destinationImage: MPSImage) -> MPSCNNInstanceNormalizationGradientState?](mpscnninstancenormalization/resultstate(sourceimage:sourcestates:destinationimage:).md)
- [func temporaryResultState(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, sourceStates: [MPSState]?, destinationImage: MPSImage) -> MPSCNNInstanceNormalizationGradientState?](mpscnninstancenormalization/temporaryresultstate(commandbuffer:sourceimage:sourcestates:destinationimage:).md)

## Relationships

### Inherits From
- [MPSCNNKernel](mpscnnkernel.md)
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

- [class MPSCNNCrossChannelNormalization](mpscnncrosschannelnormalization.md)
  A normalization kernel applied across feature channels.
- [class MPSCNNCrossChannelNormalizationGradient](mpscnncrosschannelnormalizationgradient.md)
  A gradient normalization kernel applied across feature channels.
- [class MPSCNNLocalContrastNormalization](mpscnnlocalcontrastnormalization.md)
  A local-contrast normalization kernel.
- [class MPSCNNLocalContrastNormalizationGradient](mpscnnlocalcontrastnormalizationgradient.md)
  A gradient local-contrast normalization kernel.
- [class MPSCNNSpatialNormalization](mpscnnspatialnormalization.md)
  A spatial normalization kernel.
- [class MPSCNNSpatialNormalizationGradient](mpscnnspatialnormalizationgradient.md)
  A gradient spatial normalization kernel.
- [class MPSCNNBatchNormalization](mpscnnbatchnormalization.md)
  A batch normalization kernel.
- [class MPSCNNBatchNormalizationGradient](mpscnnbatchnormalizationgradient.md)
  A gradient batch normalization kernel.
- [class MPSCNNBatchNormalizationState](mpscnnbatchnormalizationstate.md)
  An object that stores data required to execute batch normalization.
- [class MPSCNNNormalizationMeanAndVarianceState](mpscnnnormalizationmeanandvariancestate.md)
  An object that stores mean and variance terms used to execute batch normalization.
- [class MPSCNNBatchNormalizationStatistics](mpscnnbatchnormalizationstatistics.md)
  An object that stores statistics required to execute batch normalization.
- [class MPSCNNBatchNormalizationStatisticsGradient](mpscnnbatchnormalizationstatisticsgradient.md)
  An object that stores the gradient of the loss function with respect to the batch statistics and batch normalization weights.
- [class MPSCNNInstanceNormalizationGradient](mpscnninstancenormalizationgradient.md)
  A gradient instance normalization kernel.
- [class MPSCNNInstanceNormalizationGradientState](mpscnninstancenormalizationgradientstate.md)
  An object that stores information required to execute a gradient pass for instance normalization.
- [class MPSCNNNormalizationGammaAndBetaState](mpscnnnormalizationgammaandbetastate.md)
  An object that stores gamma and beta terms used to apply a scale and bias in instance- or batch-normalization operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnninstancenormalization)*
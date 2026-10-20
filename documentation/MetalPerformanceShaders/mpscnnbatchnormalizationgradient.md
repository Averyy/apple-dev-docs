# MPSCNNBatchNormalizationGradient

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A gradient batch normalization kernel.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNBatchNormalizationGradient
```

```objc
@interface MPSCNNBatchNormalizationGradient : MPSCNNGradientKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](./mpscnnbatchnormalizationgradient/init%28coder,device%29.md)
- [init(device: any MTLDevice, fusedNeuronDescriptor: MPSNNNeuronDescriptor?)](./mpscnnbatchnormalizationgradient/init%28device,fusedneurondescriptor%29.md)
### Instance Methods
- [func encode(to: any MTLCommandBuffer, sourceGradient: MPSImage, sourceImage: MPSImage, batchNormalizationState: MPSCNNBatchNormalizationState) -> MPSImage](./mpscnnbatchnormalizationgradient/encode%28to,sourcegradient,sourceimage,batchnormalizationstate%29.md)
- [func encode(to: any MTLCommandBuffer, sourceGradient: MPSImage, sourceImage: MPSImage, batchNormalizationState: MPSCNNBatchNormalizationState, destinationGradient: MPSImage)](./mpscnnbatchnormalizationgradient/encode%28to,sourcegradient,sourceimage,batchnormalizationstate,destinationgradient%29.md)
- [func encodeBatch(to: any MTLCommandBuffer, sourceGradients: [MPSImage], sourceImages: [MPSImage], batchNormalizationState: MPSCNNBatchNormalizationState) -> [MPSImage]](./mpscnnbatchnormalizationgradient/encodebatch%28to,sourcegradients,sourceimages,batchnormalizationstate%29.md)
- [func encodeBatch(to: any MTLCommandBuffer, sourceGradients: [MPSImage], sourceImages: [MPSImage], batchNormalizationState: MPSCNNBatchNormalizationState, destinationGradients: [MPSImage])](./mpscnnbatchnormalizationgradient/encodebatch%28to,sourcegradients,sourceimages,batchnormalizationstate,destinationgradients%29.md)

## Relationships

### Inherits From
- [MPSCNNGradientKernel](./mpscnngradientkernel.md)
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
- [class MPSCNNBatchNormalization](./mpscnnbatchnormalization.md)
  A batch normalization kernel.
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

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnbatchnormalizationgradient)*
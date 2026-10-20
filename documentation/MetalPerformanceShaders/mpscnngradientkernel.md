# MPSCNNGradientKernel

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

The base class for gradient layers.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNGradientKernel
```

```objc
@interface MPSCNNGradientKernel : MPSCNNBinaryKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](./mpscnngradientkernel/init%28coder,device%29.md)
- [init(device: any MTLDevice)](./mpscnngradientkernel/init%28device%29.md)
### Instance Properties
- [var kernelOffsetX: Int](./mpscnngradientkernel/kerneloffsetx.md)
- [var kernelOffsetY: Int](./mpscnngradientkernel/kerneloffsety.md)
### Instance Methods
- [func encode(commandBuffer: any MTLCommandBuffer, sourceGradient: MPSImage, sourceImage: MPSImage, gradientState: MPSState) -> MPSImage](./mpscnngradientkernel/encode%28commandbuffer,sourcegradient,sourceimage,gradientstate%29.md)
- [func encode(commandBuffer: any MTLCommandBuffer, sourceGradient: MPSImage, sourceImage: MPSImage, gradientState: MPSState, destinationGradient: MPSImage)](./mpscnngradientkernel/encode%28commandbuffer,sourcegradient,sourceimage,gradientstate,destinationgradient%29.md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceGradients: [MPSImage], sourceImages: [MPSImage], gradientStates: [MPSState]) -> [MPSImage]](./mpscnngradientkernel/encodebatch%28commandbuffer,sourcegradients,sourceimages,gradientstates%29.md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceGradients: [MPSImage], sourceImages: [MPSImage], gradientStates: [MPSState], destinationGradients: [MPSImage])](./mpscnngradientkernel/encodebatch%28commandbuffer,sourcegradients,sourceimages,gradientstates,destinationgradients%29.md)

## Relationships

### Inherits From
- [MPSCNNBinaryKernel](./mpscnnbinarykernel.md)
### Inherited By
- [MPSCNNArithmeticGradient](./mpscnnarithmeticgradient.md)
- [MPSCNNBatchNormalizationGradient](./mpscnnbatchnormalizationgradient.md)
- [MPSCNNBatchNormalizationStatisticsGradient](./mpscnnbatchnormalizationstatisticsgradient.md)
- [MPSCNNConvolutionGradient](./mpscnnconvolutiongradient.md)
- [MPSCNNConvolutionTransposeGradient](./mpscnnconvolutiontransposegradient.md)
- [MPSCNNCrossChannelNormalizationGradient](./mpscnncrosschannelnormalizationgradient.md)
- [MPSCNNDropoutGradient](./mpscnndropoutgradient.md)
- [MPSCNNGroupNormalizationGradient](./mpscnngroupnormalizationgradient.md)
- [MPSCNNInstanceNormalizationGradient](./mpscnninstancenormalizationgradient.md)
- [MPSCNNLocalContrastNormalizationGradient](./mpscnnlocalcontrastnormalizationgradient.md)
- [MPSCNNLogSoftMaxGradient](./mpscnnlogsoftmaxgradient.md)
- [MPSCNNNeuronGradient](./mpscnnneurongradient.md)
- [MPSCNNPoolingGradient](./mpscnnpoolinggradient.md)
- [MPSCNNSoftMaxGradient](./mpscnnsoftmaxgradient.md)
- [MPSCNNSpatialNormalizationGradient](./mpscnnspatialnormalizationgradient.md)
- [MPSCNNUpsamplingGradient](./mpscnnupsamplinggradient.md)
- [MPSNNGramMatrixCalculationGradient](./mpsnngrammatrixcalculationgradient.md)
- [MPSNNPadGradient](./mpsnnpadgradient.md)
- [MPSNNReshapeGradient](./mpsnnreshapegradient.md)
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

### Layer Base Classes
- [class MPSCNNKernel](./mpscnnkernel.md)
  Base class for neural network layers.
- [class MPSCNNBinaryKernel](./mpscnnbinarykernel.md)
  A convolution neural network kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnngradientkernel)*
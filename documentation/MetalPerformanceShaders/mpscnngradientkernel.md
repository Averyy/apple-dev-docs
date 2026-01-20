# MPSCNNGradientKernel

**Framework**: Metal Performance Shaders  
**Kind**: class

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

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpscnngradientkernel/init(coder:device:).md)
- [init(device: any MTLDevice)](mpscnngradientkernel/init(device:).md)
### Instance Properties
- [var kernelOffsetX: Int](mpscnngradientkernel/kerneloffsetx.md)
- [var kernelOffsetY: Int](mpscnngradientkernel/kerneloffsety.md)
### Instance Methods
- [func encode(commandBuffer: any MTLCommandBuffer, sourceGradient: MPSImage, sourceImage: MPSImage, gradientState: MPSState) -> MPSImage](mpscnngradientkernel/encode(commandbuffer:sourcegradient:sourceimage:gradientstate:).md)
- [func encode(commandBuffer: any MTLCommandBuffer, sourceGradient: MPSImage, sourceImage: MPSImage, gradientState: MPSState, destinationGradient: MPSImage)](mpscnngradientkernel/encode(commandbuffer:sourcegradient:sourceimage:gradientstate:destinationgradient:).md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceGradients: [MPSImage], sourceImages: [MPSImage], gradientStates: [MPSState]) -> [MPSImage]](mpscnngradientkernel/encodebatch(commandbuffer:sourcegradients:sourceimages:gradientstates:).md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceGradients: [MPSImage], sourceImages: [MPSImage], gradientStates: [MPSState], destinationGradients: [MPSImage])](mpscnngradientkernel/encodebatch(commandbuffer:sourcegradients:sourceimages:gradientstates:destinationgradients:).md)

## Relationships

### Inherits From
- [MPSCNNBinaryKernel](mpscnnbinarykernel.md)
### Inherited By
- [MPSCNNArithmeticGradient](mpscnnarithmeticgradient.md)
- [MPSCNNBatchNormalizationGradient](mpscnnbatchnormalizationgradient.md)
- [MPSCNNBatchNormalizationStatisticsGradient](mpscnnbatchnormalizationstatisticsgradient.md)
- [MPSCNNConvolutionGradient](mpscnnconvolutiongradient.md)
- [MPSCNNConvolutionTransposeGradient](mpscnnconvolutiontransposegradient.md)
- [MPSCNNCrossChannelNormalizationGradient](mpscnncrosschannelnormalizationgradient.md)
- [MPSCNNDropoutGradient](mpscnndropoutgradient.md)
- [MPSCNNGroupNormalizationGradient](mpscnngroupnormalizationgradient.md)
- [MPSCNNInstanceNormalizationGradient](mpscnninstancenormalizationgradient.md)
- [MPSCNNLocalContrastNormalizationGradient](mpscnnlocalcontrastnormalizationgradient.md)
- [MPSCNNLogSoftMaxGradient](mpscnnlogsoftmaxgradient.md)
- [MPSCNNNeuronGradient](mpscnnneurongradient.md)
- [MPSCNNPoolingGradient](mpscnnpoolinggradient.md)
- [MPSCNNSoftMaxGradient](mpscnnsoftmaxgradient.md)
- [MPSCNNSpatialNormalizationGradient](mpscnnspatialnormalizationgradient.md)
- [MPSCNNUpsamplingGradient](mpscnnupsamplinggradient.md)
- [MPSNNGramMatrixCalculationGradient](mpsnngrammatrixcalculationgradient.md)
- [MPSNNPadGradient](mpsnnpadgradient.md)
- [MPSNNReshapeGradient](mpsnnreshapegradient.md)
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

- [class MPSCNNKernel](mpscnnkernel.md)
  Base class for neural network layers.
- [class MPSCNNBinaryKernel](mpscnnbinarykernel.md)
  A convolution neural network kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnngradientkernel)*
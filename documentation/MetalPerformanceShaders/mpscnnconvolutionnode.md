# MPSCNNConvolutionNode

**Framework**: Metal Performance Shaders  
**Kind**: class

A representation of a convolution kernel.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNConvolutionNode
```

## Topics

### Initializers
- [init(source: MPSNNImageNode, weights: any MPSCNNConvolutionDataSource)](mpscnnconvolutionnode/init(source:weights:).md)
- [protocol MPSCNNConvolutionDataSource](mpscnnconvolutiondatasource.md)
  The protocol that provides convolution filter weights and bias terms.
### Instance Properties
- [var accumulatorPrecision: MPSNNConvolutionAccumulatorPrecisionOption](mpscnnconvolutionnode/accumulatorprecision.md)
- [var convolutionGradientState: MPSCNNConvolutionGradientStateNode?](mpscnnconvolutionnode/convolutiongradientstate.md)
- [var trainingStyle: MPSNNTrainingStyle](mpscnnconvolutionnode/trainingstyle.md)

## Relationships

### Inherits From
- [MPSNNFilterNode](mpsnnfilternode.md)
### Inherited By
- [MPSCNNBinaryConvolutionNode](mpscnnbinaryconvolutionnode.md)
- [MPSCNNConvolutionTransposeNode](mpscnnconvolutiontransposenode.md)
- [MPSCNNFullyConnectedNode](mpscnnfullyconnectednode.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [MPSNNTrainableNode](mpsnntrainablenode.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MPSCNNBinaryConvolutionNode](mpscnnbinaryconvolutionnode.md)
  A representation of a convolution kernel with binary weights and an input image using binary approximations.
- [class MPSCNNConvolutionTransposeNode](mpscnnconvolutiontransposenode.md)
  A representation of a transposed convolution.
- [class MPSCNNConvolutionGradientNode](mpscnnconvolutiongradientnode.md)
  A representation of a gradient convolution kernel.
- [class MPSCNNConvolutionGradientStateNode](mpscnnconvolutiongradientstatenode.md)
  A representation of a gradient convolution state.
- [class MPSCNNCrossChannelNormalizationGradientNode](mpscnncrosschannelnormalizationgradientnode.md)
  A representation of a gradient normalization kernel applied across feature channels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutionnode)*
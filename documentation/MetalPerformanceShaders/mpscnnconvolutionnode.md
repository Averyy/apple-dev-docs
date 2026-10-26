# MPSCNNConvolutionNode

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

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

```objc
@interface MPSCNNConvolutionNode : MPSNNFilterNode
```

## Topics

### Initializers
- [init(source: MPSNNImageNode, weights: any MPSCNNConvolutionDataSource)](./mpscnnconvolutionnode/init%28source,weights%29.md)
- [protocol MPSCNNConvolutionDataSource](./mpscnnconvolutiondatasource.md)
  The protocol that provides convolution filter weights and bias terms.
### Instance Properties
- [var accumulatorPrecision: MPSNNConvolutionAccumulatorPrecisionOption](./mpscnnconvolutionnode/accumulatorprecision.md)
- [var convolutionGradientState: MPSCNNConvolutionGradientStateNode?](./mpscnnconvolutionnode/convolutiongradientstate.md)
- [var trainingStyle: MPSNNTrainingStyle](./mpscnnconvolutionnode/trainingstyle.md)
### Type Methods
- [+ nodeWithSource:weights:](./mpscnnconvolutionnode/nodewithsource_weights_.md)

## Relationships

### Inherits From
- [MPSNNFilterNode](./mpsnnfilternode.md)
### Inherited By
- [MPSCNNBinaryConvolutionNode](./mpscnnbinaryconvolutionnode.md)
- [MPSCNNConvolutionTransposeNode](./mpscnnconvolutiontransposenode.md)
- [MPSCNNFullyConnectedNode](./mpscnnfullyconnectednode.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [MPSNNTrainableNode](./mpsnntrainablenode.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Convolution Layer Nodes
- [class MPSCNNBinaryConvolutionNode](./mpscnnbinaryconvolutionnode.md)
  A representation of a convolution kernel with binary weights and an input image using binary approximations.
- [class MPSCNNConvolutionTransposeNode](./mpscnnconvolutiontransposenode.md)
  A representation of a transposed convolution.
- [class MPSCNNConvolutionGradientNode](./mpscnnconvolutiongradientnode.md)
  A representation of a gradient convolution kernel.
- [class MPSCNNConvolutionGradientStateNode](./mpscnnconvolutiongradientstatenode.md)
  A representation of a gradient convolution state.
- [class MPSCNNCrossChannelNormalizationGradientNode](./mpscnncrosschannelnormalizationgradientnode.md)
  A representation of a gradient normalization kernel applied across feature channels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutionnode)*
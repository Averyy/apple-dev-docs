# MPSCNNConvolutionTransposeNode

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A representation of a transposed convolution.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNConvolutionTransposeNode
```

```objc
@interface MPSCNNConvolutionTransposeNode : MPSCNNConvolutionNode
```

## Topics

### Initializers
- [protocol MPSCNNConvolutionDataSource](./mpscnnconvolutiondatasource.md)
  The protocol that provides convolution filter weights and bias terms.
- [init(source: MPSNNImageNode, convolutionGradientState: MPSCNNConvolutionGradientStateNode?, weights: any MPSCNNConvolutionDataSource)](./mpscnnconvolutiontransposenode/init%28source,convolutiongradientstate,weights%29.md)
### Type Methods
- [+ nodeWithSource:convolutionGradientState:weights:](./mpscnnconvolutiontransposenode/nodewithsource_convolutiongradientstate_weights_.md)

## Relationships

### Inherits From
- [MPSCNNConvolutionNode](./mpscnnconvolutionnode.md)
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
- [class MPSCNNConvolutionNode](./mpscnnconvolutionnode.md)
  A representation of a convolution kernel.
- [class MPSCNNConvolutionGradientNode](./mpscnnconvolutiongradientnode.md)
  A representation of a gradient convolution kernel.
- [class MPSCNNConvolutionGradientStateNode](./mpscnnconvolutiongradientstatenode.md)
  A representation of a gradient convolution state.
- [class MPSCNNCrossChannelNormalizationGradientNode](./mpscnncrosschannelnormalizationgradientnode.md)
  A representation of a gradient normalization kernel applied across feature channels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutiontransposenode)*
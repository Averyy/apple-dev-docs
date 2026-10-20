# MPSCNNCrossChannelNormalizationGradientNode

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A representation of a gradient normalization kernel applied across feature channels.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNCrossChannelNormalizationGradientNode
```

```objc
@interface MPSCNNCrossChannelNormalizationGradientNode : MPSNNGradientFilterNode
```

## Topics

### Initializers
- [init(sourceGradient: MPSNNImageNode, sourceImage: MPSNNImageNode, gradientState: MPSNNGradientStateNode, kernelSize: Int)](./mpscnncrosschannelnormalizationgradientnode/init%28sourcegradient,sourceimage,gradientstate,kernelsize%29.md)
### Instance Properties
- [var kernelSize: Int](./mpscnncrosschannelnormalizationgradientnode/kernelsize.md)

## Relationships

### Inherits From
- [MPSNNGradientFilterNode](./mpsnngradientfilternode.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Convolution Layer Nodes
- [class MPSCNNBinaryConvolutionNode](./mpscnnbinaryconvolutionnode.md)
  A representation of a convolution kernel with binary weights and an input image using binary approximations.
- [class MPSCNNConvolutionNode](./mpscnnconvolutionnode.md)
  A representation of a convolution kernel.
- [class MPSCNNConvolutionTransposeNode](./mpscnnconvolutiontransposenode.md)
  A representation of a transposed convolution.
- [class MPSCNNConvolutionGradientNode](./mpscnnconvolutiongradientnode.md)
  A representation of a gradient convolution kernel.
- [class MPSCNNConvolutionGradientStateNode](./mpscnnconvolutiongradientstatenode.md)
  A representation of a gradient convolution state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnncrosschannelnormalizationgradientnode)*
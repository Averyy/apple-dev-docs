# MPSCNNConvolutionGradientState

**Framework**: Metal Performance Shaders  
**Kind**: class

An object that exposes a gradient convolution kernel’s gradient with respect to weights and biases.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNConvolutionGradientState
```

## Topics

### Instance Properties
- [var convolution: MPSCNNConvolution](mpscnnconvolutiongradientstate/convolution.md)
- [var gradientForBiases: any MTLBuffer](mpscnnconvolutiongradientstate/gradientforbiases.md)
- [var gradientForWeights: any MTLBuffer](mpscnnconvolutiongradientstate/gradientforweights.md)
- [var gradientForWeightsLayout: MPSCNNConvolutionWeightsLayout](mpscnnconvolutiongradientstate/gradientforweightslayout.md)

## Relationships

### Inherits From
- [MPSNNGradientState](mpsnngradientstate.md)
### Inherited By
- [MPSCNNConvolutionTransposeGradientState](mpscnnconvolutiontransposegradientstate.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [MPSImageSizeEncodingState](mpsimagesizeencodingstate.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MPSCNNBinaryConvolution](mpscnnbinaryconvolution.md)
  A convolution kernel with binary weights and an input image using binary approximations.
- [class MPSCNNConvolution](mpscnnconvolution.md)
  A convolution kernel that convolves the input image with a set of filters, with each producing one feature map in the output image.
- [class MPSCNNDepthWiseConvolutionDescriptor](mpscnndepthwiseconvolutiondescriptor.md)
  A description of a convolution object that does depthwise convolution.
- [class MPSCNNSubPixelConvolutionDescriptor](mpscnnsubpixelconvolutiondescriptor.md)
  A description of a convolution object that does subpixel upsampling and reshaping.
- [class MPSCNNConvolutionTranspose](mpscnnconvolutiontranspose.md)
  A transposed convolution kernel.
- [class MPSCNNConvolutionGradient](mpscnnconvolutiongradient.md)
  A gradient convolution kernel.
- [protocol MPSImageSizeEncodingState](mpsimagesizeencodingstate.md)
  A protocol for objects that contain information about an image size elsewhere in the graph.
- [class MPSCNNConvolutionWeightsAndBiasesState](mpscnnconvolutionweightsandbiasesstate.md)
  A class that stores weights and biases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutiongradientstate)*
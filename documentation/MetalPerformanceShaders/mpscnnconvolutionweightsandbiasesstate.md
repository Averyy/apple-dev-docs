# MPSCNNConvolutionWeightsAndBiasesState

**Framework**: Metal Performance Shaders  
**Kind**: class

A class that stores weights and biases.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNConvolutionWeightsAndBiasesState
```

## Topics

### Initializers
- [init(device: any MTLDevice, cnnConvolutionDescriptor: MPSCNNConvolutionDescriptor)](mpscnnconvolutionweightsandbiasesstate/init(device:cnnconvolutiondescriptor:).md)
- [init(weights: any MTLBuffer, biases: (any MTLBuffer)?)](mpscnnconvolutionweightsandbiasesstate/init(weights:biases:).md)
- [init(weights: any MTLBuffer, weightsOffset: Int, biases: (any MTLBuffer)?, biasesOffset: Int, cnnConvolutionDescriptor: MPSCNNConvolutionDescriptor)](mpscnnconvolutionweightsandbiasesstate/init(weights:weightsoffset:biases:biasesoffset:cnnconvolutiondescriptor:).md)
### Instance Properties
- [var biases: (any MTLBuffer)?](mpscnnconvolutionweightsandbiasesstate/biases.md)
- [var biasesOffset: Int](mpscnnconvolutionweightsandbiasesstate/biasesoffset.md)
- [var weights: any MTLBuffer](mpscnnconvolutionweightsandbiasesstate/weights.md)
- [var weightsOffset: Int](mpscnnconvolutionweightsandbiasesstate/weightsoffset.md)
### Type Methods
- [class func temporaryCNNConvolutionWeightsAndBiasesState(with: any MTLCommandBuffer, cnnConvolutionDescriptor: MPSCNNConvolutionDescriptor) -> Self](mpscnnconvolutionweightsandbiasesstate/temporarycnnconvolutionweightsandbiasesstate(with:cnnconvolutiondescriptor:).md)

## Relationships

### Inherits From
- [MPSState](mpsstate.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
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
- [class MPSCNNConvolutionGradientState](mpscnnconvolutiongradientstate.md)
  An object that exposes a gradient convolution kernel’s gradient with respect to weights and biases.
- [protocol MPSImageSizeEncodingState](mpsimagesizeencodingstate.md)
  A protocol for objects that contain information about an image size elsewhere in the graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutionweightsandbiasesstate)*
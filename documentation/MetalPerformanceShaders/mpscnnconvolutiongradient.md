# MPSCNNConvolutionGradient

**Framework**: Metal Performance Shaders  
**Kind**: class

A gradient convolution kernel.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNConvolutionGradient
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpscnnconvolutiongradient/init(coder:device:).md)
- [init(device: any MTLDevice, weights: any MPSCNNConvolutionDataSource)](mpscnnconvolutiongradient/init(device:weights:).md)
### Instance Properties
- [var channelMultiplier: Int](mpscnnconvolutiongradient/channelmultiplier.md)
- [var dataSource: any MPSCNNConvolutionDataSource](mpscnnconvolutiongradient/datasource.md)
- [var gradientOption: MPSCNNConvolutionGradientOption](mpscnnconvolutiongradient/gradientoption.md)
- [var groups: Int](mpscnnconvolutiongradient/groups.md)
- [var serializeWeightsAndBiases: Bool](mpscnnconvolutiongradient/serializeweightsandbiases.md)
- [var sourceGradientFeatureChannels: Int](mpscnnconvolutiongradient/sourcegradientfeaturechannels.md)
- [var sourceImageFeatureChannels: Int](mpscnnconvolutiongradient/sourceimagefeaturechannels.md)
### Instance Methods
- [func reloadWeightsAndBiases(with: any MTLCommandBuffer, state: MPSCNNConvolutionWeightsAndBiasesState)](mpscnnconvolutiongradient/reloadweightsandbiases(with:state:).md)
- [func reloadWeightsAndBiasesFromDataSource()](mpscnnconvolutiongradient/reloadweightsandbiasesfromdatasource.md)

## Relationships

### Inherits From
- [MPSCNNGradientKernel](mpscnngradientkernel.md)
### Inherited By
- [MPSCNNFullyConnectedGradient](mpscnnfullyconnectedgradient.md)
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
- [class MPSCNNConvolutionGradientState](mpscnnconvolutiongradientstate.md)
  An object that exposes a gradient convolution kernel’s gradient with respect to weights and biases.
- [protocol MPSImageSizeEncodingState](mpsimagesizeencodingstate.md)
  A protocol for objects that contain information about an image size elsewhere in the graph.
- [class MPSCNNConvolutionWeightsAndBiasesState](mpscnnconvolutionweightsandbiasesstate.md)
  A class that stores weights and biases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutiongradient)*
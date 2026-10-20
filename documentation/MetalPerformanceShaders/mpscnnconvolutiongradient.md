# MPSCNNConvolutionGradient

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

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

```objc
@interface MPSCNNConvolutionGradient : MPSCNNGradientKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](./mpscnnconvolutiongradient/init%28coder,device%29.md)
- [init(device: any MTLDevice, weights: any MPSCNNConvolutionDataSource)](./mpscnnconvolutiongradient/init%28device,weights%29.md)
### Instance Properties
- [var channelMultiplier: Int](./mpscnnconvolutiongradient/channelmultiplier.md)
- [var dataSource: any MPSCNNConvolutionDataSource](./mpscnnconvolutiongradient/datasource.md)
- [var gradientOption: MPSCNNConvolutionGradientOption](./mpscnnconvolutiongradient/gradientoption.md)
- [var groups: Int](./mpscnnconvolutiongradient/groups.md)
- [var serializeWeightsAndBiases: Bool](./mpscnnconvolutiongradient/serializeweightsandbiases.md)
- [var sourceGradientFeatureChannels: Int](./mpscnnconvolutiongradient/sourcegradientfeaturechannels.md)
- [var sourceImageFeatureChannels: Int](./mpscnnconvolutiongradient/sourceimagefeaturechannels.md)
### Instance Methods
- [func reloadWeightsAndBiases(with: any MTLCommandBuffer, state: MPSCNNConvolutionWeightsAndBiasesState)](./mpscnnconvolutiongradient/reloadweightsandbiases%28with,state%29.md)
- [func reloadWeightsAndBiasesFromDataSource()](./mpscnnconvolutiongradient/reloadweightsandbiasesfromdatasource%28%29.md)

## Relationships

### Inherits From
- [MPSCNNGradientKernel](./mpscnngradientkernel.md)
### Inherited By
- [MPSCNNFullyConnectedGradient](./mpscnnfullyconnectedgradient.md)
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

### Convolution Layers
- [class MPSCNNBinaryConvolution](./mpscnnbinaryconvolution.md)
  A convolution kernel with binary weights and an input image using binary approximations.
- [class MPSCNNConvolution](./mpscnnconvolution.md)
  A convolution kernel that convolves the input image with a set of filters, with each producing one feature map in the output image.
- [class MPSCNNDepthWiseConvolutionDescriptor](./mpscnndepthwiseconvolutiondescriptor.md)
  A description of a convolution object that does depthwise convolution.
- [class MPSCNNSubPixelConvolutionDescriptor](./mpscnnsubpixelconvolutiondescriptor.md)
  A description of a convolution object that does subpixel upsampling and reshaping.
- [class MPSCNNConvolutionTranspose](./mpscnnconvolutiontranspose.md)
  A transposed convolution kernel.
- [class MPSCNNConvolutionGradientState](./mpscnnconvolutiongradientstate.md)
  An object that exposes a gradient convolution kernel’s gradient with respect to weights and biases.
- [protocol MPSImageSizeEncodingState](./mpsimagesizeencodingstate.md)
  A protocol for objects that contain information about an image size elsewhere in the graph.
- [class MPSCNNConvolutionWeightsAndBiasesState](./mpscnnconvolutionweightsandbiasesstate.md)
  A class that stores weights and biases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutiongradient)*
# MPSCNNConvolutionTranspose

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A transposed convolution kernel.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNConvolutionTranspose
```

```objc
@interface MPSCNNConvolutionTranspose : MPSCNNKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](./mpscnnconvolutiontranspose/init%28coder,device%29.md)
  Initializes a transposed convolution kernel.
- [init(device: any MTLDevice, weights: any MPSCNNConvolutionDataSource)](./mpscnnconvolutiontranspose/init%28device,weights%29.md)
  Initializes a transposed convolution kernel.
- [protocol MPSCNNConvolutionDataSource](./mpscnnconvolutiondatasource.md)
  The protocol that provides convolution filter weights and bias terms.
### Instance Properties
- [var groups: Int](./mpscnnconvolutiontranspose/groups.md)
- [var inputFeatureChannels: Int](./mpscnnconvolutiontranspose/inputfeaturechannels.md)
- [var kernelOffsetX: Int](./mpscnnconvolutiontranspose/kerneloffsetx.md)
- [var kernelOffsetY: Int](./mpscnnconvolutiontranspose/kerneloffsety.md)
- [var outputFeatureChannels: Int](./mpscnnconvolutiontranspose/outputfeaturechannels.md)
- [var accumulatorPrecisionOption: MPSNNConvolutionAccumulatorPrecisionOption](./mpscnnconvolutiontranspose/accumulatorprecisionoption.md)
- [var dataSource: any MPSCNNConvolutionDataSource](./mpscnnconvolutiontranspose/datasource.md)
### Instance Methods
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, convolutionGradientState: MPSCNNConvolutionGradientState?) -> MPSImage](./mpscnnconvolutiontranspose/encode%28commandbuffer,sourceimage,convolutiongradientstate%29.md)
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, convolutionGradientState: MPSCNNConvolutionGradientState?, destinationImage: MPSImage)](./mpscnnconvolutiontranspose/encode%28commandbuffer,sourceimage,convolutiongradientstate,destinationimage%29.md)
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, convolutionGradientState: MPSCNNConvolutionGradientState?, destinationState: AutoreleasingUnsafeMutablePointer<MPSCNNConvolutionTransposeGradientState?>, destinationStateIsTemporary: Bool) -> MPSImage](./mpscnnconvolutiontranspose/encode%28commandbuffer,sourceimage,convolutiongradientstate,destinationstate,destinationstateistemporary%29.md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], convolutionGradientStates: [MPSCNNConvolutionGradientState]?) -> [MPSImage]](./mpscnnconvolutiontranspose/encodebatch%28commandbuffer,sourceimages,convolutiongradientstates%29.md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], convolutionGradientStates: [MPSCNNConvolutionGradientState]?, destinationImages: [MPSImage])](./mpscnnconvolutiontranspose/encodebatch%28commandbuffer,sourceimages,convolutiongradientstates,destinationimages%29.md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], convolutionGradientStates: [MPSCNNConvolutionGradientState]?, destinationStates: AutoreleasingUnsafeMutablePointer<NSArray?>, destinationStateIsTemporary: Bool) -> [MPSImage]](./mpscnnconvolutiontranspose/encodebatch%28commandbuffer,sourceimages,convolutiongradientstates,destinationstates,destinationstateistemporary%29.md)
- [func exportWeightsAndBiases(with: any MTLCommandBuffer, resultStateCanBeTemporary: Bool) -> MPSCNNConvolutionWeightsAndBiasesState](./mpscnnconvolutiontranspose/exportweightsandbiases%28with,resultstatecanbetemporary%29.md)
- [func reloadWeightsAndBiases(with: any MTLCommandBuffer, state: MPSCNNConvolutionWeightsAndBiasesState)](./mpscnnconvolutiontranspose/reloadweightsandbiases%28with,state%29.md)
- [func reloadWeightsAndBiasesFromDataSource()](./mpscnnconvolutiontranspose/reloadweightsandbiasesfromdatasource%28%29.md)
- [func resultState(sourceImage: MPSImage, sourceStates: [MPSCNNConvolutionGradientState]?, destinationImage: MPSImage) -> MPSCNNConvolutionTransposeGradientState?](./mpscnnconvolutiontranspose/resultstate%28sourceimage,sourcestates,destinationimage%29.md)
- [func resultStateBatch(sourceImage: [MPSImage], sourceStates: [[MPSCNNConvolutionGradientState]]?, destinationImage: [MPSImage]) -> [MPSCNNConvolutionTransposeGradientState]?](./mpscnnconvolutiontranspose/resultstatebatch%28sourceimage,sourcestates,destinationimage%29.md)
- [func temporaryResultState(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, sourceStates: [MPSCNNConvolutionGradientState]?, destinationImage: MPSImage) -> MPSCNNConvolutionTransposeGradientState?](./mpscnnconvolutiontranspose/temporaryresultstate%28commandbuffer,sourceimage,sourcestates,destinationimage%29.md)
- [func temporaryResultStateBatch(commandBuffer: any MTLCommandBuffer, sourceImage: [MPSImage], sourceStates: [[MPSCNNConvolutionGradientState]]?, destinationImage: [MPSImage]) -> [MPSCNNConvolutionTransposeGradientState]?](./mpscnnconvolutiontranspose/temporaryresultstatebatch%28commandbuffer,sourceimage,sourcestates,destinationimage%29.md)

## Relationships

### Inherits From
- [MPSCNNKernel](./mpscnnkernel.md)
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
- [class MPSCNNConvolutionGradient](./mpscnnconvolutiongradient.md)
  A gradient convolution kernel.
- [class MPSCNNConvolutionGradientState](./mpscnnconvolutiongradientstate.md)
  An object that exposes a gradient convolution kernel’s gradient with respect to weights and biases.
- [protocol MPSImageSizeEncodingState](./mpsimagesizeencodingstate.md)
  A protocol for objects that contain information about an image size elsewhere in the graph.
- [class MPSCNNConvolutionWeightsAndBiasesState](./mpscnnconvolutionweightsandbiasesstate.md)
  A class that stores weights and biases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutiontranspose)*
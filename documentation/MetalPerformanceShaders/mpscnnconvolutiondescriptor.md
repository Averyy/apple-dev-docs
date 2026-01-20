# MPSCNNConvolutionDescriptor

**Framework**: Metal Performance Shaders  
**Kind**: class

A description of the attributes of a convolution kernel.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNConvolutionDescriptor
```

#### Overview

You use an [`MPSCNNConvolutionDescriptor`](mpscnnconvolutiondescriptor.md) object to describe the properties of an [`MPSCNNConvolution`](mpscnnconvolution.md) kernel such as its size, pixel format and CPU cache mode.

## Topics

### Type Methods
- [init?(coder: NSCoder)](mpscnnconvolutiondescriptor/init(coder:).md)
- [convenience init(kernelWidth: Int, kernelHeight: Int, inputFeatureChannels: Int, outputFeatureChannels: Int)](mpscnnconvolutiondescriptor/init(kernelwidth:kernelheight:inputfeaturechannels:outputfeaturechannels:).md)
- [convenience init(kernelWidth: Int, kernelHeight: Int, inputFeatureChannels: Int, outputFeatureChannels: Int, neuronFilter: MPSCNNNeuron?)](mpscnnconvolutiondescriptor/init(kernelwidth:kernelheight:inputfeaturechannels:outputfeaturechannels:neuronfilter:).md)
  Creates a convolution descriptor with an optional neuron filter.
### Instance Properties
- [var groups: Int](mpscnnconvolutiondescriptor/groups.md)
  The number of groups that the input and output channels are divided into.
- [var inputFeatureChannels: Int](mpscnnconvolutiondescriptor/inputfeaturechannels.md)
  The number of feature channels per pixel in the input image.
- [var kernelHeight: Int](mpscnnconvolutiondescriptor/kernelheight.md)
  The height of the kernel window.
- [var kernelWidth: Int](mpscnnconvolutiondescriptor/kernelwidth.md)
  The width of the kernel window.
- [var outputFeatureChannels: Int](mpscnnconvolutiondescriptor/outputfeaturechannels.md)
  The number of feature channels per pixel in the output image.
- [var strideInPixelsX: Int](mpscnnconvolutiondescriptor/strideinpixelsx.md)
  The output stride (downsampling factor) in the x dimension.
- [var strideInPixelsY: Int](mpscnnconvolutiondescriptor/strideinpixelsy.md)
  The output stride (downsampling factor) in the y dimension.
- [var neuron: MPSCNNNeuron?](mpscnnconvolutiondescriptor/neuron.md)
  The neuron filter to be applied as part of the convolution operation.
- [var dilationRateX: Int](mpscnnconvolutiondescriptor/dilationratex.md)
- [var dilationRateY: Int](mpscnnconvolutiondescriptor/dilationratey.md)
- [func neuronParameterA() -> Float](mpscnnconvolutiondescriptor/neuronparametera.md)
- [func neuronParameterB() -> Float](mpscnnconvolutiondescriptor/neuronparameterb.md)
- [func neuronType() -> MPSCNNNeuronType](mpscnnconvolutiondescriptor/neurontype.md)
- [var fusedNeuronDescriptor: MPSNNNeuronDescriptor](mpscnnconvolutiondescriptor/fusedneurondescriptor.md)
### Instance Methods
- [func encode(with: NSCoder)](mpscnnconvolutiondescriptor/encode(with:).md)
- [func setBatchNormalizationParametersForInferenceWithMean(UnsafePointer<Float>?, variance: UnsafePointer<Float>?, gamma: UnsafePointer<Float>?, beta: UnsafePointer<Float>?, epsilon: Float)](mpscnnconvolutiondescriptor/setbatchnormalizationparametersforinferencewithmean(_:variance:gamma:beta:epsilon:).md)
- [func setNeuronToPReLUWithParametersA(Data)](mpscnnconvolutiondescriptor/setneurontopreluwithparametersa(_:).md)
- [func setNeuronType(MPSCNNNeuronType, parameterA: Float, parameterB: Float)](mpscnnconvolutiondescriptor/setneurontype(_:parametera:parameterb:).md)
### Type Properties
- [class var supportsSecureCoding: Bool](mpscnnconvolutiondescriptor/supportssecurecoding.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [MPSCNNDepthWiseConvolutionDescriptor](mpscnndepthwiseconvolutiondescriptor.md)
- [MPSCNNSubPixelConvolutionDescriptor](mpscnnsubpixelconvolutiondescriptor.md)
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

- [init?(coder: NSCoder, device: any MTLDevice)](mpscnnconvolution/init(coder:device:).md)
- [init(device: any MTLDevice, convolutionDescriptor: MPSCNNConvolutionDescriptor, kernelWeights: UnsafePointer<Float>, biasTerms: UnsafePointer<Float>?, flags: MPSCNNConvolutionFlags)](mpscnnconvolution/init(device:convolutiondescriptor:kernelweights:biasterms:flags:).md)
  Initializes a convolution kernel.
- [enum MPSCNNConvolutionFlags](mpscnnconvolutionflags.md)
  Options used to control how kernel weights are stored and used in the CNN kernels
- [init(device: any MTLDevice, weights: any MPSCNNConvolutionDataSource)](mpscnnconvolution/init(device:weights:).md)
- [protocol MPSCNNConvolutionDataSource](mpscnnconvolutiondatasource.md)
  The protocol that provides convolution filter weights and bias terms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutiondescriptor)*
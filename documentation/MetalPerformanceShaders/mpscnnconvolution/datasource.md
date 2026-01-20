# dataSource

**Framework**: Metal Performance Shaders  
**Kind**: property

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var dataSource: any MPSCNNConvolutionDataSource { get }
```

## See Also

- [var inputFeatureChannels: Int](mpscnnconvolution/inputfeaturechannels.md)
  The number of feature channels per pixel in the input image.
- [var outputFeatureChannels: Int](mpscnnconvolution/outputfeaturechannels.md)
  The number of feature channels per pixel in the output image.
- [var groups: Int](mpscnnconvolution/groups.md)
  The number of groups that the input and output channels are divided into.
- [var subPixelScaleFactor: Int](mpscnnconvolution/subpixelscalefactor.md)
- [var neuron: MPSCNNNeuron?](mpscnnconvolution/neuron.md)
  The neuron filter to be applied as part of the convolution operation.
- [class MPSCNNNeuron](mpscnnneuron.md)
  A filter that applies a neuron activation function.
- [var neuronType: MPSCNNNeuronType](mpscnnconvolution/neurontype.md)
- [enum MPSCNNNeuronType](mpscnnneurontype.md)
  The types of neuron filter to append to a convolution.
- [var neuronParameterA: Float](mpscnnconvolution/neuronparametera.md)
- [var neuronParameterB: Float](mpscnnconvolution/neuronparameterb.md)
- [var accumulatorPrecisionOption: MPSNNConvolutionAccumulatorPrecisionOption](mpscnnconvolution/accumulatorprecisionoption.md)
- [var channelMultiplier: Int](mpscnnconvolution/channelmultiplier.md)
- [var fusedNeuronDescriptor: MPSNNNeuronDescriptor?](mpscnnconvolution/fusedneurondescriptor.md)
- [var neuronParameterC: Float](mpscnnconvolution/neuronparameterc.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolution/datasource)*
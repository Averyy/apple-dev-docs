# neuron

**Framework**: Metal Performance Shaders  
**Kind**: property  
**Role**: Instance Property

The neuron filter to be applied as part of the convolution operation.

**Availability**:
- iOS 10.0+ - Deprecated in 11.0
- iPadOS 10.0+ - Deprecated in 11.0
- Mac Catalyst 10.0+ - Deprecated in 11.0
- macOS 10.13+
- tvOS 10.0+ - Deprecated in 11.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
var neuron: MPSCNNNeuron? { get }
```

```objc
@property (nonatomic, readonly) const MPSCNNNeuron * neuron;
```

## See Also

### Instance Properties
- [var inputFeatureChannels: Int](./inputfeaturechannels.md)
  The number of feature channels per pixel in the input image.
- [var outputFeatureChannels: Int](./outputfeaturechannels.md)
  The number of feature channels per pixel in the output image.
- [var groups: Int](./groups.md)
  The number of groups that the input and output channels are divided into.
- [var subPixelScaleFactor: Int](./subpixelscalefactor.md)
- [class MPSCNNNeuron](../mpscnnneuron.md)
  A filter that applies a neuron activation function.
- [var neuronType: MPSCNNNeuronType](./neurontype.md)
- [enum MPSCNNNeuronType](../mpscnnneurontype.md)
  The types of neuron filter to append to a convolution.
- [var neuronParameterA: Float](./neuronparametera.md)
- [var neuronParameterB: Float](./neuronparameterb.md)
- [var accumulatorPrecisionOption: MPSNNConvolutionAccumulatorPrecisionOption](./accumulatorprecisionoption.md)
- [var channelMultiplier: Int](./channelmultiplier.md)
- [var dataSource: any MPSCNNConvolutionDataSource](./datasource.md)
- [var fusedNeuronDescriptor: MPSNNNeuronDescriptor?](./fusedneurondescriptor.md)
- [var neuronParameterC: Float](./neuronparameterc.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolution/neuron)*
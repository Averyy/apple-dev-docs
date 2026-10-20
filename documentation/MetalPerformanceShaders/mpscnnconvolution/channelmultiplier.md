# channelMultiplier

**Framework**: Metal Performance Shaders  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var channelMultiplier: Int { get }
```

```objc
@property (nonatomic, readonly) NSUInteger channelMultiplier;
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
- [var neuron: MPSCNNNeuron?](./neuron.md)
  The neuron filter to be applied as part of the convolution operation.
- [class MPSCNNNeuron](../mpscnnneuron.md)
  A filter that applies a neuron activation function.
- [var neuronType: MPSCNNNeuronType](./neurontype.md)
- [enum MPSCNNNeuronType](../mpscnnneurontype.md)
  The types of neuron filter to append to a convolution.
- [var neuronParameterA: Float](./neuronparametera.md)
- [var neuronParameterB: Float](./neuronparameterb.md)
- [var accumulatorPrecisionOption: MPSNNConvolutionAccumulatorPrecisionOption](./accumulatorprecisionoption.md)
- [var dataSource: any MPSCNNConvolutionDataSource](./datasource.md)
- [var fusedNeuronDescriptor: MPSNNNeuronDescriptor?](./fusedneurondescriptor.md)
- [var neuronParameterC: Float](./neuronparameterc.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolution/channelmultiplier)*
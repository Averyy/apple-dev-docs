# fusedNeuronDescriptor

**Framework**: Metal Performance Shaders  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
var fusedNeuronDescriptor: MPSNNNeuronDescriptor { get set }
```

```objc
@property (nonatomic, retain, readwrite) MPSNNNeuronDescriptor * fusedNeuronDescriptor;
```

## See Also

### Instance Properties
- [var groups: Int](./groups.md)
  The number of groups that the input and output channels are divided into.
- [var inputFeatureChannels: Int](./inputfeaturechannels.md)
  The number of feature channels per pixel in the input image.
- [var kernelHeight: Int](./kernelheight.md)
  The height of the kernel window.
- [var kernelWidth: Int](./kernelwidth.md)
  The width of the kernel window.
- [var outputFeatureChannels: Int](./outputfeaturechannels.md)
  The number of feature channels per pixel in the output image.
- [var strideInPixelsX: Int](./strideinpixelsx.md)
  The output stride (downsampling factor) in the x dimension.
- [var strideInPixelsY: Int](./strideinpixelsy.md)
  The output stride (downsampling factor) in the y dimension.
- [var neuron: MPSCNNNeuron?](./neuron.md)
  The neuron filter to be applied as part of the convolution operation.
- [var dilationRateX: Int](./dilationratex.md)
- [var dilationRateY: Int](./dilationratey.md)
- [func neuronParameterA() -> Float](./neuronparametera%28%29.md)
- [func neuronParameterB() -> Float](./neuronparameterb%28%29.md)
- [func neuronType() -> MPSCNNNeuronType](./neurontype%28%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutiondescriptor/fusedneurondescriptor)*
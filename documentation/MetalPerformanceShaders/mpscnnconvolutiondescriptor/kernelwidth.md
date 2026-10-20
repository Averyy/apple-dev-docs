# kernelWidth

**Framework**: Metal Performance Shaders  
**Kind**: property  
**Role**: Instance Property

The width of the kernel window.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var kernelWidth: Int { get set }
```

```objc
@property (nonatomic, readwrite) NSUInteger kernelWidth;
```

#### Discussion

The default value is `3`.

Any positive non-zero value is valid, including even values. The position of the left edge of the kernel window is given by `offset.x - (kernelWidth>>1)`.

## See Also

### Instance Properties
- [var groups: Int](./groups.md)
  The number of groups that the input and output channels are divided into.
- [var inputFeatureChannels: Int](./inputfeaturechannels.md)
  The number of feature channels per pixel in the input image.
- [var kernelHeight: Int](./kernelheight.md)
  The height of the kernel window.
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
- [var fusedNeuronDescriptor: MPSNNNeuronDescriptor](./fusedneurondescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutiondescriptor/kernelwidth)*
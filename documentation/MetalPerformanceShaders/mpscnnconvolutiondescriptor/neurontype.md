# neuronType()

**Framework**: Metal Performance Shaders  
**Kind**: method

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func neuronType() -> MPSCNNNeuronType
```

## See Also

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
- [var fusedNeuronDescriptor: MPSNNNeuronDescriptor](mpscnnconvolutiondescriptor/fusedneurondescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutiondescriptor/neurontype())*
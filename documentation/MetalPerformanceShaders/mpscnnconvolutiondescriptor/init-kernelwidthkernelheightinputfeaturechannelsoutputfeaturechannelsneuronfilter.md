# init(kernelWidth:kernelHeight:inputFeatureChannels:outputFeatureChannels:neuronFilter:)

**Framework**: Metal Performance Shaders  
**Kind**: init

Creates a convolution descriptor with an optional neuron filter.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(kernelWidth: Int, kernelHeight: Int, inputFeatureChannels: Int, outputFeatureChannels: Int, neuronFilter: MPSCNNNeuron?)
```

#### Return Value

A valid [`MPSCNNConvolution`](mpscnnconvolution.md) object or `nil`, if failure.

## Parameters

- `kernelWidth`: This value must be  . Larger values will take a longer time to process.
- `kernelHeight`: The value must be  . Larger values will take a longer time to process.
- `inputFeatureChannels`: This value must be  .
- `outputFeatureChannels`: This value must be  .
- `neuronFilter`: An optional neuron filter that can be applied to the output of the convolution operation.

## See Also

- [init?(coder: NSCoder)](mpscnnconvolutiondescriptor/init(coder:).md)
- [convenience init(kernelWidth: Int, kernelHeight: Int, inputFeatureChannels: Int, outputFeatureChannels: Int)](mpscnnconvolutiondescriptor/init(kernelwidth:kernelheight:inputfeaturechannels:outputfeaturechannels:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutiondescriptor/init(kernelwidth:kernelheight:inputfeaturechannels:outputfeaturechannels:neuronfilter:))*
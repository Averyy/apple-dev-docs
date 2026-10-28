# init(kernelWidth:kernelHeight:inputFeatureChannels:outputFeatureChannels:neuronFilter:)

**Framework**: Metal Performance Shaders  
**Kind**: init  
**Role**: Initializer

Creates a convolution descriptor with an optional neuron filter.

**Availability**:
- iOS 10.0+ - Deprecated in 11.0
- iPadOS 10.0+ - Deprecated in 11.0
- Mac Catalyst 10.0+ - Deprecated in 11.0
- macOS 10.13+
- tvOS 10.0+ - Deprecated in 11.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
convenience init(kernelWidth: Int, kernelHeight: Int, inputFeatureChannels: Int, outputFeatureChannels: Int, neuronFilter: MPSCNNNeuron?)
```

```objc
+ (instancetype) cnnConvolutionDescriptorWithKernelWidth:(NSUInteger) kernelWidth kernelHeight:(NSUInteger) kernelHeight inputFeatureChannels:(NSUInteger) inputFeatureChannels outputFeatureChannels:(NSUInteger) outputFeatureChannels neuronFilter:(const MPSCNNNeuron *) neuronFilter;
```

## Return Value

A valid [`MPSCNNConvolution`](../mpscnnconvolution.md) object or `nil`, if failure.

## Parameters

- `kernelWidth`: The width of the kernel window.

  This value must be `>0`. Larger values will take a longer time to process.
- `kernelHeight`: The height of the kernel window.

  The value must be `>0`. Larger values will take a longer time to process.
- `inputFeatureChannels`: The number of feature channels in the input image.

  This value must be `>=1`.
- `outputFeatureChannels`: The number of feature channels in the output image.

  This value must be `>=1`.
- `neuronFilter`: An optional neuron filter that can be applied to the output of the convolution operation.

## See Also

### Type Methods
- [init?(coder: NSCoder)](./init%28coder%29.md)
- [convenience init(kernelWidth: Int, kernelHeight: Int, inputFeatureChannels: Int, outputFeatureChannels: Int)](./init%28kernelwidth,kernelheight,inputfeaturechannels,outputfeaturechannels%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutiondescriptor/init(kernelwidth:kernelheight:inputfeaturechannels:outputfeaturechannels:neuronfilter:))*
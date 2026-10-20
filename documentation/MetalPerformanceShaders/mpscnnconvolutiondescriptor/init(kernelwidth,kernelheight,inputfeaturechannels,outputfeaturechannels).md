# init(kernelWidth:kernelHeight:inputFeatureChannels:outputFeatureChannels:)

**Framework**: Metal Performance Shaders  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(kernelWidth: Int, kernelHeight: Int, inputFeatureChannels: Int, outputFeatureChannels: Int)
```

```objc
+ (instancetype) cnnConvolutionDescriptorWithKernelWidth:(NSUInteger) kernelWidth kernelHeight:(NSUInteger) kernelHeight inputFeatureChannels:(NSUInteger) inputFeatureChannels outputFeatureChannels:(NSUInteger) outputFeatureChannels;
```

## See Also

### Type Methods
- [init?(coder: NSCoder)](./init%28coder%29.md)
- [convenience init(kernelWidth: Int, kernelHeight: Int, inputFeatureChannels: Int, outputFeatureChannels: Int, neuronFilter: MPSCNNNeuron?)](./init%28kernelwidth,kernelheight,inputfeaturechannels,outputfeaturechannels,neuronfilter%29.md)
  Creates a convolution descriptor with an optional neuron filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutiondescriptor/init(kernelwidth:kernelheight:inputfeaturechannels:outputfeaturechannels:))*
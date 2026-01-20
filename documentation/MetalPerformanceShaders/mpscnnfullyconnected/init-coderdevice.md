# init(coder:device:)

**Framework**: Metal Performance Shaders  
**Kind**: init

Initializes a fully connected convolution layer.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init?(coder aDecoder: NSCoder, device: any MTLDevice)
```

## See Also

- [init(device: any MTLDevice, weights: any MPSCNNConvolutionDataSource)](mpscnnfullyconnected/init(device:weights:).md)
  Initializes a fully connected convolution layer.
- [protocol MPSCNNConvolutionDataSource](mpscnnconvolutiondatasource.md)
  The protocol that provides convolution filter weights and bias terms.
- [init(device: any MTLDevice, convolutionDescriptor: MPSCNNConvolutionDescriptor, kernelWeights: UnsafePointer<Float>, biasTerms: UnsafePointer<Float>?, flags: MPSCNNConvolutionFlags)](mpscnnfullyconnected/init(device:convolutiondescriptor:kernelweights:biasterms:flags:).md)
  Initializes a fully connected convolution layer.
- [class MPSCNNConvolutionDescriptor](mpscnnconvolutiondescriptor.md)
  A description of the attributes of a convolution kernel.
- [enum MPSCNNConvolutionFlags](mpscnnconvolutionflags.md)
  Options used to control how kernel weights are stored and used in the CNN kernels


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnfullyconnected/init(coder:device:))*
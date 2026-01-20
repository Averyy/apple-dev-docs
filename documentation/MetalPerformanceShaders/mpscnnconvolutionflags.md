# MPSCNNConvolutionFlags

**Framework**: Metal Performance Shaders  
**Kind**: enum

Options used to control how kernel weights are stored and used in the CNN kernels

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum MPSCNNConvolutionFlags
```

## Topics

### Enumeration Cases
- [MPSCNNConvolutionFlags.none](mpscnnconvolutionflags/none.md)
### Initializers
- [init?(rawValue: UInt)](mpscnnconvolutionflags/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [init?(coder: NSCoder, device: any MTLDevice)](mpscnnconvolution/init(coder:device:).md)
- [init(device: any MTLDevice, convolutionDescriptor: MPSCNNConvolutionDescriptor, kernelWeights: UnsafePointer<Float>, biasTerms: UnsafePointer<Float>?, flags: MPSCNNConvolutionFlags)](mpscnnconvolution/init(device:convolutiondescriptor:kernelweights:biasterms:flags:).md)
  Initializes a convolution kernel.
- [class MPSCNNConvolutionDescriptor](mpscnnconvolutiondescriptor.md)
  A description of the attributes of a convolution kernel.
- [init(device: any MTLDevice, weights: any MPSCNNConvolutionDataSource)](mpscnnconvolution/init(device:weights:).md)
- [protocol MPSCNNConvolutionDataSource](mpscnnconvolutiondatasource.md)
  The protocol that provides convolution filter weights and bias terms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutionflags)*
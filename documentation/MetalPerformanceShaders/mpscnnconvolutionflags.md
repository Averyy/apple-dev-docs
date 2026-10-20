# MPSCNNConvolutionFlags

**Framework**: Metal Performance Shaders  
**Kind**: enum  
**Role**: Enumeration

Options used to control how kernel weights are stored and used in the CNN kernels

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
enum MPSCNNConvolutionFlags
```

```c
enum MPSCNNConvolutionFlags : NSUInteger;
```

## Topics

### Enumeration Cases
- [MPSCNNConvolutionFlags.none](./mpscnnconvolutionflags/none.md)
### Initializers
- [init?(rawValue: UInt)](./mpscnnconvolutionflags/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](./mpscnnconvolution/init%28coder,device%29.md)
- [init(device: any MTLDevice, convolutionDescriptor: MPSCNNConvolutionDescriptor, kernelWeights: UnsafePointer<Float>, biasTerms: UnsafePointer<Float>?, flags: MPSCNNConvolutionFlags)](./mpscnnconvolution/init%28device,convolutiondescriptor,kernelweights,biasterms,flags%29.md)
  Initializes a convolution kernel.
- [class MPSCNNConvolutionDescriptor](./mpscnnconvolutiondescriptor.md)
  A description of the attributes of a convolution kernel.
- [init(device: any MTLDevice, weights: any MPSCNNConvolutionDataSource)](./mpscnnconvolution/init%28device,weights%29.md)
- [protocol MPSCNNConvolutionDataSource](./mpscnnconvolutiondatasource.md)
  The protocol that provides convolution filter weights and bias terms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutionflags)*
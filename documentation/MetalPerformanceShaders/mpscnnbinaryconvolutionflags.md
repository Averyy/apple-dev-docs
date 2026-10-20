# MPSCNNBinaryConvolutionFlags

**Framework**: Metal Performance Shaders  
**Kind**: enum  
**Role**: Enumeration

Options used to control binary convolution kernels.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
enum MPSCNNBinaryConvolutionFlags
```

```c
enum MPSCNNBinaryConvolutionFlags : NSUInteger;
```

## Topics

### Enumeration Cases
- [MPSCNNBinaryConvolutionFlags.none](./mpscnnbinaryconvolutionflags/none.md)
- [MPSCNNBinaryConvolutionFlags.useBetaScaling](./mpscnnbinaryconvolutionflags/usebetascaling.md)
### Initializers
- [init?(rawValue: UInt)](./mpscnnbinaryconvolutionflags/init%28rawvalue%29.md)

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
- [init?(coder: NSCoder, device: any MTLDevice)](./mpscnnbinaryconvolution/init%28coder,device%29.md)
- [convenience init(device: any MTLDevice, convolutionData: any MPSCNNConvolutionDataSource, outputBiasTerms: UnsafePointer<Float>?, outputScaleTerms: UnsafePointer<Float>?, inputBiasTerms: UnsafePointer<Float>?, inputScaleTerms: UnsafePointer<Float>?, type: MPSCNNBinaryConvolutionType, flags: MPSCNNBinaryConvolutionFlags)](./mpscnnbinaryconvolution/init%28device,convolutiondata,outputbiasterms,outputscaleterms,inputbiasterms,inputscaleterms,type,flags%29.md)
  Initializes a binary convolution kernel.
- [convenience init(device: any MTLDevice, convolutionData: any MPSCNNConvolutionDataSource, scaleValue: Float, type: MPSCNNBinaryConvolutionType, flags: MPSCNNBinaryConvolutionFlags)](./mpscnnbinaryconvolution/init%28device,convolutiondata,scalevalue,type,flags%29.md)
  Initializes a binary convolution kernel.
- [protocol MPSCNNConvolutionDataSource](./mpscnnconvolutiondatasource.md)
  The protocol that provides convolution filter weights and bias terms.
- [enum MPSCNNBinaryConvolutionType](./mpscnnbinaryconvolutiontype.md)
  Options that defines what operations are used to perform binary convolution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnbinaryconvolutionflags)*
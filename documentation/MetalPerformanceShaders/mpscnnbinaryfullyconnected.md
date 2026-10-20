# MPSCNNBinaryFullyConnected

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A fully connected convolution layer with binary weights and optionally binarized input image.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNBinaryFullyConnected
```

```objc
@interface MPSCNNBinaryFullyConnected : MPSCNNBinaryConvolution
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](./mpscnnbinaryfullyconnected/init%28coder,device%29.md)
  Initializes a fully connected convolution layer with binary weights.
- [convenience init(device: any MTLDevice, convolutionData: any MPSCNNConvolutionDataSource, outputBiasTerms: UnsafePointer<Float>?, outputScaleTerms: UnsafePointer<Float>?, inputBiasTerms: UnsafePointer<Float>?, inputScaleTerms: UnsafePointer<Float>?, type: MPSCNNBinaryConvolutionType, flags: MPSCNNBinaryConvolutionFlags)](./mpscnnbinaryfullyconnected/init%28device,convolutiondata,outputbiasterms,outputscaleterms,inputbiasterms,inputscaleterms,type,flags%29.md)
  Initializes a fully connected convolution layer with binary weights.
- [convenience init(device: any MTLDevice, convolutionData: any MPSCNNConvolutionDataSource, scaleValue: Float, type: MPSCNNBinaryConvolutionType, flags: MPSCNNBinaryConvolutionFlags)](./mpscnnbinaryfullyconnected/init%28device,convolutiondata,scalevalue,type,flags%29.md)
  Initializes a fully connected convolution layer with binary weights.
- [protocol MPSCNNConvolutionDataSource](./mpscnnconvolutiondatasource.md)
  The protocol that provides convolution filter weights and bias terms.
- [enum MPSCNNBinaryConvolutionType](./mpscnnbinaryconvolutiontype.md)
  Options that defines what operations are used to perform binary convolution.
- [enum MPSCNNBinaryConvolutionFlags](./mpscnnbinaryconvolutionflags.md)
  Options used to control binary convolution kernels.

## Relationships

### Inherits From
- [MPSCNNBinaryConvolution](./mpscnnbinaryconvolution.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Fully Connected Layers
- [class MPSCNNFullyConnected](./mpscnnfullyconnected.md)
  A fully connected convolution layer, also known as an inner product layer.
- [class MPSCNNFullyConnectedGradient](./mpscnnfullyconnectedgradient.md)
  A gradient fully connected convolution layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnbinaryfullyconnected)*
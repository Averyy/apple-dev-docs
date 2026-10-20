# MPSCNNFullyConnectedGradient

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A gradient fully connected convolution layer.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNFullyConnectedGradient
```

```objc
@interface MPSCNNFullyConnectedGradient : MPSCNNConvolutionGradient
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](./mpscnnfullyconnectedgradient/init%28coder,device%29.md)
- [init(device: any MTLDevice, weights: any MPSCNNConvolutionDataSource)](./mpscnnfullyconnectedgradient/init%28device,weights%29.md)

## Relationships

### Inherits From
- [MPSCNNConvolutionGradient](./mpscnnconvolutiongradient.md)
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
- [class MPSCNNBinaryFullyConnected](./mpscnnbinaryfullyconnected.md)
  A fully connected convolution layer with binary weights and optionally binarized input image.
- [class MPSCNNFullyConnected](./mpscnnfullyconnected.md)
  A fully connected convolution layer, also known as an inner product layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnfullyconnectedgradient)*
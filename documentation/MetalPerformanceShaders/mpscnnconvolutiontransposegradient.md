# MPSCNNConvolutionTransposeGradient

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNConvolutionTransposeGradient
```

```objc
@interface MPSCNNConvolutionTransposeGradient : MPSCNNGradientKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](./mpscnnconvolutiontransposegradient/init%28coder,device%29.md)
- [init(device: any MTLDevice, weights: any MPSCNNConvolutionDataSource)](./mpscnnconvolutiontransposegradient/init%28device,weights%29.md)
### Instance Properties
- [var dataSource: any MPSCNNConvolutionDataSource](./mpscnnconvolutiontransposegradient/datasource.md)
- [var gradientOption: MPSCNNConvolutionGradientOption](./mpscnnconvolutiontransposegradient/gradientoption.md)
- [var groups: Int](./mpscnnconvolutiontransposegradient/groups.md)
- [var sourceGradientFeatureChannels: Int](./mpscnnconvolutiontransposegradient/sourcegradientfeaturechannels.md)
- [var sourceImageFeatureChannels: Int](./mpscnnconvolutiontransposegradient/sourceimagefeaturechannels.md)
### Instance Methods
- [func reloadWeightsAndBiases(with: any MTLCommandBuffer, state: MPSCNNConvolutionWeightsAndBiasesState)](./mpscnnconvolutiontransposegradient/reloadweightsandbiases%28with,state%29.md)
- [func reloadWeightsAndBiasesFromDataSource()](./mpscnnconvolutiontransposegradient/reloadweightsandbiasesfromdatasource%28%29.md)

## Relationships

### Inherits From
- [MPSCNNGradientKernel](./mpscnngradientkernel.md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutiontransposegradient)*
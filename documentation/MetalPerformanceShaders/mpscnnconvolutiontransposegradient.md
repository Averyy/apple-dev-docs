# MPSCNNConvolutionTransposeGradient

**Framework**: Metal Performance Shaders  
**Kind**: class

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

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpscnnconvolutiontransposegradient/init(coder:device:).md)
- [init(device: any MTLDevice, weights: any MPSCNNConvolutionDataSource)](mpscnnconvolutiontransposegradient/init(device:weights:).md)
### Instance Properties
- [var dataSource: any MPSCNNConvolutionDataSource](mpscnnconvolutiontransposegradient/datasource.md)
- [var gradientOption: MPSCNNConvolutionGradientOption](mpscnnconvolutiontransposegradient/gradientoption.md)
- [var groups: Int](mpscnnconvolutiontransposegradient/groups.md)
- [var sourceGradientFeatureChannels: Int](mpscnnconvolutiontransposegradient/sourcegradientfeaturechannels.md)
- [var sourceImageFeatureChannels: Int](mpscnnconvolutiontransposegradient/sourceimagefeaturechannels.md)
### Instance Methods
- [func reloadWeightsAndBiases(with: any MTLCommandBuffer, state: MPSCNNConvolutionWeightsAndBiasesState)](mpscnnconvolutiontransposegradient/reloadweightsandbiases(with:state:).md)
- [func reloadWeightsAndBiasesFromDataSource()](mpscnnconvolutiontransposegradient/reloadweightsandbiasesfromdatasource.md)

## Relationships

### Inherits From
- [MPSCNNGradientKernel](mpscnngradientkernel.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutiontransposegradient)*
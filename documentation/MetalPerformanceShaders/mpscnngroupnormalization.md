# MPSCNNGroupNormalization

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
class MPSCNNGroupNormalization
```

```objc
@interface MPSCNNGroupNormalization : MPSCNNKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](./mpscnngroupnormalization/init%28coder,device%29.md)
- [init(device: any MTLDevice, dataSource: any MPSCNNGroupNormalizationDataSource)](./mpscnngroupnormalization/init%28device,datasource%29.md)
### Instance Properties
- [var dataSource: any MPSCNNGroupNormalizationDataSource](./mpscnngroupnormalization/datasource.md)
- [var epsilon: Float](./mpscnngroupnormalization/epsilon.md)
### Instance Methods
- [func reloadGammaAndBeta(with: any MTLCommandBuffer, gammaAndBetaState: MPSCNNNormalizationGammaAndBetaState)](./mpscnngroupnormalization/reloadgammaandbeta%28with,gammaandbetastate%29.md)
- [func reloadGammaAndBetaFromDataSource()](./mpscnngroupnormalization/reloadgammaandbetafromdatasource%28%29.md)
- [func resultState(sourceImage: MPSImage, sourceStates: [MPSState]?, destinationImage: MPSImage) -> MPSCNNGroupNormalizationGradientState?](./mpscnngroupnormalization/resultstate%28sourceimage,sourcestates,destinationimage%29.md)
- [func temporaryResultState(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, sourceStates: [MPSState]?, destinationImage: MPSImage) -> MPSCNNGroupNormalizationGradientState?](./mpscnngroupnormalization/temporaryresultstate%28commandbuffer,sourceimage,sourcestates,destinationimage%29.md)

## Relationships

### Inherits From
- [MPSCNNKernel](./mpscnnkernel.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnngroupnormalization)*
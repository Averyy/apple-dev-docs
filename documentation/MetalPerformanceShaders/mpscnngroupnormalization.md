# MPSCNNGroupNormalization

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
class MPSCNNGroupNormalization
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpscnngroupnormalization/init(coder:device:).md)
- [init(device: any MTLDevice, dataSource: any MPSCNNGroupNormalizationDataSource)](mpscnngroupnormalization/init(device:datasource:).md)
### Instance Properties
- [var dataSource: any MPSCNNGroupNormalizationDataSource](mpscnngroupnormalization/datasource.md)
- [var epsilon: Float](mpscnngroupnormalization/epsilon.md)
### Instance Methods
- [func reloadGammaAndBeta(with: any MTLCommandBuffer, gammaAndBetaState: MPSCNNNormalizationGammaAndBetaState)](mpscnngroupnormalization/reloadgammaandbeta(with:gammaandbetastate:).md)
- [func reloadGammaAndBetaFromDataSource()](mpscnngroupnormalization/reloadgammaandbetafromdatasource.md)
- [func resultState(sourceImage: MPSImage, sourceStates: [MPSState]?, destinationImage: MPSImage) -> MPSCNNGroupNormalizationGradientState?](mpscnngroupnormalization/resultstate(sourceimage:sourcestates:destinationimage:).md)
- [func temporaryResultState(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, sourceStates: [MPSState]?, destinationImage: MPSImage) -> MPSCNNGroupNormalizationGradientState?](mpscnngroupnormalization/temporaryresultstate(commandbuffer:sourceimage:sourcestates:destinationimage:).md)

## Relationships

### Inherits From
- [MPSCNNKernel](mpscnnkernel.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnngroupnormalization)*
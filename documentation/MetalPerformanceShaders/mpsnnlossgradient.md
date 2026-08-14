# MPSNNLossGradient

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
class MPSNNLossGradient
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsnnlossgradient/init(coder:device:).md)
- [init(device: any MTLDevice, lossDescriptor: MPSCNNLossDescriptor)](mpsnnlossgradient/init(device:lossdescriptor:).md)
### Instance Properties
- [var computeLabelGradients: Bool](mpsnnlossgradient/computelabelgradients.md)
- [var delta: Float](mpsnnlossgradient/delta.md)
- [var epsilon: Float](mpsnnlossgradient/epsilon.md)
- [var labelSmoothing: Float](mpsnnlossgradient/labelsmoothing.md)
- [var lossType: MPSCNNLossType](mpsnnlossgradient/losstype.md)
- [var numberOfClasses: Int](mpsnnlossgradient/numberofclasses.md)
- [var reduceAcrossBatch: Bool](mpsnnlossgradient/reduceacrossbatch.md)
- [var reductionType: MPSCNNReductionType](mpsnnlossgradient/reductiontype.md)
- [var weight: Float](mpsnnlossgradient/weight.md)
### Instance Methods
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceGradients: [MPSImage], sourceImages: [MPSImage], labels: [MPSImage], weights: [MPSImage]?, sourceStates: [MPSState]?) -> [MPSImage]](mpsnnlossgradient/encodebatch(commandbuffer:sourcegradients:sourceimages:labels:weights:sourcestates:).md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceGradients: [MPSImage], sourceImages: [MPSImage], labels: [MPSImage], weights: [MPSImage]?, sourceStates: [MPSState]?, destinationGradients: [MPSImage])](mpsnnlossgradient/encodebatch(commandbuffer:sourcegradients:sourceimages:labels:weights:sourcestates:destinationgradients:).md)

## Relationships

### Inherits From
- [MPSCNNBinaryKernel](mpscnnbinarykernel.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnlossgradient)*
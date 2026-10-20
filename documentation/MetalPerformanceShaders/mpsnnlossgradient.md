# MPSNNLossGradient

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
class MPSNNLossGradient
```

```objc
@interface MPSNNLossGradient : MPSCNNBinaryKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](./mpsnnlossgradient/init%28coder,device%29.md)
- [init(device: any MTLDevice, lossDescriptor: MPSCNNLossDescriptor)](./mpsnnlossgradient/init%28device,lossdescriptor%29.md)
### Instance Properties
- [var computeLabelGradients: Bool](./mpsnnlossgradient/computelabelgradients.md)
- [var delta: Float](./mpsnnlossgradient/delta.md)
- [var epsilon: Float](./mpsnnlossgradient/epsilon.md)
- [var labelSmoothing: Float](./mpsnnlossgradient/labelsmoothing.md)
- [var lossType: MPSCNNLossType](./mpsnnlossgradient/losstype.md)
- [var numberOfClasses: Int](./mpsnnlossgradient/numberofclasses.md)
- [var reduceAcrossBatch: Bool](./mpsnnlossgradient/reduceacrossbatch.md)
- [var reductionType: MPSCNNReductionType](./mpsnnlossgradient/reductiontype.md)
- [var weight: Float](./mpsnnlossgradient/weight.md)
### Instance Methods
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceGradients: [MPSImage], sourceImages: [MPSImage], labels: [MPSImage], weights: [MPSImage]?, sourceStates: [MPSState]?) -> [MPSImage]](./mpsnnlossgradient/encodebatch%28commandbuffer,sourcegradients,sourceimages,labels,weights,sourcestates%29.md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceGradients: [MPSImage], sourceImages: [MPSImage], labels: [MPSImage], weights: [MPSImage]?, sourceStates: [MPSState]?, destinationGradients: [MPSImage])](./mpsnnlossgradient/encodebatch%28commandbuffer,sourcegradients,sourceimages,labels,weights,sourcestates,destinationgradients%29.md)

## Relationships

### Inherits From
- [MPSCNNBinaryKernel](./mpscnnbinarykernel.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnlossgradient)*
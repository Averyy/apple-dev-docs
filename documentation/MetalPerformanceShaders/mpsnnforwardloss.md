# MPSNNForwardLoss

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
class MPSNNForwardLoss
```

```objc
@interface MPSNNForwardLoss : MPSCNNKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](./mpsnnforwardloss/init%28coder,device%29.md)
- [init(device: any MTLDevice, lossDescriptor: MPSCNNLossDescriptor)](./mpsnnforwardloss/init%28device,lossdescriptor%29.md)
### Instance Properties
- [var delta: Float](./mpsnnforwardloss/delta.md)
- [var epsilon: Float](./mpsnnforwardloss/epsilon.md)
- [var labelSmoothing: Float](./mpsnnforwardloss/labelsmoothing.md)
- [var lossType: MPSCNNLossType](./mpsnnforwardloss/losstype.md)
- [var numberOfClasses: Int](./mpsnnforwardloss/numberofclasses.md)
- [var reduceAcrossBatch: Bool](./mpsnnforwardloss/reduceacrossbatch.md)
- [var reductionType: MPSCNNReductionType](./mpsnnforwardloss/reductiontype.md)
- [var weight: Float](./mpsnnforwardloss/weight.md)
### Instance Methods
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], labels: [MPSImage], weights: [MPSImage]?, destinationStates: [MPSState]?, destinationImages: [MPSImage])](./mpsnnforwardloss/encodebatch%28commandbuffer,sourceimages,labels,weights,destinationstates,destinationimages%29.md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], labels: [MPSImage], weights: [MPSImage]?, outStates: AutoreleasingUnsafeMutablePointer<NSArray?>?, isTemporary: Bool) -> [MPSImage]](./mpsnnforwardloss/encodebatch%28commandbuffer,sourceimages,labels,weights,outstates,istemporary%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnforwardloss)*
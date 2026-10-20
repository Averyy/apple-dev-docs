# MPSCNNLoss

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A kernel that computes the loss and loss gradient between specified predictions and labels.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNLoss
```

```objc
@interface MPSCNNLoss : MPSCNNKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](./mpscnnloss/init%28coder,device%29.md)
- [init(device: any MTLDevice, lossDescriptor: MPSCNNLossDescriptor)](./mpscnnloss/init%28device,lossdescriptor%29.md)
### Instance Properties
- [var delta: Float](./mpscnnloss/delta.md)
- [var epsilon: Float](./mpscnnloss/epsilon.md)
- [var labelSmoothing: Float](./mpscnnloss/labelsmoothing.md)
- [var lossType: MPSCNNLossType](./mpscnnloss/losstype.md)
- [var numberOfClasses: Int](./mpscnnloss/numberofclasses.md)
- [var reduceAcrossBatch: Bool](./mpscnnloss/reduceacrossbatch.md)
- [var reductionType: MPSCNNReductionType](./mpscnnloss/reductiontype.md)
- [var weight: Float](./mpscnnloss/weight.md)
### Instance Methods
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, labels: MPSCNNLossLabels) -> MPSImage](./mpscnnloss/encode%28commandbuffer,sourceimage,labels%29.md)
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, labels: MPSCNNLossLabels, destinationImage: MPSImage)](./mpscnnloss/encode%28commandbuffer,sourceimage,labels,destinationimage%29.md)
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], labels: [MPSCNNLossLabels]) -> [MPSImage]](./mpscnnloss/encode%28commandbuffer,sourceimages,labels%29.md)
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], labels: [MPSCNNLossLabels], destinationImages: [MPSImage])](./mpscnnloss/encode%28commandbuffer,sourceimages,labels,destinationimages%29.md)

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

## See Also

### Loss Layers
- [class MPSCNNLossDataDescriptor](./mpscnnlossdatadescriptor.md)
  An object that specifies properties used by a loss data descriptor.
- [class MPSCNNLossDescriptor](./mpscnnlossdescriptor.md)
  An object that specifies properties used by a loss kernel.
- [class MPSCNNLossLabels](./mpscnnlosslabels.md)
  A class that stores the per-element weight buffer used by loss and gradient loss kernels.
- [class MPSCNNYOLOLoss](./mpscnnyololoss.md)
  A kernel that computes the YOLO loss and loss gradient between specified predictions and labels.
- [class MPSCNNYOLOLossDescriptor](./mpscnnyololossdescriptor.md)
  An object that specifies properties used by a YOLO loss kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnloss)*
# MPSCNNYOLOLoss

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A kernel that computes the YOLO loss and loss gradient between specified predictions and labels.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNYOLOLoss
```

```objc
@interface MPSCNNYOLOLoss : MPSCNNKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](./mpscnnyololoss/init%28coder,device%29.md)
- [init(device: any MTLDevice, lossDescriptor: MPSCNNYOLOLossDescriptor)](./mpscnnyololoss/init%28device,lossdescriptor%29.md)
### Instance Properties
- [var anchorBoxes: Data](./mpscnnyololoss/anchorboxes.md)
- [var lossClasses: MPSCNNLoss](./mpscnnyololoss/lossclasses.md)
- [var lossConfidence: MPSCNNLoss](./mpscnnyololoss/lossconfidence.md)
- [var lossWH: MPSCNNLoss](./mpscnnyololoss/losswh.md)
- [var lossXY: MPSCNNLoss](./mpscnnyololoss/lossxy.md)
- [var maxIOUForObjectAbsence: Float](./mpscnnyololoss/maxiouforobjectabsence.md)
- [var minIOUForObjectPresence: Float](./mpscnnyololoss/miniouforobjectpresence.md)
- [var numberOfAnchorBoxes: Int](./mpscnnyololoss/numberofanchorboxes.md)
- [var reduceAcrossBatch: Bool](./mpscnnyololoss/reduceacrossbatch.md)
- [var reductionType: MPSCNNReductionType](./mpscnnyololoss/reductiontype.md)
- [var scaleClass: Float](./mpscnnyololoss/scaleclass.md)
- [var scaleNoObject: Float](./mpscnnyololoss/scalenoobject.md)
- [var scaleObject: Float](./mpscnnyololoss/scaleobject.md)
- [var scaleWH: Float](./mpscnnyololoss/scalewh.md)
- [var scaleXY: Float](./mpscnnyololoss/scalexy.md)
### Instance Methods
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, labels: MPSCNNLossLabels) -> MPSImage](./mpscnnyololoss/encode%28commandbuffer,sourceimage,labels%29.md)
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, labels: MPSCNNLossLabels, destinationImage: MPSImage)](./mpscnnyololoss/encode%28commandbuffer,sourceimage,labels,destinationimage%29.md)
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], labels: [MPSCNNLossLabels]) -> [MPSImage]](./mpscnnyololoss/encode%28commandbuffer,sourceimages,labels%29.md)
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], labels: [MPSCNNLossLabels], destinationImages: [MPSImage])](./mpscnnyololoss/encode%28commandbuffer,sourceimages,labels,destinationimages%29.md)

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
- [class MPSCNNLoss](./mpscnnloss.md)
  A kernel that computes the loss and loss gradient between specified predictions and labels.
- [class MPSCNNLossDataDescriptor](./mpscnnlossdatadescriptor.md)
  An object that specifies properties used by a loss data descriptor.
- [class MPSCNNLossDescriptor](./mpscnnlossdescriptor.md)
  An object that specifies properties used by a loss kernel.
- [class MPSCNNLossLabels](./mpscnnlosslabels.md)
  A class that stores the per-element weight buffer used by loss and gradient loss kernels.
- [class MPSCNNYOLOLossDescriptor](./mpscnnyololossdescriptor.md)
  An object that specifies properties used by a YOLO loss kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnyololoss)*
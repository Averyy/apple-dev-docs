# MPSCNNLossLabels

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A class that stores the per-element weight buffer used by loss and gradient loss kernels.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNLossLabels
```

```objc
@interface MPSCNNLossLabels : MPSState
```

## Topics

### Initializers
- [convenience init(device: any MTLDevice, labelsDescriptor: MPSCNNLossDataDescriptor)](./mpscnnlosslabels/init%28device,labelsdescriptor%29.md)
- [init(device: any MTLDevice, lossImageSize: MTLSize, labelsDescriptor: MPSCNNLossDataDescriptor, weightsDescriptor: MPSCNNLossDataDescriptor?)](./mpscnnlosslabels/init%28device,lossimagesize,labelsdescriptor,weightsdescriptor%29.md)
- [init(device: any MTLDevice, lossImageSize: MTLSize, labelsImage: MPSImage, weightsImage: MPSImage?)](./mpscnnlosslabels/init%28device,lossimagesize,labelsimage,weightsimage%29.md)
### Instance Methods
- [func labelsImage() -> MPSImage](./mpscnnlosslabels/labelsimage%28%29.md)
- [func lossImage() -> MPSImage](./mpscnnlosslabels/lossimage%28%29.md)
- [func weightsImage() -> MPSImage](./mpscnnlosslabels/weightsimage%28%29.md)

## Relationships

### Inherits From
- [MPSState](./mpsstate.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Loss Layers
- [class MPSCNNLoss](./mpscnnloss.md)
  A kernel that computes the loss and loss gradient between specified predictions and labels.
- [class MPSCNNLossDataDescriptor](./mpscnnlossdatadescriptor.md)
  An object that specifies properties used by a loss data descriptor.
- [class MPSCNNLossDescriptor](./mpscnnlossdescriptor.md)
  An object that specifies properties used by a loss kernel.
- [class MPSCNNYOLOLoss](./mpscnnyololoss.md)
  A kernel that computes the YOLO loss and loss gradient between specified predictions and labels.
- [class MPSCNNYOLOLossDescriptor](./mpscnnyololossdescriptor.md)
  An object that specifies properties used by a YOLO loss kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnlosslabels)*
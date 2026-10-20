# MPSCNNDropout

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A dropout filter.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNDropout
```

```objc
@interface MPSCNNDropout : MPSCNNKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](./mpscnndropout/init%28coder,device%29.md)
- [init(device: any MTLDevice, keepProbability: Float, seed: Int, maskStrideInPixels: MTLSize)](./mpscnndropout/init%28device,keepprobability,seed,maskstrideinpixels%29.md)
### Instance Properties
- [var keepProbability: Float](./mpscnndropout/keepprobability.md)
- [var maskStrideInPixels: MTLSize](./mpscnndropout/maskstrideinpixels.md)
- [var seed: Int](./mpscnndropout/seed.md)
### Instance Methods
- [func resultState(sourceImage: MPSImage, sourceStates: [MPSState]?, destinationImage: MPSImage) -> MPSCNNDropoutGradientState?](./mpscnndropout/resultstate%28sourceimage,sourcestates,destinationimage%29.md)
- [func resultStateBatch(sourceImage: [MPSImage], sourceStates: [[MPSState]]?, destinationImage: [MPSImage]) -> MPSCNNDropoutGradientState?](./mpscnndropout/resultstatebatch%28sourceimage,sourcestates,destinationimage%29.md)
- [func temporaryResultState(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, sourceStates: [MPSState]?, destinationImage: MPSImage) -> MPSCNNDropoutGradientState?](./mpscnndropout/temporaryresultstate%28commandbuffer,sourceimage,sourcestates,destinationimage%29.md)
- [func temporaryResultStateBatch(commandBuffer: any MTLCommandBuffer, sourceImage: [MPSImage], sourceStates: [[MPSState]]?, destinationImage: [MPSImage]) -> [MPSCNNDropoutGradientState]?](./mpscnndropout/temporaryresultstatebatch%28commandbuffer,sourceimage,sourcestates,destinationimage%29.md)

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

### Dropout Layers
- [class MPSCNNDropoutGradient](./mpscnndropoutgradient.md)
  A gradient dropout filter.
- [class MPSCNNDropoutGradientState](./mpscnndropoutgradientstate.md)
  A class that stores the mask used by dropout and gradient dropout filters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnndropout)*
# MPSNNReshape

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

The base class for reshape operations.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSNNReshape
```

```objc
@interface MPSNNReshape : MPSCNNKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](./mpsnnreshape/init%28coder,device%29.md)
- [init(device: any MTLDevice)](./mpsnnreshape/init%28device%29.md)
### Instance Methods
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, destinationState: AutoreleasingUnsafeMutablePointer<MPSState?>, destinationStateIsTemporary: Bool, reshapedWidth: Int, reshapedHeight: Int, reshapedFeatureChannels: Int) -> MPSImage](./mpsnnreshape/encode%28commandbuffer,sourceimage,destinationstate,destinationstateistemporary,reshapedwidth,reshapedheight,reshapedfeaturechannels%29.md)
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, reshapedWidth: Int, reshapedHeight: Int, reshapedFeatureChannels: Int) -> MPSImage](./mpsnnreshape/encode%28commandbuffer,sourceimage,reshapedwidth,reshapedheight,reshapedfeaturechannels%29.md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], destinationStates: AutoreleasingUnsafeMutablePointer<NSArray?>, destinationStateIsTemporary: Bool, reshapedWidth: Int, reshapedHeight: Int, reshapedFeatureChannels: Int) -> [MPSImage]](./mpsnnreshape/encodebatch%28commandbuffer,sourceimages,destinationstates,destinationstateistemporary,reshapedwidth,reshapedheight,reshapedfeaturechannels%29.md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], reshapedWidth: Int, reshapedHeight: Int, reshapedFeatureChannels: Int) -> [MPSImage]](./mpsnnreshape/encodebatch%28commandbuffer,sourceimages,reshapedwidth,reshapedheight,reshapedfeaturechannels%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnreshape)*
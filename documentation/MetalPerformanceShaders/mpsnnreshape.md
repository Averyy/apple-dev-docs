# MPSNNReshape

**Framework**: Metal Performance Shaders  
**Kind**: class

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

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsnnreshape/init(coder:device:).md)
- [init(device: any MTLDevice)](mpsnnreshape/init(device:).md)
### Instance Methods
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, destinationState: AutoreleasingUnsafeMutablePointer<MPSState?>, destinationStateIsTemporary: Bool, reshapedWidth: Int, reshapedHeight: Int, reshapedFeatureChannels: Int) -> MPSImage](mpsnnreshape/encode(commandbuffer:sourceimage:destinationstate:destinationstateistemporary:reshapedwidth:reshapedheight:reshapedfeaturechannels:).md)
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, reshapedWidth: Int, reshapedHeight: Int, reshapedFeatureChannels: Int) -> MPSImage](mpsnnreshape/encode(commandbuffer:sourceimage:reshapedwidth:reshapedheight:reshapedfeaturechannels:).md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], destinationStates: AutoreleasingUnsafeMutablePointer<NSArray?>, destinationStateIsTemporary: Bool, reshapedWidth: Int, reshapedHeight: Int, reshapedFeatureChannels: Int) -> [MPSImage]](mpsnnreshape/encodebatch(commandbuffer:sourceimages:destinationstates:destinationstateistemporary:reshapedwidth:reshapedheight:reshapedfeaturechannels:).md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], reshapedWidth: Int, reshapedHeight: Int, reshapedFeatureChannels: Int) -> [MPSImage]](mpsnnreshape/encodebatch(commandbuffer:sourceimages:reshapedwidth:reshapedheight:reshapedfeaturechannels:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnreshape)*
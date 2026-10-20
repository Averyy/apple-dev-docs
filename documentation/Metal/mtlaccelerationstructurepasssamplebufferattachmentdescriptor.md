# MTLAccelerationStructurePassSampleBufferAttachmentDescriptor

**Framework**: Metal  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class MTLAccelerationStructurePassSampleBufferAttachmentDescriptor
```

```objc
@interface MTLAccelerationStructurePassSampleBufferAttachmentDescriptor : NSObject
```

## Mentions

- [Sampling GPU data into counter sample buffers](./sampling-gpu-data-into-counter-sample-buffers.md)

## Topics

### Instance Properties
- [var endOfEncoderSampleIndex: Int](./mtlaccelerationstructurepasssamplebufferattachmentdescriptor/endofencodersampleindex.md)
- [var sampleBuffer: (any MTLCounterSampleBuffer)?](./mtlaccelerationstructurepasssamplebufferattachmentdescriptor/samplebuffer.md)
  A specialized memory buffer that the GPU uses to store its counter data during the acceleration structure pass.
- [var startOfEncoderSampleIndex: Int](./mtlaccelerationstructurepasssamplebufferattachmentdescriptor/startofencodersampleindex.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Acceleration structures passes
- [class MTLAccelerationStructurePassDescriptor](./mtlaccelerationstructurepassdescriptor.md)
- [class MTLAccelerationStructurePassSampleBufferAttachmentDescriptorArray](./mtlaccelerationstructurepasssamplebufferattachmentdescriptorarray.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructurepasssamplebufferattachmentdescriptor)*
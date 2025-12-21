# MTLBlitPassSampleBufferAttachmentDescriptor

**Framework**: Metal  
**Kind**: class

A configuration that instructs the GPU where to store counter data from the beginning and end of a blit pass.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class MTLBlitPassSampleBufferAttachmentDescriptor
```

## Mentions

- [Sampling GPU data into counter sample buffers](sampling-gpu-data-into-counter-sample-buffers.md)

#### Overview

See [`Sampling GPU data into counter sample buffers`](sampling-gpu-data-into-counter-sample-buffers.md) for more context about configuring instances of this type. That article is one of a series of articles in [`GPU counters and counter sample buffers`](gpu-counters-and-counter-sample-buffers.md).

## Topics

### Configuring the sample buffer attachment
- [var sampleBuffer: (any MTLCounterSampleBuffer)?](mtlblitpasssamplebufferattachmentdescriptor/samplebuffer.md)
  A specialized memory buffer that the GPU uses to store its counter data during the blit pass.
- [var startOfEncoderSampleIndex: Int](mtlblitpasssamplebufferattachmentdescriptor/startofencodersampleindex.md)
  An index within a counter sample buffer that tells the GPU where to store counter data from the start of a blit pass.
- [var endOfEncoderSampleIndex: Int](mtlblitpasssamplebufferattachmentdescriptor/endofencodersampleindex.md)
  An index within a counter sample buffer that tells the GPU where to store counter data from the end of a blit pass.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MTLBlitPassDescriptor](mtlblitpassdescriptor.md)
  A configuration you create to customize a blit command encoder, which affects the runtime behavior of the blit pass you encode with it.
- [class MTLBlitPassSampleBufferAttachmentDescriptorArray](mtlblitpasssamplebufferattachmentdescriptorarray.md)
  A container that stores an array of sample buffer attachments for a blit pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlblitpasssamplebufferattachmentdescriptor)*
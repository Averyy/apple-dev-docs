# MTLBlitPassSampleBufferAttachmentDescriptor

**Framework**: Metal  
**Kind**: class  
**Role**: Class

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

```objc
@interface MTLBlitPassSampleBufferAttachmentDescriptor : NSObject
```

## Mentions

- [Sampling GPU data into counter sample buffers](./sampling-gpu-data-into-counter-sample-buffers.md)

#### Overview

See [Sampling GPU data into counter sample buffers](./sampling-gpu-data-into-counter-sample-buffers.md) for more context about configuring instances of this type. That article is one of a series of articles in [GPU counters and counter sample buffers](./gpu-counters-and-counter-sample-buffers.md).

## Topics

### Configuring the sample buffer attachment
- [var sampleBuffer: (any MTLCounterSampleBuffer)?](./mtlblitpasssamplebufferattachmentdescriptor/samplebuffer.md)
  A specialized memory buffer that the GPU uses to store its counter data during the blit pass.
- [var startOfEncoderSampleIndex: Int](./mtlblitpasssamplebufferattachmentdescriptor/startofencodersampleindex.md)
  An index within a counter sample buffer that tells the GPU where to store counter data from the start of a blit pass.
- [var endOfEncoderSampleIndex: Int](./mtlblitpasssamplebufferattachmentdescriptor/endofencodersampleindex.md)
  An index within a counter sample buffer that tells the GPU where to store counter data from the end of a blit pass.

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

### Configuring a blit command encoder
- [class MTLBlitPassDescriptor](./mtlblitpassdescriptor.md)
  A configuration you create to customize a blit command encoder, which affects the runtime behavior of the blit pass you encode with it.
- [class MTLBlitPassSampleBufferAttachmentDescriptorArray](./mtlblitpasssamplebufferattachmentdescriptorarray.md)
  A container that stores an array of sample buffer attachments for a blit pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlblitpasssamplebufferattachmentdescriptor)*
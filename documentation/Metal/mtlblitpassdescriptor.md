# MTLBlitPassDescriptor

**Framework**: Metal  
**Kind**: class

A configuration you create to customize a blit command encoder, which affects the runtime behavior of the blit pass you encode with it.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class MTLBlitPassDescriptor
```

## Mentions

- [Sampling GPU Data into Counter Sample Buffers](sampling-gpu-data-into-counter-sample-buffers.md)

#### Overview

You can customize an encoder for a blit pass by creating and configuring an [`MTLBlitPassDescriptor`](mtlblitpassdescriptor.md) instance and passing it to [`makeBlitCommandEncoder(descriptor:)`](mtlcommandbuffer/makeblitcommandencoder(descriptor:).md).

## Topics

### Configuring Sample Buffer Attachment Descriptors for a Blit Pass
- [var sampleBufferAttachments: MTLBlitPassSampleBufferAttachmentDescriptorArray](mtlblitpassdescriptor/samplebufferattachments.md)
  An array of counter sample buffer attachments that you configure for a blit pass.

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

- [class MTLBlitPassSampleBufferAttachmentDescriptor](mtlblitpasssamplebufferattachmentdescriptor.md)
  A configuration that instructs the GPU where to store counter data from the beginning and end of a blit pass.
- [class MTLBlitPassSampleBufferAttachmentDescriptorArray](mtlblitpasssamplebufferattachmentdescriptorarray.md)
  A container that stores an array of sample buffer attachments for a blit pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlblitpassdescriptor)*
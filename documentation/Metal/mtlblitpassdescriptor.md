# MTLBlitPassDescriptor

**Framework**: Metal  
**Kind**: class  
**Role**: Class

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

```objc
@interface MTLBlitPassDescriptor : NSObject
```

## Mentions

- [Sampling GPU data into counter sample buffers](./sampling-gpu-data-into-counter-sample-buffers.md)

#### Overview

You can customize an encoder for a blit pass by creating and configuring an [`MTLBlitPassDescriptor`](./mtlblitpassdescriptor.md) instance and passing it to [`makeBlitCommandEncoder(descriptor:)`](./mtlcommandbuffer/makeblitcommandencoder%28descriptor%29.md).

## Topics

### Configuring sample buffer attachment descriptors for a blit pass
- [var sampleBufferAttachments: MTLBlitPassSampleBufferAttachmentDescriptorArray](./mtlblitpassdescriptor/samplebufferattachments.md)
  An array of counter sample buffer attachments that you configure for a blit pass.
### Creating a blit pass descriptor
- [+ blitPassDescriptor](./mtlblitpassdescriptor/blitpassdescriptor.md)
  Creates a new blit pass descriptor with a default configuration.

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
- [class MTLBlitPassSampleBufferAttachmentDescriptor](./mtlblitpasssamplebufferattachmentdescriptor.md)
  A configuration that instructs the GPU where to store counter data from the beginning and end of a blit pass.
- [class MTLBlitPassSampleBufferAttachmentDescriptorArray](./mtlblitpasssamplebufferattachmentdescriptorarray.md)
  A container that stores an array of sample buffer attachments for a blit pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlblitpassdescriptor)*
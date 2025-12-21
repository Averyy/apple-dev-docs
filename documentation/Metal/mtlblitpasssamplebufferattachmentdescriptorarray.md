# MTLBlitPassSampleBufferAttachmentDescriptorArray

**Framework**: Metal  
**Kind**: class

A container that stores an array of sample buffer attachments for a blit pass.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class MTLBlitPassSampleBufferAttachmentDescriptorArray
```

#### Overview

The number of elements in the array is at least the number of elements in an [`MTLDevice`](mtldevice.md) instance’s [`counterSets`](mtldevice/countersets.md) property.

## Topics

### Accessing a sample buffer attachment descriptor
- [subscript(Int) -> MTLBlitPassSampleBufferAttachmentDescriptor!](mtlblitpasssamplebufferattachmentdescriptorarray/subscript(_:).md)
  Accesses one of the array’s blit pass sample buffer attachment descriptor instances.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MTLBlitPassDescriptor](mtlblitpassdescriptor.md)
  A configuration you create to customize a blit command encoder, which affects the runtime behavior of the blit pass you encode with it.
- [class MTLBlitPassSampleBufferAttachmentDescriptor](mtlblitpasssamplebufferattachmentdescriptor.md)
  A configuration that instructs the GPU where to store counter data from the beginning and end of a blit pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlblitpasssamplebufferattachmentdescriptorarray)*
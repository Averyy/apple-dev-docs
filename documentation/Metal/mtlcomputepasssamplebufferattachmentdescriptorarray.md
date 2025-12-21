# MTLComputePassSampleBufferAttachmentDescriptorArray

**Framework**: Metal  
**Kind**: class

A container that stores an array of sample buffer attachments for a compute pass.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class MTLComputePassSampleBufferAttachmentDescriptorArray
```

#### Overview

The number of elements in the array is at least the number of elements in an [`MTLDevice`](mtldevice.md) instance’s [`counterSets`](mtldevice/countersets.md) property.

## Topics

### Accessing a sample buffer attachment
- [subscript(Int) -> MTLComputePassSampleBufferAttachmentDescriptor!](mtlcomputepasssamplebufferattachmentdescriptorarray/subscript(_:).md)
  Returns the descriptor object for the specified sample buffer attachment.

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

- [class MTLComputePassDescriptor](mtlcomputepassdescriptor.md)
  A description of how to dispatch execution of pass commands and GPU performance sampling.
- [enum MTLDispatchType](mtldispatchtype.md)
  The type of dispatch method to use when calling encoded functions.
- [struct MTLDispatchThreadgroupsIndirectArguments](mtldispatchthreadgroupsindirectarguments.md)
  The data layout required for arguments needed to specify the size of threadgroups.
- [class MTLComputePassSampleBufferAttachmentDescriptor](mtlcomputepasssamplebufferattachmentdescriptor.md)
  A configuration that instructs the GPU where to store counter data from the beginning and end of a compute pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputepasssamplebufferattachmentdescriptorarray)*
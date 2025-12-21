# MTLComputePassDescriptor

**Framework**: Metal  
**Kind**: class

A description of how to dispatch execution of pass commands and GPU performance sampling.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class MTLComputePassDescriptor
```

## Mentions

- [Sampling GPU data into counter sample buffers](sampling-gpu-data-into-counter-sample-buffers.md)

## Topics

### Configuring the dispatch mechanism
- [var dispatchType: MTLDispatchType](mtlcomputepassdescriptor/dispatchtype.md)
  The strategy for dispatching any compute commands encoded in the compute pass.
### Specifying sample buffers for GPU counters
- [var sampleBufferAttachments: MTLComputePassSampleBufferAttachmentDescriptorArray](mtlcomputepassdescriptor/samplebufferattachments.md)
  The sample buffers that the compute pass can access.

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

- [enum MTLDispatchType](mtldispatchtype.md)
  The type of dispatch method to use when calling encoded functions.
- [struct MTLDispatchThreadgroupsIndirectArguments](mtldispatchthreadgroupsindirectarguments.md)
  The data layout required for arguments needed to specify the size of threadgroups.
- [class MTLComputePassSampleBufferAttachmentDescriptor](mtlcomputepasssamplebufferattachmentdescriptor.md)
  A configuration that instructs the GPU where to store counter data from the beginning and end of a compute pass.
- [class MTLComputePassSampleBufferAttachmentDescriptorArray](mtlcomputepasssamplebufferattachmentdescriptorarray.md)
  A container that stores an array of sample buffer attachments for a compute pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputepassdescriptor)*
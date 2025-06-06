# MTLComputePassSampleBufferAttachmentDescriptor

**Framework**: Metal  
**Kind**: class

A configuration that instructs the GPU where to store counter data from the beginning and end of a compute pass.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class MTLComputePassSampleBufferAttachmentDescriptor
```

## Mentions

- [Sampling GPU Data into Counter Sample Buffers](sampling-gpu-data-into-counter-sample-buffers.md)

#### Overview

For more context about configuring sample buffer attachments for compute passes, see [`Sampling GPU Data into Counter Sample Buffers`](sampling-gpu-data-into-counter-sample-buffers.md). That article is one of a series in [`GPU Counters and Counter Sample Buffers`](gpu-counters-and-counter-sample-buffers.md) about sampling Metal hardware counters for performance measurement.

## Topics

### Configuring the Sample Buffer Attachment
- [var sampleBuffer: (any MTLCounterSampleBuffer)?](mtlcomputepasssamplebufferattachmentdescriptor/samplebuffer.md)
  A specialized memory buffer that the GPU uses to store its counter data during a compute pass.
- [var startOfEncoderSampleIndex: Int](mtlcomputepasssamplebufferattachmentdescriptor/startofencodersampleindex.md)
  An index within a counter sample buffer that tells the GPU where to store counter data from the start of a compute pass.
- [var endOfEncoderSampleIndex: Int](mtlcomputepasssamplebufferattachmentdescriptor/endofencodersampleindex.md)
  An index within a counter sample buffer that tells the GPU where to store counter data from the end of a compute pass.

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

- [class MTLComputePassDescriptor](mtlcomputepassdescriptor.md)
  A description of how to dispatch execution of pass commands and GPU performance sampling.
- [enum MTLDispatchType](mtldispatchtype.md)
  The type of dispatch method to use when calling encoded functions.
- [struct MTLDispatchThreadgroupsIndirectArguments](mtldispatchthreadgroupsindirectarguments.md)
  The data layout required for arguments needed to specify the size of threadgroups.
- [class MTLComputePassSampleBufferAttachmentDescriptorArray](mtlcomputepasssamplebufferattachmentdescriptorarray.md)
  A container that stores an array of sample buffer attachments for a compute pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputepasssamplebufferattachmentdescriptor)*
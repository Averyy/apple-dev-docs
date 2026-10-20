# MTLDispatchThreadgroupsIndirectArguments

**Framework**: Metal  
**Kind**: struct  
**Role**: Structure

The data layout required for arguments needed to specify the size of threadgroups.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
struct MTLDispatchThreadgroupsIndirectArguments
```

```c
typedef struct { ... } MTLDispatchThreadgroupsIndirectArguments;
```

## Mentions

- [Specifying drawing and dispatch arguments indirectly](./specifying-drawing-and-dispatch-arguments-indirectly.md)

## Topics

### Specifying the size of the threadgroup
- [init()](./mtldispatchthreadgroupsindirectarguments/init%28%29.md)
  Returns a new data layout for dispatching threadgroups over indirect buffer calls.
- [init(threadgroupsPerGrid: (UInt32, UInt32, UInt32))](./mtldispatchthreadgroupsindirectarguments/init%28threadgroupspergrid%29.md)
  Returns a new data layout for dispatching threadgroups over indirect buffer calls, with specified threadgroups per grid.
- [var threadgroupsPerGrid: (UInt32, UInt32, UInt32)](./mtldispatchthreadgroupsindirectarguments/threadgroupspergrid.md)
  The number of threadgroups for the grid, in each dimension.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Related Documentation
- [func dispatchThreadgroups(indirectBuffer: any MTLBuffer, indirectBufferOffset: Int, threadsPerThreadgroup: MTLSize)](./mtlcomputecommandencoder/dispatchthreadgroups%28indirectbuffer,indirectbufferoffset,threadsperthreadgroup%29.md)
  Encodes a dispatch call for a compute pass, using an indirect buffer that defines the size of a grid that aligns to threadgroup boundaries.
### Configuring a compute pass
- [class MTLComputePassDescriptor](./mtlcomputepassdescriptor.md)
  A description of how to dispatch execution of pass commands and GPU performance sampling.
- [enum MTLDispatchType](./mtldispatchtype.md)
  The type of dispatch method to use when calling encoded functions.
- [class MTLComputePassSampleBufferAttachmentDescriptor](./mtlcomputepasssamplebufferattachmentdescriptor.md)
  A configuration that instructs the GPU where to store counter data from the beginning and end of a compute pass.
- [class MTLComputePassSampleBufferAttachmentDescriptorArray](./mtlcomputepasssamplebufferattachmentdescriptorarray.md)
  A container that stores an array of sample buffer attachments for a compute pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldispatchthreadgroupsindirectarguments)*
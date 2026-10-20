# dispatchThreadgroups(indirectBuffer:indirectBufferOffset:threadsPerThreadgroup:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Encodes a dispatch call for a compute pass, using an indirect buffer that defines the size of a grid that aligns to threadgroup boundaries.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func dispatchThreadgroups(indirectBuffer: any MTLBuffer, indirectBufferOffset: Int, threadsPerThreadgroup: MTLSize)
```

```objc
- (void) dispatchThreadgroupsWithIndirectBuffer:(id<MTLBuffer>) indirectBuffer indirectBufferOffset:(NSUInteger) indirectBufferOffset threadsPerThreadgroup:(MTLSize) threadsPerThreadgroup;
```

#### Discussion

The GPU fetches parameters from the indirect buffer just before the thread grid starts. This process lets the compute function run based on GPU feedback, without latency from data transfer between the CPU and the GPU.

## Parameters

- `indirectBuffer`: An [`MTLBuffer`](../mtlbuffer.md) instance providing compute parameters. Lay out the data in this buffer as described in the [`MTLDispatchThreadgroupsIndirectArguments`](../mtldispatchthreadgroupsindirectarguments.md) structure.
- `indirectBufferOffset`: Where the data begins, in bytes, from the start of the buffer. This value needs to be a multiple of `4`.
- `threadsPerThreadgroup`: The number of threads in one threadgroup, in each dimension.

## See Also

### Dispatching from indirect command buffers
- [func executeCommandsInBuffer(any MTLIndirectCommandBuffer, range: Range<Int>)](./executecommandsinbuffer%28_,range%29.md)
  Encodes an instruction to run commands from an indirect buffer.
- [func executeCommandsInBuffer(any MTLIndirectCommandBuffer, indirectBuffer: any MTLBuffer, offset: Int)](./executecommandsinbuffer%28_,indirectbuffer,offset%29.md)
  Encodes an instruction to run commands from an indirect buffer, using another buffer to provide the command range.
- [func executeCommands(in: any MTLIndirectCommandBuffer, indirectBuffer: any MTLBuffer, indirectBufferOffset: Int)](./executecommands%28in,indirectbuffer,indirectbufferoffset%29.md)
  Encodes an instruction to run commands from an indirect buffer, using another buffer to provide the command range.
- [func executeCommands(in: any MTLIndirectCommandBuffer, with: NSRange)](./executecommands%28in,with%29.md)
  Encodes an instruction to run commands from an indirect buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/dispatchthreadgroups(indirectbuffer:indirectbufferoffset:threadsperthreadgroup:))*
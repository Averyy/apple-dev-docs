# executeCommandsInBuffer:indirectBuffer:indirectBufferOffset:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Encodes an instruction to run commands from an indirect buffer, using another buffer to provide the command range.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```objc
- (void) executeCommandsInBuffer:(id<MTLIndirectCommandBuffer>) indirectCommandbuffer indirectBuffer:(id<MTLBuffer>) indirectRangeBuffer indirectBufferOffset:(NSUInteger) indirectBufferOffset;
```

## Parameters

- `indirectCommandbuffer`: The [`MTLIndirectCommandBuffer`](../mtlindirectcommandbuffer.md) instance containing the commands to execute.
- `indirectRangeBuffer`: An indirect buffer containing the execution range, laid out in an [`MTLIndirectCommandBufferExecutionRange`](../mtlindirectcommandbufferexecutionrange.md) instance. The maximum length of the range is `16384` commands.
- `indirectBufferOffset`: The number of bytes from the start of `indirectRangeBuffer` containing the execution range to use. Align the offset on a multiple of `4`.

## See Also

### Dispatching from indirect command buffers
- [func dispatchThreadgroups(indirectBuffer: any MTLBuffer, indirectBufferOffset: Int, threadsPerThreadgroup: MTLSize)](./dispatchthreadgroups%28indirectbuffer,indirectbufferoffset,threadsperthreadgroup%29.md)
  Encodes a dispatch call for a compute pass, using an indirect buffer that defines the size of a grid that aligns to threadgroup boundaries.
- [- executeCommandsInBuffer:withRange:](./executecommandsinbuffer_withrange_.md)
  Encodes an instruction to run commands from an indirect buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/executecommandsinbuffer:indirectbuffer:indirectbufferoffset:)*
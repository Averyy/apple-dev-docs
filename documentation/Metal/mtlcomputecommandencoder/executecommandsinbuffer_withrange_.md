# executeCommandsInBuffer:withRange:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Encodes an instruction to run commands from an indirect buffer.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```objc
- (void) executeCommandsInBuffer:(id<MTLIndirectCommandBuffer>) indirectCommandBuffer withRange:(NSRange) executionRange;
```

## Parameters

- `indirectCommandBuffer`: The [`MTLIndirectCommandBuffer`](../mtlindirectcommandbuffer.md) instance containing the commands to execute.
- `executionRange`: The range of commands to execute. The maximum length of the range is `16384` commands.

## See Also

### Dispatching from indirect command buffers
- [func dispatchThreadgroups(indirectBuffer: any MTLBuffer, indirectBufferOffset: Int, threadsPerThreadgroup: MTLSize)](./dispatchthreadgroups%28indirectbuffer,indirectbufferoffset,threadsperthreadgroup%29.md)
  Encodes a dispatch call for a compute pass, using an indirect buffer that defines the size of a grid that aligns to threadgroup boundaries.
- [- executeCommandsInBuffer:indirectBuffer:indirectBufferOffset:](./executecommandsinbuffer_indirectbuffer_indirectbufferoffset_.md)
  Encodes an instruction to run commands from an indirect buffer, using another buffer to provide the command range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/executecommandsinbuffer:withrange:)*
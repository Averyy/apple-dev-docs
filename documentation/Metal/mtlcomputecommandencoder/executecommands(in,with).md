# executeCommands(in:with:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Encodes an instruction to run commands from an indirect buffer.

**Availability**:
- iOS 13.0+ - Deprecated in 14.0 (renamed: executeCommandsInBuffer)
- iPadOS 13.0+ - Deprecated in 14.0 (renamed: executeCommandsInBuffer)
- tvOS 13.0+ - Deprecated in 14.0 (renamed: executeCommandsInBuffer)
- visionOS

## Declaration

```swift
func executeCommands(in indirectCommandBuffer: any MTLIndirectCommandBuffer, with executionRange: NSRange)
```

## Parameters

- `indirectCommandBuffer`: The [`MTLIndirectCommandBuffer`](../mtlindirectcommandbuffer.md) instance containing the commands to execute.
- `executionRange`: The range of commands to execute. The maximum length of the range is `16384` commands.

## See Also

### Dispatching from indirect command buffers
- [func dispatchThreadgroups(indirectBuffer: any MTLBuffer, indirectBufferOffset: Int, threadsPerThreadgroup: MTLSize)](./dispatchthreadgroups%28indirectbuffer,indirectbufferoffset,threadsperthreadgroup%29.md)
  Encodes a dispatch call for a compute pass, using an indirect buffer that defines the size of a grid that aligns to threadgroup boundaries.
- [func executeCommandsInBuffer(any MTLIndirectCommandBuffer, range: Range<Int>)](./executecommandsinbuffer%28_,range%29.md)
  Encodes an instruction to run commands from an indirect buffer.
- [func executeCommandsInBuffer(any MTLIndirectCommandBuffer, indirectBuffer: any MTLBuffer, offset: Int)](./executecommandsinbuffer%28_,indirectbuffer,offset%29.md)
  Encodes an instruction to run commands from an indirect buffer, using another buffer to provide the command range.
- [func executeCommands(in: any MTLIndirectCommandBuffer, indirectBuffer: any MTLBuffer, indirectBufferOffset: Int)](./executecommands%28in,indirectbuffer,indirectbufferoffset%29.md)
  Encodes an instruction to run commands from an indirect buffer, using another buffer to provide the command range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/executecommands(in:with:))*
# executeCommands(in:indirectBuffer:indirectBufferOffset:)

**Framework**: Metal  
**Kind**: method

Encodes an instruction to run commands from an indirect buffer, using another buffer to provide the command range.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+
- visionOS ?+

## Declaration

```swift
func executeCommands(in indirectCommandbuffer: any MTLIndirectCommandBuffer, indirectBuffer indirectRangeBuffer: any MTLBuffer, indirectBufferOffset: Int)
```

## Parameters

- `indirectCommandbuffer`: The [`MTLIndirectCommandBuffer`](mtlindirectcommandbuffer.md) instance containing the commands to execute.
- `indirectRangeBuffer`: An indirect buffer containing the execution range, laid out in an [`MTLIndirectCommandBufferExecutionRange`](mtlindirectcommandbufferexecutionrange.md) instance. The maximum length of the range is `16384` commands.
- `indirectBufferOffset`: The number of bytes from the start of `indirectRangeBuffer` containing the execution range to use. Align the offset on a multiple of `4`.

## See Also

- [func dispatchThreadgroups(indirectBuffer: any MTLBuffer, indirectBufferOffset: Int, threadsPerThreadgroup: MTLSize)](mtlcomputecommandencoder/dispatchthreadgroups(indirectbuffer:indirectbufferoffset:threadsperthreadgroup:).md)
  Encodes a dispatch call for a compute pass, using an indirect buffer that defines the size of a grid that aligns to threadgroup boundaries.
- [func executeCommandsInBuffer(any MTLIndirectCommandBuffer, range: Range<Int>)](mtlcomputecommandencoder/executecommandsinbuffer(_:range:).md)
  Encodes an instruction to run commands from an indirect buffer.
- [func executeCommandsInBuffer(any MTLIndirectCommandBuffer, indirectBuffer: any MTLBuffer, offset: Int)](mtlcomputecommandencoder/executecommandsinbuffer(_:indirectbuffer:offset:).md)
  Encodes an instruction to run commands from an indirect buffer, using another buffer to provide the command range.
- [func executeCommands(in: any MTLIndirectCommandBuffer, with: NSRange)](mtlcomputecommandencoder/executecommands(in:with:).md)
  Encodes an instruction to run commands from an indirect buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/executecommands(in:indirectbuffer:indirectbufferoffset:))*
# executeCommands(in:with:)

**Framework**: Metal  
**Kind**: method

Encodes an instruction to run commands from an indirect buffer.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.11+
- tvOS 13.0+
- visionOS ?+

## Declaration

```swift
func executeCommands(in indirectCommandBuffer: any MTLIndirectCommandBuffer, with executionRange: NSRange)
```

## Parameters

- `indirectCommandBuffer`: The   instance containing the commands to execute.
- `executionRange`: The range of commands to execute. The maximum length of the range is   commands.

## See Also

- [func dispatchThreadgroups(indirectBuffer: any MTLBuffer, indirectBufferOffset: Int, threadsPerThreadgroup: MTLSize)](mtlcomputecommandencoder/dispatchthreadgroups(indirectbuffer:indirectbufferoffset:threadsperthreadgroup:).md)
  Encodes a dispatch call for a compute pass, using an indirect buffer that defines the size of a grid that aligns to threadgroup boundaries.
- [func executeCommandsInBuffer(any MTLIndirectCommandBuffer, range: Range<Int>)](mtlcomputecommandencoder/executecommandsinbuffer(_:range:).md)
  Encodes an instruction to run commands from an indirect buffer.
- [func executeCommandsInBuffer(any MTLIndirectCommandBuffer, indirectBuffer: any MTLBuffer, offset: Int)](mtlcomputecommandencoder/executecommandsinbuffer(_:indirectbuffer:offset:).md)
  Encodes an instruction to run commands from an indirect buffer, using another buffer to provide the command range.
- [func executeCommands(in: any MTLIndirectCommandBuffer, indirectBuffer: any MTLBuffer, indirectBufferOffset: Int)](mtlcomputecommandencoder/executecommands(in:indirectbuffer:indirectbufferoffset:).md)
  Encodes an instruction to run commands from an indirect buffer, using another buffer to provide the command range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/executecommands(in:with:))*
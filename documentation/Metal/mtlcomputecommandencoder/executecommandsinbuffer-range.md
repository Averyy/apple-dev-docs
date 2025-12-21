# executeCommandsInBuffer(_:range:)

**Framework**: Metal  
**Kind**: method

Encodes an instruction to run commands from an indirect buffer.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 13.0+
- visionOS ?+

## Declaration

```swift
func executeCommandsInBuffer(_ buffer: any MTLIndirectCommandBuffer, range: Range<Int>)
```

## Parameters

- `buffer`: The   instance containing the commands to execute.
- `range`: The range of commands to execute.   When running on Metal devices that belong to the   GPU family, the maximum length of the range is 0x4000 (16,384) commands.   Metal devices that belong to an Apple silicon family, such as  , don’t have this limitation.

## See Also

- [func dispatchThreadgroups(indirectBuffer: any MTLBuffer, indirectBufferOffset: Int, threadsPerThreadgroup: MTLSize)](mtlcomputecommandencoder/dispatchthreadgroups(indirectbuffer:indirectbufferoffset:threadsperthreadgroup:).md)
  Encodes a dispatch call for a compute pass, using an indirect buffer that defines the size of a grid that aligns to threadgroup boundaries.
- [func executeCommandsInBuffer(any MTLIndirectCommandBuffer, indirectBuffer: any MTLBuffer, offset: Int)](mtlcomputecommandencoder/executecommandsinbuffer(_:indirectbuffer:offset:).md)
  Encodes an instruction to run commands from an indirect buffer, using another buffer to provide the command range.
- [func executeCommands(in: any MTLIndirectCommandBuffer, indirectBuffer: any MTLBuffer, indirectBufferOffset: Int)](mtlcomputecommandencoder/executecommands(in:indirectbuffer:indirectbufferoffset:).md)
  Encodes an instruction to run commands from an indirect buffer, using another buffer to provide the command range.
- [func executeCommands(in: any MTLIndirectCommandBuffer, with: NSRange)](mtlcomputecommandencoder/executecommands(in:with:).md)
  Encodes an instruction to run commands from an indirect buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/executecommandsinbuffer(_:range:))*
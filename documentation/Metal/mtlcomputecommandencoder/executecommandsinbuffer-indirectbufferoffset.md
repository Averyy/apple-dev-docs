# executeCommandsInBuffer(_:indirectBuffer:offset:)

**Framework**: Metal  
**Kind**: method

Encodes an instruction to run commands from an indirect buffer, using another buffer to provide the command range.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 13.0+
- visionOS ?+

## Declaration

```swift
func executeCommandsInBuffer(_ buffer: any MTLIndirectCommandBuffer, indirectBuffer indirectRangeBuffer: any MTLBuffer, offset: Int)
```

## Parameters

- `buffer`: The   instance containing the commands to execute.
- `indirectRangeBuffer`: When running on Metal devices that belong to the   GPU family, the maximum value for the   property of that structure is 0x4000 (16,384).   Metal devices that belong to an Apple silicon family, such as  , don’t have this limitation.
- `offset`: The number of bytes from the start of   containing the execution range to use. Align the offset on a multiple of  .

## See Also

- [func dispatchThreadgroups(indirectBuffer: any MTLBuffer, indirectBufferOffset: Int, threadsPerThreadgroup: MTLSize)](mtlcomputecommandencoder/dispatchthreadgroups(indirectbuffer:indirectbufferoffset:threadsperthreadgroup:).md)
  Encodes a dispatch call for a compute pass, using an indirect buffer that defines the size of a grid that aligns to threadgroup boundaries.
- [func executeCommandsInBuffer(any MTLIndirectCommandBuffer, range: Range<Int>)](mtlcomputecommandencoder/executecommandsinbuffer(_:range:).md)
  Encodes an instruction to run commands from an indirect buffer.
- [func executeCommands(in: any MTLIndirectCommandBuffer, indirectBuffer: any MTLBuffer, indirectBufferOffset: Int)](mtlcomputecommandencoder/executecommands(in:indirectbuffer:indirectbufferoffset:).md)
  Encodes an instruction to run commands from an indirect buffer, using another buffer to provide the command range.
- [func executeCommands(in: any MTLIndirectCommandBuffer, with: NSRange)](mtlcomputecommandencoder/executecommands(in:with:).md)
  Encodes an instruction to run commands from an indirect buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/executecommandsinbuffer(_:indirectbuffer:offset:))*
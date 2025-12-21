# executeCommands(buffer:range:)

**Framework**: Metal  
**Kind**: method

Encodes a command to execute commands from an indirect command buffer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func executeCommands(buffer: any MTLIndirectCommandBuffer, range: Range<Int>)
```

## Parameters

- `buffer`: An   instance that contains other commands the current command runs.
- `range`: A span of integers that represent the command entries in buffer the current command runs.   The number of commands needs to be less than or equal to  .

## See Also

- [func executeCommands(buffer: any MTLIndirectCommandBuffer, indirectBuffer: MTLGPUAddress)](mtl4computecommandencoder/executecommands(buffer:indirectbuffer:).md)
  Encodes an instruction to execute commands from an indirect command buffer, using an indirect buffer for arguments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder/executecommands(buffer:range:))*
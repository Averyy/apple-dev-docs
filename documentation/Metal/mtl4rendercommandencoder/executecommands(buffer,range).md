# executeCommands(buffer:range:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Encodes a command that runs a range of commands from an indirect command buffer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func executeCommands(buffer: any MTLIndirectCommandBuffer, range: Range<Int>)
```

## Parameters

- `buffer`: An [`MTLIndirectCommandBuffer`](../mtlindirectcommandbuffer.md) instance that contains other commands the current command runs.
- `range`: A span of integers that represent the command entries in buffer the current command runs.

## See Also

### Running commands from indirect command buffers
- [func executeCommands(buffer: any MTLIndirectCommandBuffer, indirectBuffer: MTLGPUAddress)](./executecommands%28buffer,indirectbuffer%29.md)
  Encodes a command that runs an indirect range of commands from an indirect command buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/executecommands(buffer:range:))*
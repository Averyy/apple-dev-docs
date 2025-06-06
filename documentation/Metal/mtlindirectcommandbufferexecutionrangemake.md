# MTLIndirectCommandBufferExecutionRangeMake(_:_:)

**Framework**: Metal  
**Kind**: func

Creates a command execution range.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func MTLIndirectCommandBufferExecutionRangeMake(_ location: UInt32, _ length: UInt32) -> MTLIndirectCommandBufferExecutionRange
```

## Parameters

- `location`: The start index of the range.
- `length`: The number of items in the range.

## See Also

- [Creating an Indirect Command Buffer](creating-an-indirect-command-buffer.md)
  Configure a descriptor to specify the properties of an indirect command buffer.
- [Specifying Drawing and Dispatch Arguments Indirectly](specifying-drawing-and-dispatch-arguments-indirectly.md)
  Use indirect commands if you don’t know your draw or dispatch call arguments when you encode the command.
- [Encoding Indirect Command Buffers on the CPU](encoding-indirect-command-buffers-on-the-cpu.md)
  Reduce CPU overhead and simplify your command execution by reusing commands.
- [Encoding Indirect Command Buffers on the GPU](encoding-indirect-command-buffers-on-the-gpu.md)
  Maximize CPU to GPU parallelization by generating render commands on the GPU.
- [protocol MTLIndirectCommandBuffer](mtlindirectcommandbuffer.md)
  A command buffer containing reusable commands, encoded either on the CPU or GPU.
- [class MTLIndirectCommandBufferDescriptor](mtlindirectcommandbufferdescriptor.md)
  A configuration you create to customize an indirect command buffer.
- [struct MTLIndirectCommandType](mtlindirectcommandtype.md)
  The types of commands that you can encode into the indirect command buffer.
- [struct MTLIndirectCommandBufferExecutionRange](mtlindirectcommandbufferexecutionrange.md)
  A range of commands in an indirect command buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlindirectcommandbufferexecutionrangemake(_:_:))*
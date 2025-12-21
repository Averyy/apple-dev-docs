# MTLIndirectCommandBufferExecutionRange

**Framework**: Metal  
**Kind**: struct

A range of commands in an indirect command buffer.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
struct MTLIndirectCommandBufferExecutionRange
```

## Topics

### Creating a command execution range
- [init()](mtlindirectcommandbufferexecutionrange/init.md)
  Initializes an empty command execution range.
- [init(location: UInt32, length: UInt32)](mtlindirectcommandbufferexecutionrange/init(location:length:).md)
  Initializes an command execution range.
- [func MTLIndirectCommandBufferExecutionRangeMake(UInt32, UInt32) -> MTLIndirectCommandBufferExecutionRange](mtlindirectcommandbufferexecutionrangemake(_:_:).md)
  Creates a command execution range.
### Examining the range
- [var location: UInt32](mtlindirectcommandbufferexecutionrange/location.md)
  The first index in the command execution range.
- [var length: UInt32](mtlindirectcommandbufferexecutionrange/length.md)
  The number of items in the command execution range.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Creating an indirect command buffer](creating-an-indirect-command-buffer.md)
  Configure a descriptor to specify the properties of an indirect command buffer.
- [Specifying drawing and dispatch arguments indirectly](specifying-drawing-and-dispatch-arguments-indirectly.md)
  Use indirect commands if you don’t know your draw or dispatch call arguments when you encode the command.
- [Encoding indirect command buffers on the CPU](encoding-indirect-command-buffers-on-the-cpu.md)
  Reduce CPU overhead and simplify your command execution by reusing commands.
- [Encoding indirect command buffers on the GPU](encoding-indirect-command-buffers-on-the-gpu.md)
  Maximize CPU to GPU parallelization by generating render commands on the GPU.
- [protocol MTLIndirectCommandBuffer](mtlindirectcommandbuffer.md)
  A command buffer containing reusable commands, encoded either on the CPU or GPU.
- [class MTLIndirectCommandBufferDescriptor](mtlindirectcommandbufferdescriptor.md)
  A configuration you create to customize an indirect command buffer.
- [struct MTLIndirectCommandType](mtlindirectcommandtype.md)
  The types of commands that you can encode into the indirect command buffer.
- [func MTLIndirectCommandBufferExecutionRangeMake(UInt32, UInt32) -> MTLIndirectCommandBufferExecutionRange](mtlindirectcommandbufferexecutionrangemake(_:_:).md)
  Creates a command execution range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlindirectcommandbufferexecutionrange)*
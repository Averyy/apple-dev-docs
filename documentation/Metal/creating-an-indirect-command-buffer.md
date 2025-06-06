# Creating an Indirect Command Buffer

**Framework**: Metal

Configure a descriptor to specify the properties of an indirect command buffer.

#### Overview

An indirect command buffer stores encoded GPU commands persistently. Using an indirect command buffer, you can encode a command once and reuse it multiple times. You can also encode commands into an indirect command buffer simultaneously with multiple threads on the CPU or with a compute kernel on the GPU.

To create an indirect command buffer, first create a [`MTLIndirectCommandBufferDescriptor`](mtlindirectcommandbufferdescriptor.md) object and configure the descriptor’s properties. Then call [`makeIndirectCommandBuffer(descriptor:maxCommandCount:options:)`](mtldevice/makeindirectcommandbuffer(descriptor:maxcommandcount:options:).md) on a [`MTLDevice`](mtldevice.md) object to create the indirect command buffer.

## See Also

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
- [func MTLIndirectCommandBufferExecutionRangeMake(UInt32, UInt32) -> MTLIndirectCommandBufferExecutionRange](mtlindirectcommandbufferexecutionrangemake(_:_:).md)
  Creates a command execution range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/creating-an-indirect-command-buffer)*
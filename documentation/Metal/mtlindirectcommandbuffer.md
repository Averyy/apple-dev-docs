# MTLIndirectCommandBuffer

**Framework**: Metal  
**Kind**: protocol

A command buffer containing reusable commands, encoded either on the CPU or GPU.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
protocol MTLIndirectCommandBuffer : MTLResource
```

## Mentions

- [Improving CPU Performance by Using Argument Buffers](improving-cpu-performance-by-using-argument-buffers.md)

#### Overview

Use an indirect command buffer to encode commands once and reuse them, and to encode commands on multiple CPU or GPU threads.

Don’t implement this protocol yourself; instead, create a [`MTLIndirectCommandBufferDescriptor`](mtlindirectcommandbufferdescriptor.md) object, configure its properties, and tell the [`MTLDevice`](mtldevice.md) to create the indirect command buffer. See [`Creating an Indirect Command Buffer`](creating-an-indirect-command-buffer.md).

## Topics

### Determining the Maximum Number of Commands
- [var size: Int](mtlindirectcommandbuffer/size.md)
  The number of commands contained in the indirect command buffer.
### Retrieving Commands
- [func indirectRenderCommandAt(Int) -> any MTLIndirectRenderCommand](mtlindirectcommandbuffer/indirectrendercommandat(_:).md)
  Gets the render command at the given index.
- [func indirectComputeCommandAt(Int) -> any MTLIndirectComputeCommand](mtlindirectcommandbuffer/indirectcomputecommandat(_:).md)
  Gets the compute command at the given index.
- [func indirectComputeCommand(at: Int) -> any MTLIndirectComputeCommand](mtlindirectcommandbuffer/indirectcomputecommand(at:).md)
  Gets the compute command at the given index.
### Resetting Commands
- [func reset(Range<Int>)](mtlindirectcommandbuffer/reset(_:).md)
  Resets a range of commands to their default state.
### Instance Properties
- [var gpuResourceID: MTLResourceID](mtlindirectcommandbuffer/gpuresourceid.md)

## Relationships

### Inherits From
- [MTLAllocation](mtlallocation.md)
- [MTLResource](mtlresource.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Creating an Indirect Command Buffer](creating-an-indirect-command-buffer.md)
  Configure a descriptor to specify the properties of an indirect command buffer.
- [Specifying Drawing and Dispatch Arguments Indirectly](specifying-drawing-and-dispatch-arguments-indirectly.md)
  Use indirect commands if you don’t know your draw or dispatch call arguments when you encode the command.
- [Encoding Indirect Command Buffers on the CPU](encoding-indirect-command-buffers-on-the-cpu.md)
  Reduce CPU overhead and simplify your command execution by reusing commands.
- [Encoding Indirect Command Buffers on the GPU](encoding-indirect-command-buffers-on-the-gpu.md)
  Maximize CPU to GPU parallelization by generating render commands on the GPU.
- [class MTLIndirectCommandBufferDescriptor](mtlindirectcommandbufferdescriptor.md)
  A configuration you create to customize an indirect command buffer.
- [struct MTLIndirectCommandType](mtlindirectcommandtype.md)
  The types of commands that you can encode into the indirect command buffer.
- [struct MTLIndirectCommandBufferExecutionRange](mtlindirectcommandbufferexecutionrange.md)
  A range of commands in an indirect command buffer.
- [func MTLIndirectCommandBufferExecutionRangeMake(UInt32, UInt32) -> MTLIndirectCommandBufferExecutionRange](mtlindirectcommandbufferexecutionrangemake(_:_:).md)
  Creates a command execution range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlindirectcommandbuffer)*
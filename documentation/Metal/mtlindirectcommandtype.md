# MTLIndirectCommandType

**Framework**: Metal  
**Kind**: struct

The types of commands that you can encode into the indirect command buffer.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
struct MTLIndirectCommandType
```

## Topics

### Creating a Set of Command Types
- [init(rawValue: UInt)](mtlindirectcommandtype/init(rawvalue:).md)
  Initializes the set of command types from a raw integer value.
### Specifying Command Types
- [static var draw: MTLIndirectCommandType](mtlindirectcommandtype/draw.md)
  A draw call command.
- [static var drawIndexed: MTLIndirectCommandType](mtlindirectcommandtype/drawindexed.md)
  An indexed draw call command.
- [static var drawPatches: MTLIndirectCommandType](mtlindirectcommandtype/drawpatches.md)
  A draw call command for tessellated patches.
- [static var drawIndexedPatches: MTLIndirectCommandType](mtlindirectcommandtype/drawindexedpatches.md)
  An indexed draw call command for tessellated patches.
- [static var concurrentDispatch: MTLIndirectCommandType](mtlindirectcommandtype/concurrentdispatch.md)
  A compute command using a grid aligned to threadgroup boundaries.
- [static var concurrentDispatchThreads: MTLIndirectCommandType](mtlindirectcommandtype/concurrentdispatchthreads.md)
  A compute command using an arbitrarily sized grid.
### Type Properties
- [static var drawMeshThreadgroups: MTLIndirectCommandType](mtlindirectcommandtype/drawmeshthreadgroups.md)
- [static var drawMeshThreads: MTLIndirectCommandType](mtlindirectcommandtype/drawmeshthreads.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

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
- [struct MTLIndirectCommandBufferExecutionRange](mtlindirectcommandbufferexecutionrange.md)
  A range of commands in an indirect command buffer.
- [func MTLIndirectCommandBufferExecutionRangeMake(UInt32, UInt32) -> MTLIndirectCommandBufferExecutionRange](mtlindirectcommandbufferexecutionrangemake(_:_:).md)
  Creates a command execution range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlindirectcommandtype)*
# MTLIndirectCommandBufferDescriptor

**Framework**: Metal  
**Kind**: class

A configuration you create to customize an indirect command buffer.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
class MTLIndirectCommandBufferDescriptor
```

## Mentions

- [Creating an Indirect Command Buffer](creating-an-indirect-command-buffer.md)

## Topics

### Declaring Command Types to Encode
- [var commandTypes: MTLIndirectCommandType](mtlindirectcommandbufferdescriptor/commandtypes.md)
  The set of command types that you can encode into the indirect command buffer.
### Declaring Command Inheritance
- [var inheritBuffers: Bool](mtlindirectcommandbufferdescriptor/inheritbuffers.md)
  A Boolean value that determines where commands in the indirect command buffer get their buffer arguments from when you execute them.
- [var inheritPipelineState: Bool](mtlindirectcommandbufferdescriptor/inheritpipelinestate.md)
  A Boolean value that determines where commands in the indirect command buffer get their pipeline state from when you execute them.
### Declaring the Maximum Number of Argument Buffers Per Command
- [var maxVertexBufferBindCount: Int](mtlindirectcommandbufferdescriptor/maxvertexbufferbindcount.md)
  The maximum number of buffers that you can set per command for the vertex stage.
- [var maxFragmentBufferBindCount: Int](mtlindirectcommandbufferdescriptor/maxfragmentbufferbindcount.md)
  The maximum number of buffers that you can set per command for the fragment stage.
- [var maxKernelBufferBindCount: Int](mtlindirectcommandbufferdescriptor/maxkernelbufferbindcount.md)
  The maximum number of buffers that you can set per command for the compute kernel.
### Instance Properties
- [var maxKernelThreadgroupMemoryBindCount: Int](mtlindirectcommandbufferdescriptor/maxkernelthreadgroupmemorybindcount.md)
- [var maxMeshBufferBindCount: Int](mtlindirectcommandbufferdescriptor/maxmeshbufferbindcount.md)
- [var maxObjectBufferBindCount: Int](mtlindirectcommandbufferdescriptor/maxobjectbufferbindcount.md)
- [var maxObjectThreadgroupMemoryBindCount: Int](mtlindirectcommandbufferdescriptor/maxobjectthreadgroupmemorybindcount.md)
- [var supportColorAttachmentMapping: Bool](mtlindirectcommandbufferdescriptor/supportcolorattachmentmapping.md)
  Specifies if the indirect command buffer should support color attachment mapping.
- [var supportDynamicAttributeStride: Bool](mtlindirectcommandbufferdescriptor/supportdynamicattributestride.md)
- [var supportRayTracing: Bool](mtlindirectcommandbufferdescriptor/supportraytracing.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
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
- [protocol MTLIndirectCommandBuffer](mtlindirectcommandbuffer.md)
  A command buffer containing reusable commands, encoded either on the CPU or GPU.
- [struct MTLIndirectCommandType](mtlindirectcommandtype.md)
  The types of commands that you can encode into the indirect command buffer.
- [struct MTLIndirectCommandBufferExecutionRange](mtlindirectcommandbufferexecutionrange.md)
  A range of commands in an indirect command buffer.
- [func MTLIndirectCommandBufferExecutionRangeMake(UInt32, UInt32) -> MTLIndirectCommandBufferExecutionRange](mtlindirectcommandbufferexecutionrangemake(_:_:).md)
  Creates a command execution range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlindirectcommandbufferdescriptor)*
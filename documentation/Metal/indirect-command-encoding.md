# Indirect Command Encoding

**Framework**: Metal

Store draw commands in Metal buffers and run them at a later time on the GPU, either once or repeatedly.

#### Overview

You can use an [`MTLIndirectCommandBuffer`](mtlindirectcommandbuffer.md) instance to store draw commands and invoke them at a later time. Metal executes all the draw commands in an indirect command buffer each time you submit it. This means you can use indirect command buffers multiple times, unlike [`MTLCommandBuffer`](mtlcommandbuffer.md) instances, which are all single-use.

You can encode an indirect command buffer to run on either the CPU or the GPU. However, the GPU gives you the ability to immediately use the output of one pass as the input of a subsequent pass. For example, you can create an indirect command buffer with commands that conditionally draw visible items by running:

1. A compute kernel that identifies visible geometry and saves it to a result buffer
2. An indirect command buffer that uses the result buffer as its input to make decisions on what to draw

## Topics

### Indirect Command Buffers
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
- [func MTLIndirectCommandBufferExecutionRangeMake(UInt32, UInt32) -> MTLIndirectCommandBufferExecutionRange](mtlindirectcommandbufferexecutionrangemake(_:_:).md)
  Creates a command execution range.
### Indirect Compute Commands
- [protocol MTLIndirectComputeCommand](mtlindirectcomputecommand.md)
  A compute command in an indirect command buffer.
- [struct MTLRegion](mtlregion.md)
  The bounds for a subset of an object’s elements.
- [struct MTLSize](mtlsize.md)
  The dimensions of an object.
- [struct MTLOrigin](mtlorigin.md)
  The coordinates for the front upper-left corner of a region.
- [struct MTLStageInRegionIndirectArguments](mtlstageinregionindirectarguments.md)
  The data layout required for the arguments needed to specify the stage-in region.
- [struct MTLDispatchThreadgroupsIndirectArguments](mtldispatchthreadgroupsindirectarguments.md)
  The data layout required for arguments needed to specify the size of threadgroups.
### Render Compute Commands
- [protocol MTLIndirectRenderCommand](mtlindirectrendercommand.md)
  A render command in an indirect command buffer.
- [struct MTLDrawPatchIndirectArguments](mtldrawpatchindirectarguments.md)
  The data layout required for drawing patches via indirect buffer calls.
- [struct MTLDrawPrimitivesIndirectArguments](mtldrawprimitivesindirectarguments.md)
  The data layout required for drawing primitives via indirect buffer calls.
- [struct MTLDrawIndexedPrimitivesIndirectArguments](mtldrawindexedprimitivesindirectarguments.md)
  The data layout required for drawing indexed primitives via indirect buffer calls.

## See Also

- [Render Passes](render-passes.md)
  Encode a render pass to draw graphics into an image.
- [Compute Passes](compute-passes.md)
  Encode a compute pass that runs computations in parallel on a thread grid, processing and manipulating Metal resource data on multiple cores of a GPU.
- [Blit Passes](blit-passes.md)
  Encode a block information transfer pass to adjust and copy data to and from GPU resources, such as buffers and textures.
- [Ray Tracing with Acceleration Structures](ray-tracing-with-acceleration-structures.md)
  Build a representation of your scene’s geometry using triangles and bounding volumes to quickly trace rays through the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/indirect-command-encoding)*
# Encoding indirect command buffers on the CPU

**Framework**: Metal

Reduce CPU overhead and simplify your command execution by reusing commands.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+
- macOS 10.14+
- Xcode 12.3+

#### Overview

This sample app provides an introduction to  (ICB), which enable you to store repeated commands for later use. Because Metal discards a normal command buffer and its commands after Metal executes them, use ICBs to save expensive allocation, deallocation, and encoding time for your app’s common instructions. Additionally, you benefit when using ICBs with:

- A reduction in rendering tasks because you execute an ICB with a single call.
- By creating ICBs at initialization, it moves expensive command management out of your app’s critical path at rendering or compute-time.

An example of where ICBs are effective is with a game’s head-up display (HUD), because:

- You render HUDs every frame.
- The appearance of the HUD is usually static across frames.

ICBs are also useful to render static objects in typical 3D scenes. Because encoded commands typically result in lightweight data structures, ICBs are suitable for saving complex draws, too.

This sample demonstrates how to set up an ICB to repeatedly render a series of shapes. While it’s possible to gain even more instruction-parallelism by encoding the ICB on the GPU, this sample encodes an ICB on the CPU for simplicity. See [`Encoding indirect command buffers on the GPU`](encoding-indirect-command-buffers-on-the-gpu.md) for the more advanced usage.

##### Getting Started

This sample contains macOS and iOS targets. Run the iOS scheme on a physical device because Metal isn’t supported in the simulator.

ICBs are supported by GPUs of family greater than or equal to:

- `MTLFeatureSet_iOS_GPUFamily3_v4`
- `MTLFeatureSet_macOS_GPUFamily2_v1`

You check the GPU that you choose at runtime if it supports ICBs using the [`MTLDevice`](mtldevice.md) method [`supportsFeatureSet(_:)`](mtldevice/supportsfeatureset(_:).md):

This sample calls ‘supportsFeatureSet:’ for this purpose within its view controller’s `viewDidLoad:` callback.

##### Individual Commands Versus Indirect Command Buffers

Metal apps, particularly games, typically contain multiple render commands, each associated with a set of render states, buffers, and draw calls. To execute these commands for a render pass, apps first encode them into a render command encoder within a command buffer.

You encode individual commands into a render command encoder by calling [`MTLRenderCommandEncoder`](mtlrendercommandencoder.md) methods such as [`setVertexBuffer(_:offset:index:)`](mtlrendercommandencoder/setvertexbuffer(_:offset:index:).md) or [`drawPrimitives(type:vertexStart:vertexCount:instanceCount:baseInstance:)`](mtlrendercommandencoder/drawprimitives(type:vertexstart:vertexcount:instancecount:baseinstance:).md).

![Layout diagram that shows render commands encoded individually.](https://docs-assets.developer.apple.com/published/5dc1c3a9c161dbf526c493cd27c255f9/icbs-with-cpu-encoding-1-IndividualCommands.png)

Recreating draws that were equivalent to ones you did in a previous queue can be tedious from a coding perspective and non-performant at runtime. Instead, move your repeated draws and their data buffers into an [`MTLIndirectCommandBuffer`](mtlindirectcommandbuffer.md) instance using an [`MTLIndirectRenderCommand`](mtlindirectrendercommand.md), thereby filling the ICB with commands. When you’re ready to use the ICB, encode individual executions of it by calling an `MTLRenderCommandEncoder` instance’s [`executeCommandsInBuffer:withRange:`](mtlrendercommandencoder/executecommandsinbuffer:withrange:.md) method.

![Layout diagram that shows render commands encoded as grouped commands within an indirect command buffer, which is encoded as an individual command.](https://docs-assets.developer.apple.com/published/94b74ea8f716d9d364157fec02c459a1/icbs-with-cpu-encoding-2-IndirectCommandBuffers.png)

> **Note**: To access individual buffers referenced by an indirect command buffer, you need to call the `useResource:usage:` method for each buffer that you want to use. For more information, see the “Execute an Indirect Command Buffer” section.

##### Define Render Commands and Inherited Render State

For the indirect command buffer, `_indirectCommandBuffer`, the sample defines render commands that:

1. Set a vertex buffer using unique vertex data for each mesh
2. Set another vertex buffer using common transformation data for all meshes
3. Set another vertex buffer containing an array of parameters for each mesh
4. Draw the mesh’s triangles

The sample encodes these commands differently for the CPU or the GPU. However, these commands are still encoded into both versions of the indirect command buffer.

The sample also allows `_indirectCommandBuffer` to inherit the render pipeline state from its parent encoder, `renderEncoder`. Furthermore, `_indirectCommandBuffer` implicitly inherits any render state that can’t be encoded into it, such as the cull mode and depth or stencil state for the render pass.

##### Create an Indirect Command Buffer

The sample creates `_indirectCommandBuffer` from an [`MTLIndirectCommandBufferDescriptor`](mtlindirectcommandbufferdescriptor.md), which defines the features and limits of an indirect command buffer.

The sample specifies the types of commands, `commandTypes`, and the maximum number of commands, `maxCount`, so that Metal reserves enough space in memory for the sample to encode `_indirectCommandBuffer` successfully (with the CPU or GPU).

##### Encode an Indirect Command Buffer with the Cpu

From the CPU, the sample encodes commands into `_indirectCommandBuffer` with an [`MTLIndirectRenderCommand`](mtlindirectrendercommand.md) instance. For each shape to be rendered, the sample encodes two [`setVertexBuffer(_:offset:at:)`](mtlindirectrendercommand/setvertexbuffer(_:offset:at:).md) commands and one [`drawPrimitives(_:vertexStart:vertexCount:instanceCount:baseInstance:)`](mtlindirectrendercommand/drawprimitives(_:vertexstart:vertexcount:instancecount:baseinstance:).md) command.

The sample performs this encoding only once, before encoding any subsequent render commands. `_indirectCommandBuffer` contains a total of 16 draw calls, one for each shape to be rendered. Each draw call references the same transformation data, `_uniformBuffers`, but different vertex data, `_vertexBuffers[indx]`. Although the CPU encodes data only once, the sample issues 16 draw calls per frame.

![Layout diagram that shows the commands encoded into an indirect command buffer with the CPU.](https://docs-assets.developer.apple.com/published/6fe3613067edf5429d368f7904d4ae20/icbs-with-cpu-encoding-3-IndirectCommandBufferCPUEncoding.png)

##### Update the Data Used By an Icb

To update data that’s fed to the GPU, you typically cycle through a set of buffers such that the CPU updates one while the GPU reads another (see [`Synchronizing events between a GPU and the CPU`](synchronizing-events-between-a-gpu-and-the-cpu.md)). You can’t apply that pattern literally with ICBs, however, because you can’t update an ICB’s buffer set after you encode its commands, but you follow a two-step process to blit data updates from the CPU. First, update a single buffer in your dynamic buffer array on the CPU:

Then, blit the CPU-side buffer set to the location that’s accessible to the ICB (see `_indirectFrameStateBuffer`):

##### Execute an Indirect Command Buffer

The sample calls the `executeCommandsInBuffer:withRange:` method to execute the commands in `_indirectCommandBuffer`.

Similar to the arguments in an argument buffer, the sample calls the `useResource:usage:` method to indicate that the GPU can access the resources within an indirect command buffer.

The sample continues to execute `_indirectCommandBuffer` each frame.

## See Also

- [Creating an indirect command buffer](creating-an-indirect-command-buffer.md)
  Configure a descriptor to specify the properties of an indirect command buffer.
- [Specifying drawing and dispatch arguments indirectly](specifying-drawing-and-dispatch-arguments-indirectly.md)
  Use indirect commands if you don’t know your draw or dispatch call arguments when you encode the command.
- [Encoding indirect command buffers on the GPU](encoding-indirect-command-buffers-on-the-gpu.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/metal/encoding-indirect-command-buffers-on-the-cpu)*
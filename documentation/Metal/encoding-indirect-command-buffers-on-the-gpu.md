# Encoding indirect command buffers on the GPU

**Framework**: Metal

Maximize CPU to GPU parallelization by generating render commands on the GPU.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+
- macOS 10.14+
- Xcode 12.3+

#### Overview

This sample app demonstrates how to use  (ICB) to issue rendering instructions from the GPU. When you have a rendering algorithm that runs in a compute kernel, use ICBs to generate draw calls based on your algorithm’s results. The sample app uses a compute kernel to remove invisible objects submitted for rendering, and generates draw commands only for the objects currently visible in the scene.

![Flow chart of an algorithm and its dependent rendering instructions executing on the GPU. At left, a body representing the CPU dispatches the algorithm to the GPU via compute kernel. A line flows from the left body to another body, at center representing the GPU, which executes the compute kernel and generates its dependent rendering commands using an ICB. A line flows from the center body to a body at right, also representing the GPU, which executes the rendering commands.](https://docs-assets.developer.apple.com/published/28f04960640b40e69469ea9294b3cd5f/icbs-with-gpu-encoding-1-GpuDrivenPipeline.png)

Without ICBs, you can’t submit rendering commands on the GPU. Instead, the CPU waits for your compute kernel’s results before generating the render commands. Then, the GPU waits for the rendering commands to make it across the CPU to GPU bridge. The following diagram shows how this creates a slower round trip:

![Flow chart of an algorithm being parallelized on the GPU with the CPU waiting on its results.](https://docs-assets.developer.apple.com/published/98a58b36c689a56c07a8588158bc6b88/icbs-with-gpu-encoding-2-CpuRoundTrip.png)

The sample code project, [`Encoding indirect command buffers on the CPU`](encoding-indirect-command-buffers-on-the-cpu.md) introduces ICBs by creating a single ICB to reuse its commands every frame. While the former sample saved expensive command-encoding time by reusing commands, this sample uses ICBs to effect a GPU-driven rendering pipeline.

The techniques shown by this sample include issuing draw calls from the GPU, and the process of executing a select set of draws.

##### Getting Started

This project contains targets for macOS and iOS. Run the iOS scheme on a physical device because Metal isn’t supported in the simulator.

The sample calls an [`MTLComputeCommandEncoder`](mtlcomputecommandencoder.md) instances’s
[`dispatchThreads(_:threadsPerThreadgroup:)`](mtlcomputecommandencoder/dispatchthreads(_:threadsperthreadgroup:).md) method, which is available to a GPU that supports the following feature sets and later:

- MTLFeatureSet_iOS_GPUFamily4_v2
- MTLFeatureSet_macOS_GPUFamily2_v1

##### Define the Data Read By the Icb

In an ideal scenario, you store each mesh in its own buffer. However, on iOS, kernels running on the GPU can only access a limited number of data buffers per execution. To reduce the number of buffers needed during the ICBs execution, you pack all meshes into a single buffer at varying offsets. Then, use another buffer to store the offset and size of each mesh. The process to do this follows.

At initialization, create the data for each mesh:

Count the individual and accumulated mesh sizes and create the container buffer:

Finally, insert each mesh into the container buffer while noting its offset and size in the second buffer:

##### Update the Data Read By the Icb Dynamically

By culling non-visible vertices from the data fed to the rendering pipeline, you save significant rendering time and effort. To do that, use the same compute kernel that encodes the ICB’s commands to continually update the ICB’s data buffers:

The parallel nature of the GPU partitions the compute task for you, resulting in multiple offscreen meshes getting culled concurrently.

##### Pass an Icb to a Compute Kernel Using an Argument Buffer

To get an ICB on the GPU and make it accessible to a compute kernel, you pass it through an argument buffer, as follows:

Define the container argument buffer as a structure that contains one member, the ICB:

Encode the ICB into the argument buffer:

Pass the ICB (`_indirectCommandBuffer`) to the kernel by setting the argument buffer on the kernel’s compute command encoder:

Because you pass the ICB through an argument buffer, standard argument buffer rules apply. Call `useResource` on the ICB to tell Metal to prepare its use:

##### Encode and Optimize Icb Commands

Reset the ICB’s commands to their initial before beginning encoding:

Encode the ICB’s commands by dispatching the compute kernel:

Optimize your ICB commands to remove empty commands or redundant state by calling `optimizeIndirectCommandBuffer:withRange:`:

This sample optimizes ICB commands because redundant state results from the kernel setting a buffer for each draw, and encoding empty commands for each invisible object. By removing the empty commands, you can free up a significant number of blank spaces in the command buffer that Metal otherwise spends time skipping at runtime.

> **Note**: If you optimize an indirect command buffer, you won’t be able to call `executeCommandsInBuffer:withRange:` with a range that starts in the optimized region. Instead, specify a range staring at the beginning and finishing within or at the end of the optimized region.

##### Execute the Icb

Draw the onscreen meshes by calling `executeCommandsInBuffer` on your render command encoder:

While you can encode an ICB’s commands in a compute kernel, you call `executeCommandsInBuffer` from your host app to encode a single command that contains all of the commands encoded by the compute kernel. By doing this, you choose the queue and buffer that the ICB’s commands go into. When you call `executeIndirectCommandBuffer` determines the placement of the ICB’s commands among any other commands you may also encode in the same buffer.

## See Also

- [Creating an indirect command buffer](creating-an-indirect-command-buffer.md)
  Configure a descriptor to specify the properties of an indirect command buffer.
- [Specifying drawing and dispatch arguments indirectly](specifying-drawing-and-dispatch-arguments-indirectly.md)
  Use indirect commands if you don’t know your draw or dispatch call arguments when you encode the command.
- [Encoding indirect command buffers on the CPU](encoding-indirect-command-buffers-on-the-cpu.md)
  Reduce CPU overhead and simplify your command execution by reusing commands.
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

*[View on Apple Developer](https://developer.apple.com/documentation/metal/encoding-indirect-command-buffers-on-the-gpu)*
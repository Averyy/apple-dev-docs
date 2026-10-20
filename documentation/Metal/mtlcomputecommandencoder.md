# MTLComputeCommandEncoder

**Framework**: Metal  
**Kind**: protocol  
**Role**: Protocol

Encodes computation dispatch commands for a single compute pass into a command buffer.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
protocol MTLComputeCommandEncoder : MTLCommandEncoder
```

```objc
@protocol MTLComputeCommandEncoder <MTLCommandEncoder>
```

## Mentions

- [Understanding the Metal 4 core API](./understanding-the-metal-4-core-api.md)
- [Improving CPU performance by using argument buffers](./improving-cpu-performance-by-using-argument-buffers.md)
- [Sampling GPU data into counter sample buffers](./sampling-gpu-data-into-counter-sample-buffers.md)
- [Setting up a command structure](./setting-up-a-command-structure.md)
- [Simplifying GPU resource management with residency sets](./simplifying-gpu-resource-management-with-residency-sets.md)
- [Tracking the resource residency of argument buffers](./tracking-the-resource-residency-of-argument-buffers.md)

#### Overview

Create a compute encoder by calling one of the factory methods on an [`MTLCommandBuffer`](./mtlcommandbuffer.md) instance, such as [`makeComputeCommandEncoder(dispatchType:)`](./mtlcommandbuffer/makecomputecommandencoder%28dispatchtype%29.md). You can encode multiple commands that each run a compute kernel as part of a single pass of the encoder with the following steps:

1. Configure an [`MTLComputePipelineState`](./mtlcomputepipelinestate.md) instance with a kernel, using a method such as [`makeComputePipelineState(function:)`](./mtldevice/makecomputepipelinestate%28function%29.md). See the [Creating compute pipeline states](./pipeline-state-creation.md#Creating-compute-pipeline-states) section of [Pipeline state creation](./pipeline-state-creation.md) for all [`MTLDevice`](./mtldevice.md) methods that create a new pipeline state for your command encoder.
2. Set the pipeline state with the [`setComputePipelineState(_:)`](./mtlcomputecommandencoder/setcomputepipelinestate%28_%29.md) method on your command encoder.
3. Set kernel arguments by binding buffers, textures, and other resources with methods such as [`setBuffer(_:offset:index:)`](./mtlcomputecommandencoder/setbuffer%28_,offset,index%29.md) and [`setTexture(_:index:)`](./mtlcomputecommandencoder/settexture%28_,index%29.md).
4. Encode compute commands that call your kernel by either [Dispatching kernel calls directly](./mtlcomputecommandencoder.md#Dispatching-kernel-calls-directly) or [Dispatching from indirect command buffers](./mtlcomputecommandencoder.md#Dispatching-from-indirect-command-buffers).
5. Call [`endEncoding()`](./mtlcommandencoder/endencoding%28%29.md) to finish encoding the kernel call of the compute pass.

##### Command stages

Most compute commands apply to one stage within a pass. The following table shows which stage applies to each command:

| Function | MTLStages |
| --- | --- |
| [`dispatchThreads(_:threadsPerThreadgroup:)`](./mtlcomputecommandencoder/dispatchthreads%28_,threadsperthreadgroup%29.md) | [`dispatch`](./mtlstages/dispatch.md) |
| [`dispatchThreadgroups(_:threadsPerThreadgroup:)`](./mtlcomputecommandencoder/dispatchthreadgroups%28_,threadsperthreadgroup%29.md) | [`dispatch`](./mtlstages/dispatch.md) |
| [`dispatchThreadgroups(indirectBuffer:indirectBufferOffset:threadsPerThreadgroup:)`](./mtlcomputecommandencoder/dispatchthreadgroups%28indirectbuffer,indirectbufferoffset,threadsperthreadgroup%29.md) | [`dispatch`](./mtlstages/dispatch.md) |
| [`executeCommandsInBuffer(_:range:)`](./mtlcomputecommandencoder/executecommandsinbuffer%28_,range%29.md)![](https://developer.apple.com/tutorials/images/com.apple.metal/spacer.png)[`executeCommandsInBuffer:withRange:`](./mtlcomputecommandencoder/executecommandsinbuffer_withrange_.md) | None |
| [`executeCommandsInBuffer(_:indirectBuffer:offset:)`](./mtlcomputecommandencoder/executecommandsinbuffer%28_,indirectbuffer,offset%29.md)![](https://developer.apple.com/tutorials/images/com.apple.metal/spacer.png)[`executeCommandsInBuffer:indirectBuffer:indirectBufferOffset:`](./mtlcomputecommandencoder/executecommandsinbuffer_indirectbuffer_indirectbufferoffset_.md) | None |
| [`sampleCounters(sampleBuffer:sampleIndex:barrier:)`](./mtlcomputecommandencoder/samplecounters%28samplebuffer,sampleindex,barrier%29.md) | None |

The [`executeCommandsInBuffer(_:range:)`](./mtlcomputecommandencoder/executecommandsinbuffer%28_,range%29.md) and [`executeCommandsInBuffer(_:indirectBuffer:offset:)`](./mtlcomputecommandencoder/executecommandsinbuffer%28_,indirectbuffer,offset%29.md) commands don’t apply to any stage, which means you can’t use a barrier to wait for all commands in an indirect command buffer to complete. However, each command within the [`MTLIndirectCommandBuffer`](./mtlindirectcommandbuffer.md) applies to the same stages as when you encode the equivalent command directly.

For more information about stages and synchronization, see [`MTLStages`](./mtlstages.md) and [Resource synchronization](./resource-synchronization.md).

## Topics

### Configuring the pipeline state
- [func setComputePipelineState(any MTLComputePipelineState)](./mtlcomputecommandencoder/setcomputepipelinestate%28_%29.md)
  Configures the compute encoder with a pipeline state for subsequent kernel calls.
- [var dispatchType: MTLDispatchType](./mtlcomputecommandencoder/dispatchtype.md)
  The dispatch type to use when submitting compute work to the GPU.
### Binding buffers
- [func setBuffer((any MTLBuffer)?, offset: Int, index: Int)](./mtlcomputecommandencoder/setbuffer%28_,offset,index%29.md)
  Binds a buffer to the buffer argument table, allowing compute kernels to access its data on the GPU.
- [func setBuffer(any MTLBuffer, offset: Int, attributeStride: Int, index: Int)](./mtlcomputecommandencoder/setbuffer%28_,offset,attributestride,index%29.md)
  Binds a buffer with a stride to the buffer argument table, allowing compute kernels to access its data on the GPU.
- [func setBuffers([(any MTLBuffer)?], offsets: [Int], range: Range<Int>)](./mtlcomputecommandencoder/setbuffers%28_,offsets,range%29.md)
  Binds multiple buffers to the buffer argument table at once, allowing compute kernels to access their data on the GPU.
- [func setBuffers([(any MTLBuffer)?], offsets: [Int], attributeStrides: [Int], range: Range<Int>)](./mtlcomputecommandencoder/setbuffers%28_,offsets,attributestrides,range%29.md)
  Binds multiple buffers with data in stride to the buffer argument table at once, allowing compute kernels to access their data on the GPU.
- [func setBufferOffset(Int, index: Int)](./mtlcomputecommandencoder/setbufferoffset%28_,index%29.md)
  Changes where the data begins in a buffer already bound to the buffer argument table.
- [func setBufferOffset(offset: Int, attributeStride: Int, index: Int)](./mtlcomputecommandencoder/setbufferoffset%28offset,attributestride,index%29.md)
  Changes where the data begins and the distance between adjacent elements in a buffer already bound to the buffer argument table.
### Binding raw bytes
- [func setBytes(UnsafeRawPointer, length: Int, index: Int)](./mtlcomputecommandencoder/setbytes%28_,length,index%29.md)
  Copies data directly to the GPU to populate an entry in the buffer argument table.
- [func setBytes(UnsafeRawPointer, length: Int, attributeStride: Int, index: Int)](./mtlcomputecommandencoder/setbytes%28_,length,attributestride,index%29.md)
  Copies data with a given stride directly to the GPU to populate an entry in the buffer argument table.
### Binding textures
- [func setTexture((any MTLTexture)?, index: Int)](./mtlcomputecommandencoder/settexture%28_,index%29.md)
  Binds a texture to the texture argument table, allowing compute kernels to access its data on the GPU.
- [func setTextures([(any MTLTexture)?], range: Range<Int>)](./mtlcomputecommandencoder/settextures%28_,range%29.md)
  Binds multiple textures to the texture argument table, allowing compute functions to access their data on the GPU.
### Binding texture samplers
- [func setSamplerState((any MTLSamplerState)?, index: Int)](./mtlcomputecommandencoder/setsamplerstate%28_,index%29.md)
  Encodes a texture sampler, allowing compute kernels to use it for sampling textures on the GPU.
- [func setSamplerState((any MTLSamplerState)?, lodMinClamp: Float, lodMaxClamp: Float, index: Int)](./mtlcomputecommandencoder/setsamplerstate%28_,lodminclamp,lodmaxclamp,index%29.md)
  Encodes a texture sampler with a custom level of detail clamping, allowing compute kernels to use it for sampling textures on the GPU.
- [func setSamplerStates([(any MTLSamplerState)?], range: Range<Int>)](./mtlcomputecommandencoder/setsamplerstates%28_,range%29.md)
  Encodes multiple texture samplers to the sampler argument table, allowing compute kernels to use them for sampling textures on the GPU.
- [func setSamplerStates([(any MTLSamplerState)?], lodMinClamps: [Float], lodMaxClamps: [Float], range: Range<Int>)](./mtlcomputecommandencoder/setsamplerstates%28_,lodminclamps,lodmaxclamps,range%29.md)
  Encodes multiple texture samplers for the compute function, specifying clamp values for the level of detail of each sampler.
### Binding function tables
- [func setVisibleFunctionTable((any MTLVisibleFunctionTable)?, bufferIndex: Int)](./mtlcomputecommandencoder/setvisiblefunctiontable%28_,bufferindex%29.md)
  Binds a visible function table to the buffer argument table, allowing you to call its functions on the GPU.
- [func setVisibleFunctionTables([(any MTLVisibleFunctionTable)?], bufferRange: Range<Int>)](./mtlcomputecommandencoder/setvisiblefunctiontables%28_,bufferrange%29.md)
  Binds multiple visible function tables to the buffer argument table, allowing you to call their functions on the GPU.
- [func setIntersectionFunctionTables([(any MTLIntersectionFunctionTable)?], bufferRange: Range<Int>)](./mtlcomputecommandencoder/setintersectionfunctiontables%28_,bufferrange%29.md)
  Binds multiple intersection function tables to the buffer argument table, allowing you to call their functions on the GPU.
### Binding arguments for acceleration structures
- [func setAccelerationStructure((any MTLAccelerationStructure)?, bufferIndex: Int)](./mtlcomputecommandencoder/setaccelerationstructure%28_,bufferindex%29.md)
  Binds an acceleration structure to the buffer argument table, allowing functions to access it on the GPU.
- [func setIntersectionFunctionTable((any MTLIntersectionFunctionTable)?, bufferIndex: Int)](./mtlcomputecommandencoder/setintersectionfunctiontable%28_,bufferindex%29.md)
  Binds an intersection function table to the buffer argument table, making it callable in your Metal shaders.
### Making indirect resources resident
- [func useResource(any MTLResource, usage: MTLResourceUsage)](./mtlcomputecommandencoder/useresource%28_,usage%29.md)
  Ensures kernel calls that the system encodes in subsequent commands have access to a resource.
- [func useResources([any MTLResource], usage: MTLResourceUsage)](./mtlcomputecommandencoder/useresources%28_,usage%29.md)
  Ensures kernel calls that the system encodes in subsequent commands have access to multiple resources.
- [func useHeap(any MTLHeap)](./mtlcomputecommandencoder/useheap%28_%29.md)
  Ensures the shaders in the render pass’s subsequent draw commands have access to all of the resources you allocate from a heap.
- [func useHeaps([any MTLHeap])](./mtlcomputecommandencoder/useheaps%28_%29.md)
  Ensures the shaders in the render pass’s subsequent draw commands have access to all of the resources you allocate from multiple heaps.
### Configuring tile memory
- [func setThreadgroupMemoryLength(Int, index: Int)](./mtlcomputecommandencoder/setthreadgroupmemorylength%28_,index%29.md)
  Configures the size of a block of threadgroup memory.
- [func setImageblockWidth(Int, height: Int)](./mtlcomputecommandencoder/setimageblockwidth%28_,height%29.md)
  Sets the size, in pixels, of imageblock data in tile memory.
### Configuring stage-in data
- [func setStageInRegion(MTLRegion)](./mtlcomputecommandencoder/setstageinregion%28_%29.md)
  Sets the dimensions over the thread grid of how your compute kernel receives stage-in arguments.
- [func setStageInRegionWithIndirectBuffer(any MTLBuffer, indirectBufferOffset: Int)](./mtlcomputecommandencoder/setstageinregionwithindirectbuffer%28_,indirectbufferoffset%29.md)
  Sets the region of the stage-in attributes to apply to a compute kernel using an indirect buffer.
### Dispatching kernel calls directly
- [func dispatchThreads(MTLSize, threadsPerThreadgroup: MTLSize)](./mtlcomputecommandencoder/dispatchthreads%28_,threadsperthreadgroup%29.md)
  Encodes a compute command using an arbitrarily sized grid.
- [func dispatchThreadgroups(MTLSize, threadsPerThreadgroup: MTLSize)](./mtlcomputecommandencoder/dispatchthreadgroups%28_,threadsperthreadgroup%29.md)
  Encodes a compute dispatch command using a grid aligned to threadgroup boundaries.
### Dispatching from indirect command buffers
- [func dispatchThreadgroups(indirectBuffer: any MTLBuffer, indirectBufferOffset: Int, threadsPerThreadgroup: MTLSize)](./mtlcomputecommandencoder/dispatchthreadgroups%28indirectbuffer,indirectbufferoffset,threadsperthreadgroup%29.md)
  Encodes a dispatch call for a compute pass, using an indirect buffer that defines the size of a grid that aligns to threadgroup boundaries.
- [func executeCommandsInBuffer(any MTLIndirectCommandBuffer, range: Range<Int>)](./mtlcomputecommandencoder/executecommandsinbuffer%28_,range%29.md)
  Encodes an instruction to run commands from an indirect buffer.
- [func executeCommandsInBuffer(any MTLIndirectCommandBuffer, indirectBuffer: any MTLBuffer, offset: Int)](./mtlcomputecommandencoder/executecommandsinbuffer%28_,indirectbuffer,offset%29.md)
  Encodes an instruction to run commands from an indirect buffer, using another buffer to provide the command range.
- [func executeCommands(in: any MTLIndirectCommandBuffer, indirectBuffer: any MTLBuffer, indirectBufferOffset: Int)](./mtlcomputecommandencoder/executecommands%28in,indirectbuffer,indirectbufferoffset%29.md)
  Encodes an instruction to run commands from an indirect buffer, using another buffer to provide the command range.
- [func executeCommands(in: any MTLIndirectCommandBuffer, with: NSRange)](./mtlcomputecommandencoder/executecommands%28in,with%29.md)
  Encodes an instruction to run commands from an indirect buffer.
### Preventing resource access conflicts
- [func waitForFence(any MTLFence)](./mtlcomputecommandencoder/waitforfence%28_%29.md)
  Encodes a command that instructs the GPU to pause the compute pass until another pass updates a fence.
- [func updateFence(any MTLFence)](./mtlcomputecommandencoder/updatefence%28_%29.md)
  Encodes a command that instructs the GPU to update a fence after the compute pass completes.
- [func memoryBarrier(scope: MTLBarrierScope)](./mtlcomputecommandencoder/memorybarrier%28scope%29.md)
  Creates a memory barrier that enforces the order of write and read operations for specific resource types.
- [func memoryBarrier(resources: [any MTLResource])](./mtlcomputecommandencoder/memorybarrier%28resources%29.md)
  Creates a memory barrier that enforces the order of write and read operations for specific resources.
### Sampling counters
- [func sampleCounters(sampleBuffer: any MTLCounterSampleBuffer, sampleIndex: Int, barrier: Bool)](./mtlcomputecommandencoder/samplecounters%28samplebuffer,sampleindex,barrier%29.md)
  Encodes a command to sample hardware counters, providing performance information.

## Relationships

### Inherits From
- [MTLCommandEncoder](./mtlcommandencoder.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Encoding a compute pass
- [Creating threads and threadgroups](./creating-threads-and-threadgroups.md)
  Learn how Metal organizes compute-processing workloads.
- [Calculating threadgroup and grid sizes](./calculating-threadgroup-and-grid-sizes.md)
  Calculate the optimum sizes for threadgroups and grids when dispatching compute-processing workloads.
- [protocol MTL4ComputeCommandEncoder](./mtl4computecommandencoder.md)
  Encodes computation dispatches, resource copying commands, and acceleration structure building commands for a single pass into a command buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder)*
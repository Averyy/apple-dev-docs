# MTLComputeCommandEncoder

**Framework**: Metal  
**Kind**: protocol

An interface for dispatching commands to encode in a compute pass.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
protocol MTLComputeCommandEncoder : MTLCommandEncoder
```

## Mentions

- [Tracking the Resource Residency of Argument Buffers](tracking-the-resource-residency-of-argument-buffers.md)
- [Improving CPU Performance by Using Argument Buffers](improving-cpu-performance-by-using-argument-buffers.md)
- [Sampling GPU Data into Counter Sample Buffers](sampling-gpu-data-into-counter-sample-buffers.md)
- [Setting Up a Command Structure](setting-up-a-command-structure.md)
- [Simplifying GPU Resource Management with Residency Sets](simplifying-gpu-resource-management-with-residency-sets.md)

#### Overview

You create compute command encoders by calling the [`makeComputeCommandEncoder(dispatchType:)`](mtlcommandbuffer/makecomputecommandencoder(dispatchtype:).md) method of the [`MTLCommandBuffer`](mtlcommandbuffer.md) instance you’re using to encode your compute pass. You can encode multiple commands to execute as part of a single pass of the encoder.

To encode kernel function calls:

1. Configure an [`MTLComputePipelineState`](mtlcomputepipelinestate.md) instance with a kernel, using a method such as [`makeComputePipelineState(function:)`](mtldevice/makecomputepipelinestate(function:).md). See Creating Compute Pipeline States for all [`MTLDevice`](mtldevice.md) methods that create a new pipeline state for your command encoder.
2. Set the pipeline state with the [`setComputePipelineState(_:)`](mtlcomputecommandencoder/setcomputepipelinestate(_:).md) method on your command encoder.
3. Provide parameters for your compute kernel by binding information to kernel arguments._ _Examples of methods that bind data for access on the GPU are [`setBuffer(_:offset:index:)`](mtlcomputecommandencoder/setbuffer(_:offset:index:).md) and [`setTexture(_:index:)`](mtlcomputecommandencoder/settexture(_:index:).md).
4. Encode compute commands that call your kernel by either Dispatching Kernel Calls Directly or Dispatching from Indirect Command Buffers.
5. Call [`endEncoding()`](mtlcommandencoder/endencoding().md) to finish encoding the kernel call of the compute pass.

> ❗ **Important**:  Call [`endEncoding()`](mtlcommandencoder/endencoding().md) on any existing compute command encoder before releasing it or creating one.

 Call [`endEncoding()`](mtlcommandencoder/endencoding().md) on any existing compute command encoder before releasing it or creating one.

After adding all commands to your compute command encoder, use the [`commit()`](mtlcommandbuffer/commit().md) method to submit work to the GPU.

## Topics

### Configuring the Pipeline State
- [func setComputePipelineState(any MTLComputePipelineState)](mtlcomputecommandencoder/setcomputepipelinestate(_:).md)
  Configures the compute encoder with a pipeline state instance for subsequent kernel calls.
- [var dispatchType: MTLDispatchType](mtlcomputecommandencoder/dispatchtype.md)
  The dispatch type to use when submitting compute work to the GPU.
### Encoding Buffers
- [func setBuffer((any MTLBuffer)?, offset: Int, index: Int)](mtlcomputecommandencoder/setbuffer(_:offset:index:).md)
  Binds a buffer to the buffer argument table, allowing compute kernels to access its data on the GPU.
- [func setBuffer(any MTLBuffer, offset: Int, attributeStride: Int, index: Int)](mtlcomputecommandencoder/setbuffer(_:offset:attributestride:index:).md)
  Binds a buffer with a stride to the buffer argument table, allowing compute kernels to access its data on the GPU.
- [func setBuffers([(any MTLBuffer)?], offsets: [Int], range: Range<Int>)](mtlcomputecommandencoder/setbuffers(_:offsets:range:).md)
  Binds multiple buffers to the buffer argument table at once, allowing compute kernels to access their data on the GPU.
- [func setBuffers([(any MTLBuffer)?], offsets: [Int], attributeStrides: [Int], range: Range<Int>)](mtlcomputecommandencoder/setbuffers(_:offsets:attributestrides:range:).md)
  Binds multiple buffers with data in stride to the buffer argument table at once, allowing compute kernels to access their data on the GPU.
- [func setBufferOffset(Int, index: Int)](mtlcomputecommandencoder/setbufferoffset(_:index:).md)
  Changes where the data begins in a buffer already bound to the buffer argument table.
- [func setBufferOffset(offset: Int, attributeStride: Int, index: Int)](mtlcomputecommandencoder/setbufferoffset(offset:attributestride:index:).md)
  Changes where the data begins and the distance between adjacent elements in a buffer already bound to the buffer argument table.
### Encoding Raw Bytes
- [func setBytes(UnsafeRawPointer, length: Int, index: Int)](mtlcomputecommandencoder/setbytes(_:length:index:).md)
  Copies data directly to the GPU to populate an entry in the buffer argument table.
- [func setBytes(UnsafeRawPointer, length: Int, attributeStride: Int, index: Int)](mtlcomputecommandencoder/setbytes(_:length:attributestride:index:).md)
  Copies data with a given stride directly to the GPU to populate an entry in the buffer argument table.
### Encoding Textures
- [func setTexture((any MTLTexture)?, index: Int)](mtlcomputecommandencoder/settexture(_:index:).md)
  Binds a texture to the texture argument table, allowing compute kernels to access its data on the GPU.
- [func setTextures([(any MTLTexture)?], range: Range<Int>)](mtlcomputecommandencoder/settextures(_:range:).md)
  Binds multiple textures to the texture argument table, allowing compute functions to access their data on the GPU.
### Encoding Texture Sampler States
- [func setSamplerState((any MTLSamplerState)?, index: Int)](mtlcomputecommandencoder/setsamplerstate(_:index:).md)
  Encodes a texture sampler, allowing compute kernels to use it for sampling textures on the GPU.
- [func setSamplerState((any MTLSamplerState)?, lodMinClamp: Float, lodMaxClamp: Float, index: Int)](mtlcomputecommandencoder/setsamplerstate(_:lodminclamp:lodmaxclamp:index:).md)
  Encodes a texture sampler with a custom level of detail clamping, allowing compute kernels to use it for sampling textures on the GPU.
- [func setSamplerStates([(any MTLSamplerState)?], range: Range<Int>)](mtlcomputecommandencoder/setsamplerstates(_:range:).md)
  Encodes multiple texture samplers to the sampler argument table, allowing compute kernels to use them for sampling textures on the GPU.
- [func setSamplerStates([(any MTLSamplerState)?], lodMinClamps: [Float], lodMaxClamps: [Float], range: Range<Int>)](mtlcomputecommandencoder/setsamplerstates(_:lodminclamps:lodmaxclamps:range:).md)
  Encodes multiple texture samplers for the compute function, specifying clamp values for the level of detail of each sampler.
### Encoding Function Tables
- [func setVisibleFunctionTable((any MTLVisibleFunctionTable)?, bufferIndex: Int)](mtlcomputecommandencoder/setvisiblefunctiontable(_:bufferindex:).md)
  Binds a visible function table to the buffer argument table, allowing you to call its functions on the GPU.
- [func setVisibleFunctionTables([(any MTLVisibleFunctionTable)?], bufferRange: Range<Int>)](mtlcomputecommandencoder/setvisiblefunctiontables(_:bufferrange:).md)
  Binds multiple visible function tables to the buffer argument table, allowing you to call their functions on the GPU.
- [func setIntersectionFunctionTables([(any MTLIntersectionFunctionTable)?], bufferRange: Range<Int>)](mtlcomputecommandencoder/setintersectionfunctiontables(_:bufferrange:).md)
  Binds multiple intersection function tables to the buffer argument table, allowing you to call their functions on the GPU.
### Encoding Acceleration Structures
- [func setAccelerationStructure((any MTLAccelerationStructure)?, bufferIndex: Int)](mtlcomputecommandencoder/setaccelerationstructure(_:bufferindex:).md)
  Binds an acceleration structure to the buffer argument table, allowing functions to access it on the GPU.
- [func setIntersectionFunctionTable((any MTLIntersectionFunctionTable)?, bufferIndex: Int)](mtlcomputecommandencoder/setintersectionfunctiontable(_:bufferindex:).md)
  Binds an intersection function table to the buffer argument table, making it callable in your Metal shaders.
### Encoding Resident Resources
- [func useResource(any MTLResource, usage: MTLResourceUsage)](mtlcomputecommandencoder/useresource(_:usage:).md)
  Ensures kernel calls that the system encodes in subsequent commands have access to a resource.
- [func useResources([any MTLResource], usage: MTLResourceUsage)](mtlcomputecommandencoder/useresources(_:usage:).md)
  Ensures kernel calls that the system encodes in subsequent commands have access to multiple resources.
- [func useHeap(any MTLHeap)](mtlcomputecommandencoder/useheap(_:).md)
  Ensures the shaders in the render pass’s subsequent draw commands have access to all of the resources you allocate from a heap.
- [func useHeaps([any MTLHeap])](mtlcomputecommandencoder/useheaps(_:).md)
  Ensures the shaders in the render pass’s subsequent draw commands have access to all of the resources you allocate from multiple heaps.
### Encoding Tile Memory Usage
- [func setThreadgroupMemoryLength(Int, index: Int)](mtlcomputecommandencoder/setthreadgroupmemorylength(_:index:).md)
  Configures the size of a block of threadgroup memory.
- [func setImageblockWidth(Int, height: Int)](mtlcomputecommandencoder/setimageblockwidth(_:height:).md)
  Sets the size, in pixels, of imageblock data in tile memory.
### Encoding Stage-in Data
- [func setStageInRegion(MTLRegion)](mtlcomputecommandencoder/setstageinregion(_:).md)
  Sets the dimensions over the thread grid of how your compute kernel receives stage-in arguments.
- [func setStageInRegionWithIndirectBuffer(any MTLBuffer, indirectBufferOffset: Int)](mtlcomputecommandencoder/setstageinregionwithindirectbuffer(_:indirectbufferoffset:).md)
  Sets the region of the stage-in attributes to apply to a compute kernel using an indirect buffer.
### Dispatching Kernel Calls Directly
- [func dispatchThreads(MTLSize, threadsPerThreadgroup: MTLSize)](mtlcomputecommandencoder/dispatchthreads(_:threadsperthreadgroup:).md)
  Encodes a compute command using an arbitrarily sized grid.
- [func dispatchThreadgroups(MTLSize, threadsPerThreadgroup: MTLSize)](mtlcomputecommandencoder/dispatchthreadgroups(_:threadsperthreadgroup:).md)
  Encodes a compute dispatch command using a grid aligned to threadgroup boundaries.
### Dispatching from Indirect Command Buffers
- [func dispatchThreadgroups(indirectBuffer: any MTLBuffer, indirectBufferOffset: Int, threadsPerThreadgroup: MTLSize)](mtlcomputecommandencoder/dispatchthreadgroups(indirectbuffer:indirectbufferoffset:threadsperthreadgroup:).md)
  Encodes a dispatch call for a compute pass, using an indirect buffer that defines the size of a grid that aligns to threadgroup boundaries.
- [func executeCommandsInBuffer(any MTLIndirectCommandBuffer, range: Range<Int>)](mtlcomputecommandencoder/executecommandsinbuffer(_:range:).md)
  Encodes an instruction to run commands from an indirect buffer.
- [func executeCommandsInBuffer(any MTLIndirectCommandBuffer, indirectBuffer: any MTLBuffer, offset: Int)](mtlcomputecommandencoder/executecommandsinbuffer(_:indirectbuffer:offset:).md)
  Encodes an instruction to run commands from an indirect buffer, using another buffer to provide the command range.
- [func executeCommands(in: any MTLIndirectCommandBuffer, indirectBuffer: any MTLBuffer, indirectBufferOffset: Int)](mtlcomputecommandencoder/executecommands(in:indirectbuffer:indirectbufferoffset:).md)
  Encodes an instruction to run commands from an indirect buffer, using another buffer to provide the command range.
- [func executeCommands(in: any MTLIndirectCommandBuffer, with: NSRange)](mtlcomputecommandencoder/executecommands(in:with:).md)
  Encodes an instruction to run commands from an indirect buffer.
### Synchronizing Across Command Execution
- [func waitForFence(any MTLFence)](mtlcomputecommandencoder/waitforfence(_:).md)
  Encodes a command that instructs the GPU to pause pass execution until a fence updates.
- [func updateFence(any MTLFence)](mtlcomputecommandencoder/updatefence(_:).md)
  Encodes a command that instructs the GPU to update a fence, allowing passes waiting on the fence to start or resume.
- [func memoryBarrier(scope: MTLBarrierScope)](mtlcomputecommandencoder/memorybarrier(scope:).md)
  Creates a memory barrier that enforces the order of write and read operations for specific resource types.
- [func memoryBarrier(resources: [any MTLResource])](mtlcomputecommandencoder/memorybarrier(resources:).md)
  Creates a memory barrier that enforces the order of write and read operations for specific resources.
### Encoding Sample Counters
- [func sampleCounters(sampleBuffer: any MTLCounterSampleBuffer, sampleIndex: Int, barrier: Bool)](mtlcomputecommandencoder/samplecounters(samplebuffer:sampleindex:barrier:).md)
  Encodes a command to sample hardware counters, providing performance information.

## Relationships

### Inherits From
- [MTLCommandEncoder](mtlcommandencoder.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Creating Threads and Threadgroups](creating-threads-and-threadgroups.md)
  Learn how Metal organizes compute-processing workloads.
- [Calculating Threadgroup and Grid Sizes](calculating-threadgroup-and-grid-sizes.md)
  Calculate the optimum sizes for threadgroups and grids when dispatching compute-processing workloads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder)*
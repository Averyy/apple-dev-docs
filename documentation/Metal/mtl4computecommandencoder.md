# MTL4ComputeCommandEncoder

**Framework**: Metal  
**Kind**: protocol

Encodes computation dispatches, resource copying commands, and acceleration structure building commands for a single pass into a command buffer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
protocol MTL4ComputeCommandEncoder : MTL4CommandEncoder
```

## Mentions

- [Understanding the Metal 4 core API](understanding-the-metal-4-core-api.md)

#### Overview

Each Metal 4 compute encoder combines compute dispatch commands, blit commands, and acceleration structure commands into a single pass. The unified nature of this encoder type eliminates the overhead from creating separate encoders like [`MTLComputeCommandEncoder`](mtlcomputecommandencoder.md), [`MTLBlitCommandEncoder`](mtlblitcommandencoder.md), and [`MTLAccelerationStructureCommandEncoder`](mtlaccelerationstructurecommandencoder.md), and then encoding separate passes with them.

Create a compute encoder by calling a factory method of an [`MTL4CommandBuffer`](mtl4commandbuffer.md) instance, such as [`makeComputeCommandEncoder()`](mtl4commandbuffer/makecomputecommandencoder().md).

##### Command Stages

Most compute commands apply to one stage within a pass. The following table shows which stage applies to each command:

| Function | MTLStages |
| --- | --- |
| [`dispatchThreads(threadsPerGrid:threadsPerThreadgroup:)`](mtl4computecommandencoder/dispatchthreads(threadspergrid:threadsperthreadgroup:).md) | [`dispatch`](mtlstages/dispatch.md) |
| [`dispatchThreads(indirectBuffer:)`](mtl4computecommandencoder/dispatchthreads(indirectbuffer:).md) | [`dispatch`](mtlstages/dispatch.md) |
| [`dispatchThreadgroups(threadgroupsPerGrid:threadsPerThreadgroup:)`](mtl4computecommandencoder/dispatchthreadgroups(threadgroupspergrid:threadsperthreadgroup:).md) | [`dispatch`](mtlstages/dispatch.md) |
| [`dispatchThreadgroups(indirectBuffer:threadsPerThreadgroup:)`](mtl4computecommandencoder/dispatchthreadgroups(indirectbuffer:threadsperthreadgroup:).md) | [`dispatch`](mtlstages/dispatch.md) |
| [`copy(sourceBuffer:sourceOffset:destinationBuffer:destinationOffset:size:)`](mtl4computecommandencoder/copy(sourcebuffer:sourceoffset:destinationbuffer:destinationoffset:size:).md) | [`blit`](mtlstages/blit.md) |
| [`copy(sourceBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:destinationTexture:destinationSlice:destinationLevel:destinationOrigin:options:)`](mtl4computecommandencoder/copy(sourcebuffer:sourceoffset:sourcebytesperrow:sourcebytesperimage:sourcesize:destinationtexture:destinationslice:destinationlevel:destinationorigin:options:).md) | [`blit`](mtlstages/blit.md) |
| [`copy(sourceTensor:sourceOrigin:sourceDimensions:destinationTensor:destinationOrigin:destinationDimensions:)`](mtl4computecommandencoder/copy(sourcetensor:sourceorigin:sourcedimensions:destinationtensor:destinationorigin:destinationdimensions:).md) | [`blit`](mtlstages/blit.md) |
| [`copy(sourceTexture:destinationTexture:)`](mtl4computecommandencoder/copy(sourcetexture:destinationtexture:).md) | [`blit`](mtlstages/blit.md) |
| [`copy(sourceTexture:sourceSlice:sourceLevel:destinationTexture:destinationSlice:destinationLevel:sliceCount:levelCount:)`](mtl4computecommandencoder/copy(sourcetexture:sourceslice:sourcelevel:destinationtexture:destinationslice:destinationlevel:slicecount:levelcount:).md) | [`blit`](mtlstages/blit.md) |
| [`copy(sourceTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:destinationBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:options:)`](mtl4computecommandencoder/copy(sourcetexture:sourceslice:sourcelevel:sourceorigin:sourcesize:destinationbuffer:destinationoffset:destinationbytesperrow:destinationbytesperimage:options:).md) | [`blit`](mtlstages/blit.md) |
| [`copy(sourceTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:destinationTexture:destinationSlice:destinationLevel:destinationOrigin:)`](mtl4computecommandencoder/copy(sourcetexture:sourceslice:sourcelevel:sourceorigin:sourcesize:destinationtexture:destinationslice:destinationlevel:destinationorigin:).md) | [`blit`](mtlstages/blit.md) |
| [`copyCommands(sourceBuffer:sourceRange:destinationBuffer:destinationIndex:)`](mtl4computecommandencoder/copycommands(sourcebuffer:sourcerange:destinationbuffer:destinationindex:).md) | [`blit`](mtlstages/blit.md) |
| [`fill(buffer:range:value:)`](mtl4computecommandencoder/fill(buffer:range:value:).md) | [`blit`](mtlstages/blit.md) |
| [`generateMipmaps(texture:)`](mtl4computecommandencoder/generatemipmaps(texture:).md) | [`blit`](mtlstages/blit.md) |
| [`optimizeCommands(buffer:range:)`](mtl4computecommandencoder/optimizecommands(buffer:range:).md) | [`blit`](mtlstages/blit.md) |
| [`optimizeContents(forCPUAccess:)`](mtl4computecommandencoder/optimizecontents(forcpuaccess:).md) | [`blit`](mtlstages/blit.md) |
| [`optimizeContents(forCPUAccess:slice:level:)`](mtl4computecommandencoder/optimizecontents(forcpuaccess:slice:level:).md) | [`blit`](mtlstages/blit.md) |
| [`optimizeContents(forGPUAccess:)`](mtl4computecommandencoder/optimizecontents(forgpuaccess:).md) | [`blit`](mtlstages/blit.md) |
| [`optimizeContents(forGPUAccess:slice:level:)`](mtl4computecommandencoder/optimizecontents(forgpuaccess:slice:level:).md) | [`blit`](mtlstages/blit.md) |
| [`resetCommands(buffer:range:)`](mtl4computecommandencoder/resetcommands(buffer:range:).md) | [`blit`](mtlstages/blit.md) |
| [`build(destinationAccelerationStructure:descriptor:scratchBuffer:)`](mtl4computecommandencoder/build(destinationaccelerationstructure:descriptor:scratchbuffer:).md) | [`accelerationStructure`](mtlstages/accelerationstructure.md) |
| [`copy(sourceAccelerationStructure:destinationAccelerationStructure:)`](mtl4computecommandencoder/copy(sourceaccelerationstructure:destinationaccelerationstructure:).md) | [`accelerationStructure`](mtlstages/accelerationstructure.md) |
| [`copyAndCompact(sourceAccelerationStructure:destinationAccelerationStructure:)`](mtl4computecommandencoder/copyandcompact(sourceaccelerationstructure:destinationaccelerationstructure:).md) | [`accelerationStructure`](mtlstages/accelerationstructure.md) |
| [`refit(sourceAccelerationStructure:descriptor:destinationAccelerationStructure:scratchBuffer:options:)`](mtl4computecommandencoder/refit(sourceaccelerationstructure:descriptor:destinationaccelerationstructure:scratchbuffer:options:).md) | [`accelerationStructure`](mtlstages/accelerationstructure.md) |
| [`writeCompactedSize(sourceAccelerationStructure:destinationBuffer:)`](mtl4computecommandencoder/writecompactedsize(sourceaccelerationstructure:destinationbuffer:).md) | [`accelerationStructure`](mtlstages/accelerationstructure.md) |
| [`executeCommands(buffer:range:)`](mtl4computecommandencoder/executecommands(buffer:range:).md)![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[`executeCommandsInBuffer:withRange:`](mtl4computecommandencoder/executecommandsinbuffer:withrange:.md) | None |
| [`executeCommands(buffer:indirectBuffer:)`](mtl4computecommandencoder/executecommands(buffer:indirectbuffer:).md) | None |
| [`writeTimestamp(granularity:counterHeap:index:)`](mtl4computecommandencoder/writetimestamp(granularity:counterheap:index:).md) | None |

The [`executeCommands(buffer:range:)`](mtl4computecommandencoder/executecommands(buffer:range:).md) and [`executeCommands(buffer:indirectBuffer:)`](mtl4computecommandencoder/executecommands(buffer:indirectbuffer:).md) commands don’t apply to any stage, which means you can’t use a barrier to wait for all commands in an indirect command buffer to complete. However, each command within the [`MTLIndirectCommandBuffer`](mtlindirectcommandbuffer.md) applies to the same stages as when you encode the equivalent command directly.

For more information about stages and synchronization, see [`MTLStages`](mtlstages.md) and [`Resource synchronization`](resource-synchronization.md).

## Topics

### Configuring the pass
- [func setComputePipelineState(any MTLComputePipelineState)](mtl4computecommandencoder/setcomputepipelinestate(_:).md)
  Configures this encoder with a compute pipeline state that applies to your subsequent dispatch commands.
- [func setArgumentTable((any MTL4ArgumentTable)?)](mtl4computecommandencoder/setargumenttable(_:).md)
  Sets an argument table for the compute shader stage of this pipeline.
- [func setThreadgroupMemoryLength(Int, index: Int)](mtl4computecommandencoder/setthreadgroupmemorylength(_:index:).md)
  Configures the size of a threadgroup memory buffer for a threadgroup argument in the compute shader function.
- [func setImageblockSize(width: Int, height: Int)](mtl4computecommandencoder/setimageblocksize(width:height:).md)
  Specifies the size, in pixels, of imageblock data in tile memory.
### Inspecting the pass
- [func stages() -> MTLStages](mtl4computecommandencoder/stages.md)
  Queries a bitmask representing the shader stages on which commands currently present in this command encoder operate.
### Running dispatch commands
- [func dispatchThreads(threadsPerGrid: MTLSize, threadsPerThreadgroup: MTLSize)](mtl4computecommandencoder/dispatchthreads(threadspergrid:threadsperthreadgroup:).md)
  Encodes a compute dispatch command using an arbitrarily-sized grid.
- [func dispatchThreads(indirectBuffer: MTLGPUAddress)](mtl4computecommandencoder/dispatchthreads(indirectbuffer:).md)
  Encodes a compute dispatch command with an arbitrarily sized grid, using an indirect buffer for arguments.
- [func dispatchThreadgroups(threadgroupsPerGrid: MTLSize, threadsPerThreadgroup: MTLSize)](mtl4computecommandencoder/dispatchthreadgroups(threadgroupspergrid:threadsperthreadgroup:).md)
  Encodes a compute dispatch command with a grid that aligns to threadgroup boundaries.
- [func dispatchThreadgroups(indirectBuffer: MTLGPUAddress, threadsPerThreadgroup: MTLSize)](mtl4computecommandencoder/dispatchthreadgroups(indirectbuffer:threadsperthreadgroup:).md)
  Encodes a compute dispatch command with a grid that aligns to threadgroup boundaries, using an indirect buffer for arguments.
### Encoding buffer copy commands
- [func copy(sourceBuffer: any MTLBuffer, sourceOffset: Int, destinationBuffer: any MTLBuffer, destinationOffset: Int, size: Int)](mtl4computecommandencoder/copy(sourcebuffer:sourceoffset:destinationbuffer:destinationoffset:size:).md)
  Encodes a command that copies data from a buffer instance into another.
### Encoding buffer-to-texture copy commands
- [func copy(sourceBuffer: any MTLBuffer, sourceOffset: Int, sourceBytesPerRow: Int, sourceBytesPerImage: Int, sourceSize: MTLSize, destinationTexture: any MTLTexture, destinationSlice: Int, destinationLevel: Int, destinationOrigin: MTLOrigin, options: MTLBlitOption)](mtl4computecommandencoder/copy(sourcebuffer:sourceoffset:sourcebytesperrow:sourcebytesperimage:sourcesize:destinationtexture:destinationslice:destinationlevel:destinationorigin:options:).md)
  Encodes a command to copy image data from a buffer into a texture with options for special texture formats.
### Encoding texture copy commands
- [func copy(sourceTensor: any MTLTensor, sourceOrigin: MTLTensorExtents, sourceDimensions: MTLTensorExtents, destinationTensor: any MTLTensor, destinationOrigin: MTLTensorExtents, destinationDimensions: MTLTensorExtents)](mtl4computecommandencoder/copy(sourcetensor:sourceorigin:sourcedimensions:destinationtensor:destinationorigin:destinationdimensions:).md)
  Encodes a command to copy data from a tensor instance into another.
- [func copy(sourceTexture: any MTLTexture, destinationTexture: any MTLTexture)](mtl4computecommandencoder/copy(sourcetexture:destinationtexture:).md)
  Encodes a command that copies data from a texture to another.
- [func copy(sourceTexture: any MTLTexture, sourceSlice: Int, sourceLevel: Int, destinationTexture: any MTLTexture, destinationSlice: Int, destinationLevel: Int, sliceCount: Int, levelCount: Int)](mtl4computecommandencoder/copy(sourcetexture:sourceslice:sourcelevel:destinationtexture:destinationslice:destinationlevel:slicecount:levelcount:).md)
  Encodes a command that copies slices of a texture to slices of another texture.
- [func copy(sourceTexture: any MTLTexture, sourceSlice: Int, sourceLevel: Int, sourceOrigin: MTLOrigin, sourceSize: MTLSize, destinationTexture: any MTLTexture, destinationSlice: Int, destinationLevel: Int, destinationOrigin: MTLOrigin)](mtl4computecommandencoder/copy(sourcetexture:sourceslice:sourcelevel:sourceorigin:sourcesize:destinationtexture:destinationslice:destinationlevel:destinationorigin:).md)
  Encodes a command that copies image data from a slice of a texture into a slice of another texture.
### Encoding texture-to-buffer copy commands
- [func copy(sourceTexture: any MTLTexture, sourceSlice: Int, sourceLevel: Int, sourceOrigin: MTLOrigin, sourceSize: MTLSize, destinationBuffer: any MTLBuffer, destinationOffset: Int, destinationBytesPerRow: Int, destinationBytesPerImage: Int, options: MTLBlitOption)](mtl4computecommandencoder/copy(sourcetexture:sourceslice:sourcelevel:sourceorigin:sourcesize:destinationbuffer:destinationoffset:destinationbytesperrow:destinationbytesperimage:options:).md)
  Encodes a command that copies image data from a slice of a texture instance to a buffer, with options for special texture formats.
### Encoding indirect command buffer copy commands
- [func copyCommands(sourceBuffer: any MTLIndirectCommandBuffer, sourceRange: Range<Int>, destinationBuffer: any MTLIndirectCommandBuffer, destinationIndex: Int)](mtl4computecommandencoder/copycommands(sourcebuffer:sourcerange:destinationbuffer:destinationindex:).md)
  Encodes a command that copies commands from one indirect command buffer into another.
### Encoding buffer fill commands
- [func fill(buffer: any MTLBuffer, range: Range<Int>, value: UInt8)](mtl4computecommandencoder/fill(buffer:range:value:).md)
  Encodes a command that fills a buffer with a constant value for each byte.
### Encoding mipmap generation commands
- [func generateMipmaps(texture: any MTLTexture)](mtl4computecommandencoder/generatemipmaps(texture:).md)
  Encodes a command that generates mipmaps for a texture instance from the base mipmap level up to the highest mipmap level.
### Encoding optimization commands
- [func optimizeCommands(buffer: any MTLIndirectCommandBuffer, range: Range<Int>)](mtl4computecommandencoder/optimizecommands(buffer:range:).md)
  Encode a command to attempt to improve the performance of a range of commands within an indirect command buffer.
- [func optimizeContents(forCPUAccess: any MTLTexture)](mtl4computecommandencoder/optimizecontents(forcpuaccess:).md)
  Encodes a command that modifies the contents of a texture to improve the performance of CPU accesses to its contents.
- [func optimizeContents(forCPUAccess: any MTLTexture, slice: Int, level: Int)](mtl4computecommandencoder/optimizecontents(forcpuaccess:slice:level:).md)
  Encodes a command that modifies the contents of a texture to improve the performance of CPU accesses to its contents in a specific region.
- [func optimizeContents(forGPUAccess: any MTLTexture)](mtl4computecommandencoder/optimizecontents(forgpuaccess:).md)
  Encodes a command that modifies the contents of a texture to improve the performance of GPU accesses to its contents.
- [func optimizeContents(forGPUAccess: any MTLTexture, slice: Int, level: Int)](mtl4computecommandencoder/optimizecontents(forgpuaccess:slice:level:).md)
  Encodes a command that modifies the contents of a texture instance to improve the performance of GPU accesses to its contents in a specific region.
### Encoding reset commands
- [func resetCommands(buffer: any MTLIndirectCommandBuffer, range: Range<Int>)](mtl4computecommandencoder/resetcommands(buffer:range:).md)
  Encodes a command that resets a range of commands in an indirect command buffer.
### Encoding acceleration structure build commands
- [func build(destinationAccelerationStructure: any MTLAccelerationStructure, descriptor: MTL4AccelerationStructureDescriptor, scratchBuffer: MTL4BufferRange)](mtl4computecommandencoder/build(destinationaccelerationstructure:descriptor:scratchbuffer:).md)
  Encodes an acceleration structure build into the command buffer.
### Encoding acceleration structure copy commands
- [func copy(sourceAccelerationStructure: any MTLAccelerationStructure, destinationAccelerationStructure: any MTLAccelerationStructure)](mtl4computecommandencoder/copy(sourceaccelerationstructure:destinationaccelerationstructure:).md)
  Encodes an acceleration structure copy operation into the command buffer.
- [func copyAndCompact(sourceAccelerationStructure: any MTLAccelerationStructure, destinationAccelerationStructure: any MTLAccelerationStructure)](mtl4computecommandencoder/copyandcompact(sourceaccelerationstructure:destinationaccelerationstructure:).md)
  Encodes a command to copy and compact an acceleration structure.
- [func writeCompactedSize(sourceAccelerationStructure: any MTLAccelerationStructure, destinationBuffer: MTL4BufferRange)](mtl4computecommandencoder/writecompactedsize(sourceaccelerationstructure:destinationbuffer:).md)
  Encodes a command to compute the size an acceleration structure can compact into, writing the result into a buffer.
### Encoding acceleration structure refit commands
- [func refit(sourceAccelerationStructure: any MTLAccelerationStructure, descriptor: MTL4AccelerationStructureDescriptor, destinationAccelerationStructure: (any MTLAccelerationStructure)?, scratchBuffer: MTL4BufferRange, options: MTLAccelerationStructureRefitOptions)](mtl4computecommandencoder/refit(sourceaccelerationstructure:descriptor:destinationaccelerationstructure:scratchbuffer:options:).md)
  Encodes an acceleration structure refit operation into the command buffer, providing additional options.
### Encoding indirect command buffers
- [func executeCommands(buffer: any MTLIndirectCommandBuffer, range: Range<Int>)](mtl4computecommandencoder/executecommands(buffer:range:).md)
  Encodes a command to execute commands from an indirect command buffer.
- [func executeCommands(buffer: any MTLIndirectCommandBuffer, indirectBuffer: MTLGPUAddress)](mtl4computecommandencoder/executecommands(buffer:indirectbuffer:).md)
  Encodes an instruction to execute commands from an indirect command buffer, using an indirect buffer for arguments.
### Encoding performance measurement commands
- [func writeTimestamp(granularity: MTL4TimestampGranularity, counterHeap: any MTL4CounterHeap, index: Int)](mtl4computecommandencoder/writetimestamp(granularity:counterheap:index:).md)
  Writes a GPU timestamp into a heap.

## Relationships

### Inherits From
- [MTL4CommandEncoder](mtl4commandencoder.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Creating threads and threadgroups](creating-threads-and-threadgroups.md)
  Learn how Metal organizes compute-processing workloads.
- [Calculating threadgroup and grid sizes](calculating-threadgroup-and-grid-sizes.md)
  Calculate the optimum sizes for threadgroups and grids when dispatching compute-processing workloads.
- [protocol MTLComputeCommandEncoder](mtlcomputecommandencoder.md)
  Encodes computation dispatch commands for a single compute pass into a command buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder)*
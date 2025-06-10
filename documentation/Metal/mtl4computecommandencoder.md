# MTL4ComputeCommandEncoder

**Framework**: Metal  
**Kind**: protocol

Encodes a compute pass and other memory operations into a command buffer.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
protocol MTL4ComputeCommandEncoder : MTL4CommandEncoder
```

## Mentions

- [Understanding the Metal 4 core API](understanding-the-metal-4-core-api.md)

#### Overview

Use instances of this abstraction to encode a compute pass into [`MTL4CommandBuffer`](mtl4commandbuffer.md) instances, as well as commands that copy and modify the underlying memory of various Metal resources, and commands that build or refit acceleration structures.

## Topics

### Instance Methods
- [func build(destinationAccelerationStructure: any MTLAccelerationStructure, descriptor: MTL4AccelerationStructureDescriptor, scratchBuffer: MTL4BufferRange)](mtl4computecommandencoder/build(destinationaccelerationstructure:descriptor:scratchbuffer:).md)
  Encodes an acceleration structure build into the command buffer.
- [func copy(sourceAccelerationStructure: any MTLAccelerationStructure, destinationAccelerationStructure: any MTLAccelerationStructure)](mtl4computecommandencoder/copy(sourceaccelerationstructure:destinationaccelerationstructure:).md)
  Encodes an acceleration structure copy operation into the command buffer.
- [func copy(sourceBuffer: any MTLBuffer, sourceOffset: Int, destinationBuffer: any MTLBuffer, destinationOffset: Int, size: Int)](mtl4computecommandencoder/copy(sourcebuffer:sourceoffset:destinationbuffer:destinationoffset:size:).md)
  Encodes a command that copies data from a buffer instance into another.
- [func copy(sourceBuffer: any MTLBuffer, sourceOffset: Int, sourceBytesPerRow: Int, sourceBytesPerImage: Int, sourceSize: MTLSize, destinationTexture: any MTLTexture, destinationSlice: Int, destinationLevel: Int, destinationOrigin: MTLOrigin, options: MTLBlitOption)](mtl4computecommandencoder/copy(sourcebuffer:sourceoffset:sourcebytesperrow:sourcebytesperimage:sourcesize:destinationtexture:destinationslice:destinationlevel:destinationorigin:options:).md)
  Encodes a command to copy image data from a buffer into a texture with options for special texture formats.
- [func copy(sourceTensor: any MTLTensor, sourceOrigin: MTLTensorExtents, sourceDimensions: MTLTensorExtents, destinationTensor: any MTLTensor, destinationOrigin: MTLTensorExtents, destinationDimensions: MTLTensorExtents)](mtl4computecommandencoder/copy(sourcetensor:sourceorigin:sourcedimensions:destinationtensor:destinationorigin:destinationdimensions:).md)
  Encodes a command to copy data from a tensor instance into another.
- [func copy(sourceTexture: any MTLTexture, destinationTexture: any MTLTexture)](mtl4computecommandencoder/copy(sourcetexture:destinationtexture:).md)
  Encodes a command that copies data from a texture to another.
- [func copy(sourceTexture: any MTLTexture, sourceSlice: Int, sourceLevel: Int, destinationTexture: any MTLTexture, destinationSice: Int, destinationLevel: Int, sliceCount: Int, levelCount: Int)](mtl4computecommandencoder/copy(sourcetexture:sourceslice:sourcelevel:destinationtexture:destinationsice:destinationlevel:slicecount:levelcount:).md)
  Encodes a command that copies slices of a texture to slices of another texture.
- [func copy(sourceTexture: any MTLTexture, sourceSlice: Int, sourceLevel: Int, sourceOrigin: MTLOrigin, sourceSize: MTLSize, destinationBuffer: any MTLBuffer, destinationOffset: Int, destinationBytesPerRow: Int, destinationBytesPerImage: Int, options: MTLBlitOption)](mtl4computecommandencoder/copy(sourcetexture:sourceslice:sourcelevel:sourceorigin:sourcesize:destinationbuffer:destinationoffset:destinationbytesperrow:destinationbytesperimage:options:).md)
  Encodes a command that copies image data from a slice of a texture instance to a buffer, with options for special texture formats.
- [func copy(sourceTexture: any MTLTexture, sourceSlice: Int, sourceLevel: Int, sourceOrigin: MTLOrigin, sourceSize: MTLSize, destinationTexture: any MTLTexture, destinationSlice: Int, destinationLevel: Int, destinationOrigin: MTLOrigin)](mtl4computecommandencoder/copy(sourcetexture:sourceslice:sourcelevel:sourceorigin:sourcesize:destinationtexture:destinationslice:destinationlevel:destinationorigin:).md)
  Encodes a command that copies image data from a slice of a texture into a slice of another texture.
- [func copyAndCompact(sourceAccelerationStructure: any MTLAccelerationStructure, destinationAccelerationStructure: any MTLAccelerationStructure)](mtl4computecommandencoder/copyandcompact(sourceaccelerationstructure:destinationaccelerationstructure:).md)
  Encodes a command to copy and compact an acceleration structure.
- [func copyCommands(sourceBuffer: any MTLIndirectCommandBuffer, sourceRange: Range<Int>, destinationBuffer: any MTLIndirectCommandBuffer, destinationIndex: Int)](mtl4computecommandencoder/copycommands(sourcebuffer:sourcerange:destinationbuffer:destinationindex:).md)
  Encodes a command that copies commands from one indirect command buffer into another.
- [func dispatchThreadgroups(indirectBuffer: UInt64, threadsPerThreadgroup: MTLSize)](mtl4computecommandencoder/dispatchthreadgroups(indirectbuffer:threadsperthreadgroup:).md)
  Encodes a compute dispatch command with a grid that aligns to threadgroup boundaries, using an indirect buffer for arguments.
- [func dispatchThreadgroups(threadgroupsPerGrid: MTLSize, threadsPerThreadgroup: MTLSize)](mtl4computecommandencoder/dispatchthreadgroups(threadgroupspergrid:threadsperthreadgroup:).md)
  Encodes a compute dispatch command with a grid that aligns to threadgroup boundaries.
- [func dispatchThreads(indirectBuffer: UInt64)](mtl4computecommandencoder/dispatchthreads(indirectbuffer:).md)
  Encodes a compute dispatch command with an arbitrarily sized grid, using an indirect buffer for arguments.
- [func dispatchThreads(threadsPerGrid: MTLSize, threadsPerThreadgroup: MTLSize)](mtl4computecommandencoder/dispatchthreads(threadspergrid:threadsperthreadgroup:).md)
  Encodes a compute dispatch command using an arbitrarily-sized grid.
- [func executeCommands(buffer: any MTLIndirectCommandBuffer, indirectBuffer: UInt64)](mtl4computecommandencoder/executecommands(buffer:indirectbuffer:).md)
  Encodes an instruction to execute commands from an indirect command buffer, using an indirect buffer for arguments.
- [func executeCommands(buffer: any MTLIndirectCommandBuffer, range: Range<Int>)](mtl4computecommandencoder/executecommands(buffer:range:).md)
  Encodes a command to execute commands from an indirect command buffer.
- [func fill(buffer: any MTLBuffer, range: Range<Int>, value: UInt8)](mtl4computecommandencoder/fill(buffer:range:value:).md)
  Encodes a command that fills a buffer with a constant value for each byte.
- [func generateMipmaps(texture: any MTLTexture)](mtl4computecommandencoder/generatemipmaps(texture:).md)
  Encodes a command that generates mipmaps for a texture instance from the base mipmap level up to the highest mipmap level.
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
- [func refit(sourceAccelerationStructure: any MTLAccelerationStructure, descriptor: MTL4AccelerationStructureDescriptor, destinationAccelerationStructure: (any MTLAccelerationStructure)?, scratchBuffer: MTL4BufferRange, options: MTLAccelerationStructureRefitOptions)](mtl4computecommandencoder/refit(sourceaccelerationstructure:descriptor:destinationaccelerationstructure:scratchbuffer:options:).md)
  Encodes an acceleration structure refit operation into the command buffer, providing additional options.
- [func resetCommands(buffer: any MTLIndirectCommandBuffer, range: Range<Int>)](mtl4computecommandencoder/resetcommands(buffer:range:).md)
  Encodes a command that resets a range of commands in an indirect command buffer.
- [func setArgumentTable((any MTL4ArgumentTable)?)](mtl4computecommandencoder/setargumenttable(_:).md)
  Sets an argument table for the compute shader stage of this pipeline.
- [func setComputePipelineState(any MTLComputePipelineState)](mtl4computecommandencoder/setcomputepipelinestate(_:).md)
  Configures this encoder with a compute pipeline state that applies to your subsequent dispatch commands.
- [func setImageblockSize(width: Int, height: Int)](mtl4computecommandencoder/setimageblocksize(width:height:).md)
  Specifies the size, in pixels, of imageblock data in tile memory.
- [func setThreadgroupMemoryLength(Int, index: Int)](mtl4computecommandencoder/setthreadgroupmemorylength(_:index:).md)
  Configures the size of a threadgroup memory buffer for a threadgroup argument in the compute shader function.
- [func stages() -> MTLStages](mtl4computecommandencoder/stages.md)
  Queries a bitmask representing the shader stages on which commands currently present in this command encoder operate.
- [func writeCompactedSize(sourceAccelerationStructure: any MTLAccelerationStructure, destinationBuffer: MTL4BufferRange)](mtl4computecommandencoder/writecompactedsize(sourceaccelerationstructure:destinationbuffer:).md)
  Encodes a command to compute the size an acceleration structure can compact into, writing the result into a buffer.
- [func writeTimestamp(granularity: MTL4TimestampGranularity, counterHeap: any MTL4CounterHeap, index: Int)](mtl4computecommandencoder/writetimestamp(granularity:counterheap:index:).md)
  Writes a GPU timestamp into a heap.

## Relationships

### Inherits From
- [MTL4CommandEncoder](mtl4commandencoder.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Creating Threads and Threadgroups](creating-threads-and-threadgroups.md)
  Learn how Metal organizes compute-processing workloads.
- [Calculating Threadgroup and Grid Sizes](calculating-threadgroup-and-grid-sizes.md)
  Calculate the optimum sizes for threadgroups and grids when dispatching compute-processing workloads.
- [protocol MTLComputeCommandEncoder](mtlcomputecommandencoder.md)
  An interface for dispatching commands to encode in a compute pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder)*
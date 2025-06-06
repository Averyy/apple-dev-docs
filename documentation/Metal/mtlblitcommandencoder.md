# MTLBlitCommandEncoder

**Framework**: Metal  
**Kind**: protocol

An interface you can use to encode GPU commands that copy and modify the underlying memory of various Metal resources.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
protocol MTLBlitCommandEncoder : MTLCommandEncoder
```

## Mentions

- [Copying Data into or out of Mipmaps](copying-data-into-or-out-of-mipmaps.md)
- [Converting a GPU’s Counter Data into a Readable Format](converting-a-gpus-counter-data-into-a-readable-format.md)
- [Sampling GPU Data into Counter Sample Buffers](sampling-gpu-data-into-counter-sample-buffers.md)
- [Transferring Data Between Connected GPUs](transferring-data-between-connected-gpus.md)

#### Overview

Each GPU driver implements the [`MTLBlitCommandEncoder`](mtlblitcommandencoder.md) protocol, an interface you use to encode various commands that copy or manipulate resource data, which include the following:

- Filling buffers with repeating bytes
- Generating mipmaps for textures
- Copying data between buffers
- Copying data between textures
- Copying data between a texture and a buffer
- Managing the contents of indirect command buffers
- Synchronizing buffers, textures, and other resources between the CPU and GPU
- Improving runtime performance for resources by optimizing their memory layout for the GPU or CPU

Apps typically use these commands to move data between a resource that uses private storage to, or from, another resource that uses CPU-accessible storage. Some apps use them to apply image-processing and texture effects, such as blurring or reflections, or to render and work with offscreen image data.

You can create an [`MTLBlitCommandEncoder`](mtlblitcommandencoder.md) instance by calling one of an [`MTLCommandBuffer`](mtlcommandbuffer.md) instance’s methods, such as [`makeBlitCommandEncoder()`](mtlcommandbuffer/makeblitcommandencoder().md). When you finish encoding blit commands, finalize the blit pass into the command buffer by calling the encoder’s [`endEncoding()`](mtlcommandencoder/endencoding().md) method.

## Topics

### Filling Buffers with Data
- [func fill(buffer: any MTLBuffer, range: Range<Int>, value: UInt8)](mtlblitcommandencoder/fill(buffer:range:value:).md)
  Encodes a command that fills a buffer with a constant value for each byte.
### Generating Texture Mipmaps
- [func generateMipmaps(for: any MTLTexture)](mtlblitcommandencoder/generatemipmaps(for:).md)
  Encodes a command that generates mipmaps for a texture from the base mipmap level up to the highest mipmap level.
### Copying Buffer Data to Another Buffer
- [func copy(from: any MTLBuffer, sourceOffset: Int, to: any MTLBuffer, destinationOffset: Int, size: Int)](mtlblitcommandencoder/copy(from:sourceoffset:to:destinationoffset:size:).md)
  Encodes a command that copies data from one buffer into another.
### Copying Texture Data to Another Texture
- [func copy(from: any MTLTexture, to: any MTLTexture)](mtlblitcommandencoder/copy(from:to:).md)
  Encodes a command that copies data from one texture to another.
- [func copy(from: any MTLTexture, sourceSlice: Int, sourceLevel: Int, to: any MTLTexture, destinationSlice: Int, destinationLevel: Int, sliceCount: Int, levelCount: Int)](mtlblitcommandencoder/copy(from:sourceslice:sourcelevel:to:destinationslice:destinationlevel:slicecount:levelcount:).md)
  Encodes a command that copies slices of a texture to another texture’s slices.
- [func copy(from: any MTLTexture, sourceSlice: Int, sourceLevel: Int, sourceOrigin: MTLOrigin, sourceSize: MTLSize, to: any MTLTexture, destinationSlice: Int, destinationLevel: Int, destinationOrigin: MTLOrigin)](mtlblitcommandencoder/copy(from:sourceslice:sourcelevel:sourceorigin:sourcesize:to:destinationslice:destinationlevel:destinationorigin:).md)
  Encodes a command that copies image data from a texture’s slice into another slice.
### Copying Buffer Data to a Texture
- [func copy(from: any MTLBuffer, sourceOffset: Int, sourceBytesPerRow: Int, sourceBytesPerImage: Int, sourceSize: MTLSize, to: any MTLTexture, destinationSlice: Int, destinationLevel: Int, destinationOrigin: MTLOrigin)](mtlblitcommandencoder/copy(from:sourceoffset:sourcebytesperrow:sourcebytesperimage:sourcesize:to:destinationslice:destinationlevel:destinationorigin:).md)
  Encodes a command to copy image data from a source buffer into a destination texture.
- [func copy(from: any MTLBuffer, sourceOffset: Int, sourceBytesPerRow: Int, sourceBytesPerImage: Int, sourceSize: MTLSize, to: any MTLTexture, destinationSlice: Int, destinationLevel: Int, destinationOrigin: MTLOrigin, options: MTLBlitOption)](mtlblitcommandencoder/copy(from:sourceoffset:sourcebytesperrow:sourcebytesperimage:sourcesize:to:destinationslice:destinationlevel:destinationorigin:options:).md)
  Encodes a command to copy image data from a source buffer into a destination texture.
### Copying Texture Data to a Buffer
- [func copy(from: any MTLTexture, sourceSlice: Int, sourceLevel: Int, sourceOrigin: MTLOrigin, sourceSize: MTLSize, to: any MTLBuffer, destinationOffset: Int, destinationBytesPerRow: Int, destinationBytesPerImage: Int)](mtlblitcommandencoder/copy(from:sourceslice:sourcelevel:sourceorigin:sourcesize:to:destinationoffset:destinationbytesperrow:destinationbytesperimage:).md)
  Encodes a command that copies image data from a texture slice to a buffer.
- [func copy(from: any MTLTexture, sourceSlice: Int, sourceLevel: Int, sourceOrigin: MTLOrigin, sourceSize: MTLSize, to: any MTLBuffer, destinationOffset: Int, destinationBytesPerRow: Int, destinationBytesPerImage: Int, options: MTLBlitOption)](mtlblitcommandencoder/copy(from:sourceslice:sourcelevel:sourceorigin:sourcesize:to:destinationoffset:destinationbytesperrow:destinationbytesperimage:options:).md)
  Encodes a command that copies image data from a texture slice to a buffer, and provides options for special texture formats.
### Working with Textures on the GPU
- [func optimizeContentsForGPUAccess(texture: any MTLTexture)](mtlblitcommandencoder/optimizecontentsforgpuaccess(texture:).md)
  Encodes a command that improves the performance of the GPU’s accesses to a texture.
- [func optimizeContentsForGPUAccess(texture: any MTLTexture, slice: Int, level: Int)](mtlblitcommandencoder/optimizecontentsforgpuaccess(texture:slice:level:).md)
  Encodes a command that improves the performance of the GPU’s accesses to a specific portion of a texture.
### Working with Textures on the CPU
- [func optimizeContentsForCPUAccess(texture: any MTLTexture)](mtlblitcommandencoder/optimizecontentsforcpuaccess(texture:).md)
  Encodes a command that improves the performance of the CPU’s accesses to a texture.
- [func optimizeContentsForCPUAccess(texture: any MTLTexture, slice: Int, level: Int)](mtlblitcommandencoder/optimizecontentsforcpuaccess(texture:slice:level:).md)
  Encodes a command that improves the performance of the CPU’s accesses to a specific portion of a texture.
### Working with Managed Resources
- [func synchronize(resource: any MTLResource)](mtlblitcommandencoder/synchronize(resource:).md)
  Encodes a command that synchronizes the CPU’s copy of a managed resource, such as a buffer or texture, so that it matches the GPU’s copy.
- [func synchronize(texture: any MTLTexture, slice: Int, level: Int)](mtlblitcommandencoder/synchronize(texture:slice:level:).md)
  Encodes a command that synchronizes a part of the CPU’s copy of a texture so that it matches the GPU’s copy.
### Working with Fences
- [func waitForFence(any MTLFence)](mtlblitcommandencoder/waitforfence(_:).md)
  Encodes a command that instructs the GPU to wait until a pass updates a fence.
- [func updateFence(any MTLFence)](mtlblitcommandencoder/updatefence(_:).md)
  Encodes a command that instructs the GPU to update a fence, which signals passes waiting on the fence.
### Working with Indirect Command Buffers
- [func copyIndirectCommandBuffer(any MTLIndirectCommandBuffer, sourceRange: Range<Int>, destination: any MTLIndirectCommandBuffer, destinationIndex: Int)](mtlblitcommandencoder/copyindirectcommandbuffer(_:sourcerange:destination:destinationindex:).md)
  Encodes a command that copies commands from one indirect command buffer into another.
- [func resetCommandsInBuffer(any MTLIndirectCommandBuffer, range: Range<Int>)](mtlblitcommandencoder/resetcommandsinbuffer(_:range:).md)
  Encodes a command that resets a range of commands in an indirect command buffer.
- [func optimizeIndirectCommandBuffer(any MTLIndirectCommandBuffer, range: Range<Int>)](mtlblitcommandencoder/optimizeindirectcommandbuffer(_:range:).md)
  Encodes a command that can improve the performance of a range of commands within an indirect command buffer.
### Working with Sample Counter Buffers
- [func sampleCounters(sampleBuffer: any MTLCounterSampleBuffer, sampleIndex: Int, barrier: Bool)](mtlblitcommandencoder/samplecounters(samplebuffer:sampleindex:barrier:).md)
  Encodes a command that samples the GPU’s hardware counters during a blit pass and stores the data in a counter sample buffer.
- [func resolveCounters(any MTLCounterSampleBuffer, range: Range<Int>, destinationBuffer: any MTLBuffer, destinationOffset: Int)](mtlblitcommandencoder/resolvecounters(_:range:destinationbuffer:destinationoffset:).md)
  Encodes a command that resolves the data from the samples in a sample counter buffer and stores the results into a buffer.
### Working with Sparse Texture Access Counters
- [func getTextureAccessCounters(any MTLTexture, region: MTLRegion, mipLevel: Int, slice: Int, resetCounters: Bool, countersBuffer: any MTLBuffer, countersBufferOffset: Int)](mtlblitcommandencoder/gettextureaccesscounters(_:region:miplevel:slice:resetcounters:countersbuffer:countersbufferoffset:).md)
  Encodes a command that retrieves a sparse texture’s access data for a specific region, mipmap level, and slice.
- [func resetTextureAccessCounters(any MTLTexture, region: MTLRegion, mipLevel: Int, slice: Int)](mtlblitcommandencoder/resettextureaccesscounters(_:region:miplevel:slice:).md)
  Encodes a command that resets a sparse texture’s access data for a specific region, mipmap level, and slice.

## Relationships

### Inherits From
- [MTLCommandEncoder](mtlcommandencoder.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [struct MTLBlitOption](mtlblitoption.md)
  The options that enable behavior for some blit operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlblitcommandencoder)*
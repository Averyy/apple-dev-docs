# MTLBlitCommandEncoder

**Framework**: Metal  
**Kind**: protocol  
**Role**: Protocol

Encodes commands that copy and modify resources for a single blit pass.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
protocol MTLBlitCommandEncoder : MTLCommandEncoder
```

```objc
@protocol MTLBlitCommandEncoder <MTLCommandEncoder>
```

## Mentions

- [Copying data into or out of mipmaps](./copying-data-into-or-out-of-mipmaps.md)
- [Understanding the Metal 4 core API](./understanding-the-metal-4-core-api.md)
- [Converting a GPU’s counter data into a readable format](./converting-a-gpus-counter-data-into-a-readable-format.md)
- [Sampling GPU data into counter sample buffers](./sampling-gpu-data-into-counter-sample-buffers.md)
- [Transferring data between connected GPUs](./transferring-data-between-connected-gpus.md)

#### Overview

Create a blit encoder by calling one of the factory methods on an [`MTLCommandBuffer`](./mtlcommandbuffer.md) instance, such as [`makeBlitCommandEncoder()`](./mtlcommandbuffer/makeblitcommandencoder%28%29.md).

A blit command encoder adds commands to a command buffer that modify resources in various ways, including:

- Filling buffers with repeating bytes
- Generating mipmaps for textures
- Copying data between buffers
- Copying data between textures
- Copying data between a texture and a buffer
- Managing the contents of indirect command buffers
- Synchronizing buffers, textures, and other resources between the CPU and GPU
- Improving runtime performance for resources by optimizing their memory layout for the GPU or CPU

You typically use these commands to move data between a resource that uses private storage and another resource that uses CPU-accessible storage. Some apps also use them to apply image-processing and texture effects, such as blurring or reflections, or to render and work with offscreen image data.

When you finish encoding blit commands, finalize the blit pass into the command buffer by calling the encoder’s [`endEncoding()`](./mtlcommandencoder/endencoding%28%29.md) method.

##### Command stages

Most blit commands apply to one stage within a pass. The following table shows which stages apply to each command:

| Function | MTLStages |
| --- | --- |
| [`fill(buffer:range:value:)`](./mtlblitcommandencoder/fill%28buffer,range,value%29.md) | [`blit`](./mtlstages/blit.md) |
| [`generateMipmaps(for:)`](./mtlblitcommandencoder/generatemipmaps%28for%29.md) | [`blit`](./mtlstages/blit.md) |
| [`copy(from:sourceOffset:to:destinationOffset:size:)`](./mtlblitcommandencoder/copy%28from,sourceoffset,to,destinationoffset,size%29.md) | [`blit`](./mtlstages/blit.md) |
| [`copy(from:to:)`](./mtlblitcommandencoder/copy%28from,to%29.md) | [`blit`](./mtlstages/blit.md) |
| [`copy(from:sourceSlice:sourceLevel:to:destinationSlice:destinationLevel:sliceCount:levelCount:)`](./mtlblitcommandencoder/copy%28from,sourceslice,sourcelevel,to,destinationslice,destinationlevel,slicecount,levelcount%29.md) | [`blit`](./mtlstages/blit.md) |
| [`copy(from:sourceSlice:sourceLevel:sourceOrigin:sourceSize:to:destinationSlice:destinationLevel:destinationOrigin:)`](./mtlblitcommandencoder/copy%28from,sourceslice,sourcelevel,sourceorigin,sourcesize,to,destinationslice,destinationlevel,destinationorigin%29.md) | [`blit`](./mtlstages/blit.md) |
| [`copy(from:sourceOrigin:sourceDimensions:to:destinationOrigin:destinationDimensions:)`](./mtlblitcommandencoder/copy%28from,sourceorigin,sourcedimensions,to,destinationorigin,destinationdimensions%29.md) | [`blit`](./mtlstages/blit.md) |
| [`copy(from:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:to:destinationSlice:destinationLevel:destinationOrigin:)`](./mtlblitcommandencoder/copy%28from,sourceoffset,sourcebytesperrow,sourcebytesperimage,sourcesize,to,destinationslice,destinationlevel,destinationorigin%29.md) | [`blit`](./mtlstages/blit.md) |
| [`copy(from:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:to:destinationSlice:destinationLevel:destinationOrigin:options:)`](./mtlblitcommandencoder/copy%28from,sourceoffset,sourcebytesperrow,sourcebytesperimage,sourcesize,to,destinationslice,destinationlevel,destinationorigin,options%29.md) | [`blit`](./mtlstages/blit.md) |
| [`copy(from:sourceSlice:sourceLevel:sourceOrigin:sourceSize:to:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:)`](./mtlblitcommandencoder/copy%28from,sourceslice,sourcelevel,sourceorigin,sourcesize,to,destinationoffset,destinationbytesperrow,destinationbytesperimage%29.md) | [`blit`](./mtlstages/blit.md) |
| [`copy(from:sourceSlice:sourceLevel:sourceOrigin:sourceSize:to:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:options:)`](./mtlblitcommandencoder/copy%28from,sourceslice,sourcelevel,sourceorigin,sourcesize,to,destinationoffset,destinationbytesperrow,destinationbytesperimage,options%29.md) | [`blit`](./mtlstages/blit.md) |
| [`optimizeContentsForGPUAccess(texture:)`](./mtlblitcommandencoder/optimizecontentsforgpuaccess%28texture%29.md) | [`blit`](./mtlstages/blit.md) |
| [`optimizeContentsForGPUAccess(texture:slice:level:)`](./mtlblitcommandencoder/optimizecontentsforgpuaccess%28texture,slice,level%29.md) | [`blit`](./mtlstages/blit.md) |
| [`optimizeContentsForCPUAccess(texture:)`](./mtlblitcommandencoder/optimizecontentsforcpuaccess%28texture%29.md) | [`blit`](./mtlstages/blit.md) |
| [`optimizeContentsForCPUAccess(texture:slice:level:)`](./mtlblitcommandencoder/optimizecontentsforcpuaccess%28texture,slice,level%29.md) | [`blit`](./mtlstages/blit.md) |
| [`synchronize(resource:)`](./mtlblitcommandencoder/synchronize%28resource%29.md) | None |
| [`synchronize(texture:slice:level:)`](./mtlblitcommandencoder/synchronize%28texture,slice,level%29.md) | None |
| [`copyIndirectCommandBuffer(_:sourceRange:destination:destinationIndex:)`](./mtlblitcommandencoder/copyindirectcommandbuffer%28_,sourcerange,destination,destinationindex%29.md) | [`blit`](./mtlstages/blit.md) |
| [`resetCommandsInBuffer(_:range:)`](./mtlblitcommandencoder/resetcommandsinbuffer%28_,range%29.md) | [`blit`](./mtlstages/blit.md) |
| [`optimizeIndirectCommandBuffer(_:range:)`](./mtlblitcommandencoder/optimizeindirectcommandbuffer%28_,range%29.md) | [`blit`](./mtlstages/blit.md) |
| [`sampleCounters(sampleBuffer:sampleIndex:barrier:)`](./mtlblitcommandencoder/samplecounters%28samplebuffer,sampleindex,barrier%29.md) | None |
| [`resolveCounters(_:range:destinationBuffer:destinationOffset:)`](./mtlblitcommandencoder/resolvecounters%28_,range,destinationbuffer,destinationoffset%29.md) | [`blit`](./mtlstages/blit.md) |
| [`getTextureAccessCounters(_:region:mipLevel:slice:resetCounters:countersBuffer:countersBufferOffset:)`](./mtlblitcommandencoder/gettextureaccesscounters%28_,region,miplevel,slice,resetcounters,countersbuffer,countersbufferoffset%29.md) | [`blit`](./mtlstages/blit.md) |
| [`resetTextureAccessCounters(_:region:mipLevel:slice:)`](./mtlblitcommandencoder/resettextureaccesscounters%28_,region,miplevel,slice%29.md) | [`blit`](./mtlstages/blit.md) |

For more information about stages and synchronization, see [`MTLStages`](./mtlstages.md) and [Resource synchronization](./resource-synchronization.md).

## Topics

### Filling buffers
- [func fill(buffer: any MTLBuffer, range: Range<Int>, value: UInt8)](./mtlblitcommandencoder/fill%28buffer,range,value%29.md)
  Encodes a command that fills a buffer with a constant value for each byte.
### Generating texture mipmaps
- [func generateMipmaps(for: any MTLTexture)](./mtlblitcommandencoder/generatemipmaps%28for%29.md)
  Encodes a command that generates mipmaps for a texture from the base mipmap level up to the highest mipmap level.
### Copying buffer data to another buffer
- [func copy(from: any MTLBuffer, sourceOffset: Int, to: any MTLBuffer, destinationOffset: Int, size: Int)](./mtlblitcommandencoder/copy%28from,sourceoffset,to,destinationoffset,size%29.md)
  Encodes a command that copies data from one buffer into another.
### Copying texture data to another texture
- [func copy(from: any MTLTexture, to: any MTLTexture)](./mtlblitcommandencoder/copy%28from,to%29.md)
  Encodes a command that copies data from one texture to another.
- [func copy(from: any MTLTexture, sourceSlice: Int, sourceLevel: Int, to: any MTLTexture, destinationSlice: Int, destinationLevel: Int, sliceCount: Int, levelCount: Int)](./mtlblitcommandencoder/copy%28from,sourceslice,sourcelevel,to,destinationslice,destinationlevel,slicecount,levelcount%29.md)
  Encodes a command that copies slices of a texture to another texture’s slices.
- [func copy(from: any MTLTexture, sourceSlice: Int, sourceLevel: Int, sourceOrigin: MTLOrigin, sourceSize: MTLSize, to: any MTLTexture, destinationSlice: Int, destinationLevel: Int, destinationOrigin: MTLOrigin)](./mtlblitcommandencoder/copy%28from,sourceslice,sourcelevel,sourceorigin,sourcesize,to,destinationslice,destinationlevel,destinationorigin%29.md)
  Encodes a command that copies image data from a texture’s slice into another slice.
- [func copy(from: any MTLTensor, sourceOrigin: MTLTensorExtents, sourceDimensions: MTLTensorExtents, to: any MTLTensor, destinationOrigin: MTLTensorExtents, destinationDimensions: MTLTensorExtents)](./mtlblitcommandencoder/copy%28from,sourceorigin,sourcedimensions,to,destinationorigin,destinationdimensions%29.md)
  Encodes a command to copy data from a slice of the data plane of a tensor into a slice of the data plane of another tensor.
### Copying buffer data to a texture
- [func copy(from: any MTLBuffer, sourceOffset: Int, sourceBytesPerRow: Int, sourceBytesPerImage: Int, sourceSize: MTLSize, to: any MTLTexture, destinationSlice: Int, destinationLevel: Int, destinationOrigin: MTLOrigin)](./mtlblitcommandencoder/copy%28from,sourceoffset,sourcebytesperrow,sourcebytesperimage,sourcesize,to,destinationslice,destinationlevel,destinationorigin%29.md)
  Encodes a command to copy image data from a source buffer into a destination texture.
- [func copy(from: any MTLBuffer, sourceOffset: Int, sourceBytesPerRow: Int, sourceBytesPerImage: Int, sourceSize: MTLSize, to: any MTLTexture, destinationSlice: Int, destinationLevel: Int, destinationOrigin: MTLOrigin, options: MTLBlitOption)](./mtlblitcommandencoder/copy%28from,sourceoffset,sourcebytesperrow,sourcebytesperimage,sourcesize,to,destinationslice,destinationlevel,destinationorigin,options%29.md)
  Encodes a command to copy image data from a source buffer into a destination texture.
### Copying texture data to a buffer
- [func copy(from: any MTLTexture, sourceSlice: Int, sourceLevel: Int, sourceOrigin: MTLOrigin, sourceSize: MTLSize, to: any MTLBuffer, destinationOffset: Int, destinationBytesPerRow: Int, destinationBytesPerImage: Int)](./mtlblitcommandencoder/copy%28from,sourceslice,sourcelevel,sourceorigin,sourcesize,to,destinationoffset,destinationbytesperrow,destinationbytesperimage%29.md)
  Encodes a command that copies image data from a texture slice to a buffer.
- [func copy(from: any MTLTexture, sourceSlice: Int, sourceLevel: Int, sourceOrigin: MTLOrigin, sourceSize: MTLSize, to: any MTLBuffer, destinationOffset: Int, destinationBytesPerRow: Int, destinationBytesPerImage: Int, options: MTLBlitOption)](./mtlblitcommandencoder/copy%28from,sourceslice,sourcelevel,sourceorigin,sourcesize,to,destinationoffset,destinationbytesperrow,destinationbytesperimage,options%29.md)
  Encodes a command that copies image data from a texture slice to a buffer, and provides options for special texture formats.
### Optimizing textures for GPU access
- [func optimizeContentsForGPUAccess(texture: any MTLTexture)](./mtlblitcommandencoder/optimizecontentsforgpuaccess%28texture%29.md)
  Encodes a command that improves the performance of GPU memory operations with a texture.
- [func optimizeContentsForGPUAccess(texture: any MTLTexture, slice: Int, level: Int)](./mtlblitcommandencoder/optimizecontentsforgpuaccess%28texture,slice,level%29.md)
  Encodes a command that improves the performance of GPU memory operations with a specific portion of a texture.
### Optimizing textures for CPU access
- [func optimizeContentsForCPUAccess(texture: any MTLTexture)](./mtlblitcommandencoder/optimizecontentsforcpuaccess%28texture%29.md)
  Encodes a command that improves the performance of CPU memory operations with a texture.
- [func optimizeContentsForCPUAccess(texture: any MTLTexture, slice: Int, level: Int)](./mtlblitcommandencoder/optimizecontentsforcpuaccess%28texture,slice,level%29.md)
  Encodes a command that improves the performance of CPU memory operations with a specific portion of a texture.
### Synchronizing managed resources
- [func synchronize(resource: any MTLResource)](./mtlblitcommandencoder/synchronize%28resource%29.md)
  Encodes a command that synchronizes the CPU’s copy of a managed resource, such as a buffer or texture, so that it matches the GPU’s copy.
- [func synchronize(texture: any MTLTexture, slice: Int, level: Int)](./mtlblitcommandencoder/synchronize%28texture,slice,level%29.md)
  Encodes a command that synchronizes a part of the CPU’s copy of a texture so that it matches the GPU’s copy.
### Preventing resource access conflicts
- [func waitForFence(any MTLFence)](./mtlblitcommandencoder/waitforfence%28_%29.md)
  Encodes a command that instructs the GPU to pause the blit pass until another pass updates a fence.
- [func updateFence(any MTLFence)](./mtlblitcommandencoder/updatefence%28_%29.md)
  Encodes a command that instructs the GPU to update a fence after the blit pass completes.
### Managing indirect command buffers
- [func copyIndirectCommandBuffer(any MTLIndirectCommandBuffer, sourceRange: Range<Int>, destination: any MTLIndirectCommandBuffer, destinationIndex: Int)](./mtlblitcommandencoder/copyindirectcommandbuffer%28_,sourcerange,destination,destinationindex%29.md)
  Encodes a command that copies commands from one indirect command buffer into another.
- [func resetCommandsInBuffer(any MTLIndirectCommandBuffer, range: Range<Int>)](./mtlblitcommandencoder/resetcommandsinbuffer%28_,range%29.md)
  Encodes a command that resets a range of commands in an indirect command buffer.
- [func optimizeIndirectCommandBuffer(any MTLIndirectCommandBuffer, range: Range<Int>)](./mtlblitcommandencoder/optimizeindirectcommandbuffer%28_,range%29.md)
  Encodes a command that can improve the performance of a range of commands within an indirect command buffer.
### Sampling counters
- [func sampleCounters(sampleBuffer: any MTLCounterSampleBuffer, sampleIndex: Int, barrier: Bool)](./mtlblitcommandencoder/samplecounters%28samplebuffer,sampleindex,barrier%29.md)
  Encodes a command that samples the GPU’s hardware counters during a blit pass and stores the data in a counter sample buffer.
- [func resolveCounters(any MTLCounterSampleBuffer, range: Range<Int>, destinationBuffer: any MTLBuffer, destinationOffset: Int)](./mtlblitcommandencoder/resolvecounters%28_,range,destinationbuffer,destinationoffset%29.md)
  Encodes a command that resolves the data from the samples in a sample counter buffer and stores the results into a buffer.
### Managing sparse texture access counters
- [func getTextureAccessCounters(any MTLTexture, region: MTLRegion, mipLevel: Int, slice: Int, resetCounters: Bool, countersBuffer: any MTLBuffer, countersBufferOffset: Int)](./mtlblitcommandencoder/gettextureaccesscounters%28_,region,miplevel,slice,resetcounters,countersbuffer,countersbufferoffset%29.md)
  Encodes a command that retrieves a sparse texture’s access data for a specific region, mipmap level, and slice.
- [func resetTextureAccessCounters(any MTLTexture, region: MTLRegion, mipLevel: Int, slice: Int)](./mtlblitcommandencoder/resettextureaccesscounters%28_,region,miplevel,slice%29.md)
  Encodes a command that resets a sparse texture’s access data for a specific region, mipmap level, and slice.
### Instance Methods
- [func copy(from: any MTLTensor, sourceOrigin: MTLTensorExtents, sourceDimensions: MTLTensorExtents, sourcePlane: MTLTensorPlaneType, to: any MTLTensor, destinationOrigin: MTLTensorExtents, destinationDimensions: MTLTensorExtents, destinationPlane: MTLTensorPlaneType)](./mtlblitcommandencoder/copy%28from,sourceorigin,sourcedimensions,sourceplane,to,destinationorigin,destinationdimensions,destinationplane%29.md)
  Encodes a command to copy data from a slice of a plane of a tensor into a slice of a plane of another tensor.

## Relationships

### Inherits From
- [MTLCommandEncoder](./mtlcommandencoder.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Encoding a blit pass
- [struct MTLBlitOption](./mtlblitoption.md)
  The options that enable behavior for some blit operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlblitcommandencoder)*
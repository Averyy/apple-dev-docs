# MTLIndirectComputeCommand

**Framework**: Metal  
**Kind**: protocol

A compute command in an indirect command buffer.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol MTLIndirectComputeCommand : NSObjectProtocol
```

#### Overview

Don’t implement this protocol; you get instances of this type by asking an [`MTLIndirectCommandBuffer`](mtlindirectcommandbuffer.md) for them.

Use this instance to reset or encode a command. You need to reset a command before encoding a new command.

## Topics

### Setting a command’s arguments
- [func setComputePipelineState(any MTLComputePipelineState)](mtlindirectcomputecommand/setcomputepipelinestate(_:).md)
  Sets the command’s compute pipeline state.
- [func setImageblockWidth(Int, height: Int)](mtlindirectcomputecommand/setimageblockwidth(_:height:).md)
  Sets the size, in pixels, of the imageblock.
- [func setKernelBuffer(any MTLBuffer, offset: Int, at: Int)](mtlindirectcomputecommand/setkernelbuffer(_:offset:at:).md)
  Sets a buffer for the compute function.
- [func setThreadgroupMemoryLength(Int, index: Int)](mtlindirectcomputecommand/setthreadgroupmemorylength(_:index:).md)
  Sets the size of a block of threadgroup memory.
- [func setThreadgroupMemoryLength(Int, at: Int)](mtlindirectcomputecommand/setthreadgroupmemorylength(_:at:).md)
  Sets the size of a block of threadgroup memory.
- [func setStageInRegion(MTLRegion)](mtlindirectcomputecommand/setstageinregion(_:).md)
  Sets the region of the stage-in attributes to apply to the compute kernel.
- [func setStageIn(MTLRegion)](mtlindirectcomputecommand/setstagein(_:).md)
  Sets the region of the stage-in attributes to apply to the compute kernel.
### Synchronizing command execution
- [func setBarrier()](mtlindirectcomputecommand/setbarrier.md)
  Adds a barrier to ensure that commands executed prior to this command are complete before this command executes.
- [func clearBarrier()](mtlindirectcomputecommand/clearbarrier.md)
  Removes any barrier set on the command.
### Encoding a compute command
- [func concurrentDispatchThreadgroups(MTLSize, threadsPerThreadgroup: MTLSize)](mtlindirectcomputecommand/concurrentdispatchthreadgroups(_:threadsperthreadgroup:).md)
  Encodes a compute command using a grid aligned to threadgroup boundaries.
- [func concurrentDispatchThreads(MTLSize, threadsPerThreadgroup: MTLSize)](mtlindirectcomputecommand/concurrentdispatchthreads(_:threadsperthreadgroup:).md)
  Encodes a compute command using an arbitrarily sized grid.
### Resetting a command
- [func reset()](mtlindirectcomputecommand/reset.md)
  Resets the command to its default state.
### Instance Methods
- [func setKernelBuffer(any MTLBuffer, offset: Int, attributeStride: Int, at: Int)](mtlindirectcomputecommand/setkernelbuffer(_:offset:attributestride:at:).md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [struct MTLRegion](mtlregion.md)
  The bounds for a subset of an instance’s elements.
- [struct MTLSize](mtlsize.md)
  A type that represents one, two, or three dimensions of a type instance, such as an array or texture.
- [struct MTLOrigin](mtlorigin.md)
  The coordinates for the front upper-left corner of a region.
- [struct MTLStageInRegionIndirectArguments](mtlstageinregionindirectarguments.md)
  The data layout required for the arguments needed to specify the stage-in region.
- [struct MTLDispatchThreadgroupsIndirectArguments](mtldispatchthreadgroupsindirectarguments.md)
  The data layout required for arguments needed to specify the size of threadgroups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlindirectcomputecommand)*
# setComputePipelineState(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Sets the command’s compute pipeline state object.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func setComputePipelineState(_ pipelineState: any MTLComputePipelineState)
```

#### Discussion

If you created the indirect command buffer with [`inheritPipelineState`](mtlindirectcommandbufferdescriptor/inheritpipelinestate.md) set to [`true`](https://developer.apple.com/documentation/swift/true), do not call this method. The command gets the pipeline state object from the parent encoder when you execute the command.

If you created the indirect command buffer with [`inheritPipelineState`](mtlindirectcommandbufferdescriptor/inheritpipelinestate.md) set to [`false`](https://developer.apple.com/documentation/swift/false), you must set the pipeline state prior to encoding the drawing command.

## Parameters

- `pipelineState`: The compute pipeline state object to use.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlindirectcomputecommand/setcomputepipelinestate(_:))*
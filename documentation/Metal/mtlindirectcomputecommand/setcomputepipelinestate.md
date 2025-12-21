# setComputePipelineState(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Sets the command’s compute pipeline state.

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

You don’t need to call this method if you create an indirect command buffer with its [`inheritPipelineState`](mtlindirectcommandbufferdescriptor/inheritpipelinestate.md) property equal to [`true`](https://developer.apple.com/documentation/Swift/true). The command gets the pipeline state from the parent encoder when you run the command.

If you create an indirect command buffer with its [`inheritPipelineState`](mtlindirectcommandbufferdescriptor/inheritpipelinestate.md) property equal to [`false`](https://developer.apple.com/documentation/Swift/false), you need to set the pipeline state prior to encoding a drawing command.

## Parameters

- `pipelineState`: A compute pipeline state instance.

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
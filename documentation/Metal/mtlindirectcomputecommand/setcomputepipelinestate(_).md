# setComputePipelineState(_:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (void) setComputePipelineState:(id<MTLComputePipelineState>) pipelineState;
```

#### Discussion

You don’t need to call this method if you create an indirect command buffer with its [`inheritPipelineState`](../mtlindirectcommandbufferdescriptor/inheritpipelinestate.md) property equal to [`true`](../../Swift/true.md). The command gets the pipeline state from the parent encoder when you run the command.

If you create an indirect command buffer with its [`inheritPipelineState`](../mtlindirectcommandbufferdescriptor/inheritpipelinestate.md) property equal to [`false`](../../Swift/false.md), you need to set the pipeline state prior to encoding a drawing command.

## Parameters

- `pipelineState`: A compute pipeline state instance.

## See Also

### Setting a command’s arguments
- [func setImageblockWidth(Int, height: Int)](./setimageblockwidth%28_,height%29.md)
  Sets the size, in pixels, of the imageblock.
- [func setKernelBuffer(any MTLBuffer, offset: Int, at: Int)](./setkernelbuffer%28_,offset,at%29.md)
  Sets a buffer for the compute function.
- [func setThreadgroupMemoryLength(Int, index: Int)](./setthreadgroupmemorylength%28_,index%29.md)
  Sets the size of a block of threadgroup memory.
- [func setThreadgroupMemoryLength(Int, at: Int)](./setthreadgroupmemorylength%28_,at%29.md)
  Sets the size of a block of threadgroup memory.
- [func setStageInRegion(MTLRegion)](./setstageinregion%28_%29.md)
  Sets the region of the stage-in attributes to apply to the compute kernel.
- [func setStageIn(MTLRegion)](./setstagein%28_%29.md)
  Sets the region of the stage-in attributes to apply to the compute kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlindirectcomputecommand/setcomputepipelinestate(_:))*
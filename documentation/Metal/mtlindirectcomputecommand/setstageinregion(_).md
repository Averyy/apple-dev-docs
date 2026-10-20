# setStageInRegion(_:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sets the region of the stage-in attributes to apply to the compute kernel.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func setStageInRegion(_ region: MTLRegion)
```

```objc
- (void) setStageInRegion:(MTLRegion) region;
```

## Parameters

- `region`: The offset and maximum size of the grid over which compute threads that read per-thread stage-in data are launched.

## See Also

### Setting a command’s arguments
- [func setComputePipelineState(any MTLComputePipelineState)](./setcomputepipelinestate%28_%29.md)
  Sets the command’s compute pipeline state.
- [func setImageblockWidth(Int, height: Int)](./setimageblockwidth%28_,height%29.md)
  Sets the size, in pixels, of the imageblock.
- [func setKernelBuffer(any MTLBuffer, offset: Int, at: Int)](./setkernelbuffer%28_,offset,at%29.md)
  Sets a buffer for the compute function.
- [func setThreadgroupMemoryLength(Int, index: Int)](./setthreadgroupmemorylength%28_,index%29.md)
  Sets the size of a block of threadgroup memory.
- [func setThreadgroupMemoryLength(Int, at: Int)](./setthreadgroupmemorylength%28_,at%29.md)
  Sets the size of a block of threadgroup memory.
- [func setStageIn(MTLRegion)](./setstagein%28_%29.md)
  Sets the region of the stage-in attributes to apply to the compute kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlindirectcomputecommand/setstageinregion(_:))*
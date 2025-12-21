# setStageIn(_:)

**Framework**: Metal  
**Kind**: method

Sets the region of the stage-in attributes to apply to the compute kernel.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- tvOS 13.0+
- visionOS ?+

## Declaration

```swift
func setStageIn(_ region: MTLRegion)
```

## Parameters

- `region`: The offset and maximum size of the grid over which compute threads that read per-thread stage-in data are launched.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlindirectcomputecommand/setstagein(_:))*
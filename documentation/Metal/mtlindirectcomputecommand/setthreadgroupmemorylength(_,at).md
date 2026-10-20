# setThreadgroupMemoryLength(_:at:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Sets the size of a block of threadgroup memory.

**Availability**:
- iOS 13.0+ - Deprecated in 14.0 (renamed: setThreadgroupMemoryLength(_:index:))
- iPadOS 13.0+ - Deprecated in 14.0 (renamed: setThreadgroupMemoryLength(_:index:))
- Mac Catalyst 14.0+ - Deprecated in 14.0 (renamed: setThreadgroupMemoryLength(_:index:))
- tvOS 13.0+ - Deprecated in 14.0 (renamed: setThreadgroupMemoryLength(_:index:))
- visionOS

## Declaration

```swift
func setThreadgroupMemoryLength(_ length: Int, at index: Int)
```

## Parameters

- `length`: The size of the threadgroup memory, in bytes, which needs to be a multiple of 16 bytes.
- `index`: The index in the threadgroup memory argument table.

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
- [func setStageInRegion(MTLRegion)](./setstageinregion%28_%29.md)
  Sets the region of the stage-in attributes to apply to the compute kernel.
- [func setStageIn(MTLRegion)](./setstagein%28_%29.md)
  Sets the region of the stage-in attributes to apply to the compute kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlindirectcomputecommand/setthreadgroupmemorylength(_:at:))*
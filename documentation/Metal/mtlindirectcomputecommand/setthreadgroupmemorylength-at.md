# setThreadgroupMemoryLength(_:at:)

**Framework**: Metal  
**Kind**: method

Sets the size of a block of threadgroup memory.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- tvOS 13.0+
- visionOS ?+

## Declaration

```swift
func setThreadgroupMemoryLength(_ length: Int, at index: Int)
```

## Parameters

- `length`: The size of the threadgroup memory, in bytes. Must be a multiple of 16 bytes.
- `index`: The index in the threadgroup memory argument table.

## See Also

- [func setComputePipelineState(any MTLComputePipelineState)](mtlindirectcomputecommand/setcomputepipelinestate(_:).md)
  Sets the command’s compute pipeline state object.
- [func setImageblockWidth(Int, height: Int)](mtlindirectcomputecommand/setimageblockwidth(_:height:).md)
  Sets the size, in pixels, of the imageblock.
- [func setKernelBuffer(any MTLBuffer, offset: Int, at: Int)](mtlindirectcomputecommand/setkernelbuffer(_:offset:at:).md)
  Sets a buffer for the compute function.
- [func setThreadgroupMemoryLength(Int, index: Int)](mtlindirectcomputecommand/setthreadgroupmemorylength(_:index:).md)
  Sets the size of a block of threadgroup memory.
- [func setStageInRegion(MTLRegion)](mtlindirectcomputecommand/setstageinregion(_:).md)
  Sets the region of the stage-in attributes to apply to the compute kernel.
- [func setStageIn(MTLRegion)](mtlindirectcomputecommand/setstagein(_:).md)
  Sets the region of the stage-in attributes to apply to the compute kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlindirectcomputecommand/setthreadgroupmemorylength(_:at:))*
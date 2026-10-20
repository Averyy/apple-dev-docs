# setImageblockWidth(_:height:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sets the size, in pixels, of the imageblock.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func setImageblockWidth(_ width: Int, height: Int)
```

```objc
- (void) setImageblockWidth:(NSUInteger) width height:(NSUInteger) height;
```

## Parameters

- `width`: The width of the imageblock.
- `height`: The height of the imageblock.

## See Also

### Setting a command’s arguments
- [func setComputePipelineState(any MTLComputePipelineState)](./setcomputepipelinestate%28_%29.md)
  Sets the command’s compute pipeline state.
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

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlindirectcomputecommand/setimageblockwidth(_:height:))*
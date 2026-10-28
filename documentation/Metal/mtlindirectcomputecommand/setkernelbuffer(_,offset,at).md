# setKernelBuffer(_:offset:at:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sets a buffer for the compute function.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func setKernelBuffer(_ buffer: any MTLBuffer, offset: Int, at index: Int)
```

```objc
- (void) setKernelBuffer:(id<MTLBuffer>) buffer offset:(NSUInteger) offset atIndex:(NSUInteger) index;
```

## Discussion

If you created the indirect command buffer with [`inheritBuffers`](../mtlindirectcommandbufferdescriptor/inheritbuffers.md) set to [`true`](../../Swift/true.md), don’t call this method. The command gets the arguments from the parent encoder when you execute the command.

If you need to pass other kinds of parameters to your shader, such as textures and samplers, create an argument buffer and pass it to the shader using this method.

## Parameters

- `buffer`: The buffer to set in the buffer argument table.
- `offset`: Where the data begins, in bytes, from the start of the buffer.
- `index`: An index in the buffer argument table.

## See Also

### Setting a command’s arguments
- [func setComputePipelineState(any MTLComputePipelineState)](./setcomputepipelinestate%28_%29.md)
  Sets the command’s compute pipeline state.
- [func setImageblockWidth(Int, height: Int)](./setimageblockwidth%28_,height%29.md)
  Sets the size, in pixels, of the imageblock.
- [func setThreadgroupMemoryLength(Int, index: Int)](./setthreadgroupmemorylength%28_,index%29.md)
  Sets the size of a block of threadgroup memory.
- [func setThreadgroupMemoryLength(Int, at: Int)](./setthreadgroupmemorylength%28_,at%29.md)
  Sets the size of a block of threadgroup memory.
- [func setStageInRegion(MTLRegion)](./setstageinregion%28_%29.md)
  Sets the region of the stage-in attributes to apply to the compute kernel.
- [func setStageIn(MTLRegion)](./setstagein%28_%29.md)
  Sets the region of the stage-in attributes to apply to the compute kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlindirectcomputecommand/setkernelbuffer(_:offset:at:))*
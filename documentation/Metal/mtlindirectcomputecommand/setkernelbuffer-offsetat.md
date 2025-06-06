# setKernelBuffer(_:offset:at:)

**Framework**: Metal  
**Kind**: method  
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

#### Discussion

If you created the indirect command buffer with [`inheritBuffers`](mtlindirectcommandbufferdescriptor/inheritbuffers.md) set to [`true`](https://developer.apple.com/documentation/swift/true), don’t call this method. The command gets the arguments from the parent encoder when you execute the command.

If you need to pass other kinds of parameters to your shader, such as textures and samplers, create an argument buffer and pass it to the shader using this method.

## Parameters

- `buffer`: The buffer to set in the buffer argument table.
- `offset`: Where the data begins, in bytes, from the start of the buffer.
- `index`: An index in the buffer argument table.

## See Also

- [func setComputePipelineState(any MTLComputePipelineState)](mtlindirectcomputecommand/setcomputepipelinestate(_:).md)
  Sets the command’s compute pipeline state object.
- [func setImageblockWidth(Int, height: Int)](mtlindirectcomputecommand/setimageblockwidth(_:height:).md)
  Sets the size, in pixels, of the imageblock.
- [func setThreadgroupMemoryLength(Int, index: Int)](mtlindirectcomputecommand/setthreadgroupmemorylength(_:index:).md)
  Sets the size of a block of threadgroup memory.
- [func setThreadgroupMemoryLength(Int, at: Int)](mtlindirectcomputecommand/setthreadgroupmemorylength(_:at:).md)
  Sets the size of a block of threadgroup memory.
- [func setStageInRegion(MTLRegion)](mtlindirectcomputecommand/setstageinregion(_:).md)
  Sets the region of the stage-in attributes to apply to the compute kernel.
- [func setStageIn(MTLRegion)](mtlindirectcomputecommand/setstagein(_:).md)
  Sets the region of the stage-in attributes to apply to the compute kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlindirectcomputecommand/setkernelbuffer(_:offset:at:))*
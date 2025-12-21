# setThreadgroupMemoryLength(_:index:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Configures the size of a threadgroup memory buffer for a threadgroup argument in the compute shader function.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func setThreadgroupMemoryLength(_ length: Int, index: Int)
```

## Parameters

- `length`: The size of the threadgroup memory, in bytes. Use a multiple of   bytes.
- `index`: An integer that corresponds to the index of the argument you annotate with attribute    in the shader function.

## See Also

- [func setComputePipelineState(any MTLComputePipelineState)](mtl4computecommandencoder/setcomputepipelinestate(_:).md)
  Configures this encoder with a compute pipeline state that applies to your subsequent dispatch commands.
- [func setArgumentTable((any MTL4ArgumentTable)?)](mtl4computecommandencoder/setargumenttable(_:).md)
  Sets an argument table for the compute shader stage of this pipeline.
- [func setImageblockSize(width: Int, height: Int)](mtl4computecommandencoder/setimageblocksize(width:height:).md)
  Specifies the size, in pixels, of imageblock data in tile memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder/setthreadgroupmemorylength(_:index:))*
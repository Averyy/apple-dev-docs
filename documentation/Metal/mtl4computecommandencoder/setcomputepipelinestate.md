# setComputePipelineState(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Configures this encoder with a compute pipeline state that applies to your subsequent dispatch commands.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func setComputePipelineState(_ state: any MTLComputePipelineState)
```

## Parameters

- `state`: A non-   .

## See Also

- [func setArgumentTable((any MTL4ArgumentTable)?)](mtl4computecommandencoder/setargumenttable(_:).md)
  Sets an argument table for the compute shader stage of this pipeline.
- [func setThreadgroupMemoryLength(Int, index: Int)](mtl4computecommandencoder/setthreadgroupmemorylength(_:index:).md)
  Configures the size of a threadgroup memory buffer for a threadgroup argument in the compute shader function.
- [func setImageblockSize(width: Int, height: Int)](mtl4computecommandencoder/setimageblocksize(width:height:).md)
  Specifies the size, in pixels, of imageblock data in tile memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder/setcomputepipelinestate(_:))*
# setArgumentTable(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Sets an argument table for the compute shader stage of this pipeline.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func setArgumentTable(_ argumentTable: (any MTL4ArgumentTable)?)
```

#### Discussion

Metal takes a snapshot of the resources in the argument table when you make dispatch or execute calls on this encoder instance. Metal makes the snapshot contents available to the compute shader function of the current pipeline state.

## Parameters

- `argumentTable`: A   to set on the command encoder.

## See Also

- [func setComputePipelineState(any MTLComputePipelineState)](mtl4computecommandencoder/setcomputepipelinestate(_:).md)
  Configures this encoder with a compute pipeline state that applies to your subsequent dispatch commands.
- [func setThreadgroupMemoryLength(Int, index: Int)](mtl4computecommandencoder/setthreadgroupmemorylength(_:index:).md)
  Configures the size of a threadgroup memory buffer for a threadgroup argument in the compute shader function.
- [func setImageblockSize(width: Int, height: Int)](mtl4computecommandencoder/setimageblocksize(width:height:).md)
  Specifies the size, in pixels, of imageblock data in tile memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder/setargumenttable(_:))*
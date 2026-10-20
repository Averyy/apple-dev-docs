# setArgumentTable(_:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (void) setArgumentTable:(id<MTL4ArgumentTable>) argumentTable;
```

#### Discussion

Metal takes a snapshot of the resources in the argument table when you make dispatch or execute calls on this encoder instance. Metal makes the snapshot contents available to the compute shader function of the current pipeline state.

## Parameters

- `argumentTable`: A [`MTL4ArgumentTable`](../mtl4argumenttable.md) to set on the command encoder.

## See Also

### Configuring the pass
- [func setComputePipelineState(any MTLComputePipelineState)](./setcomputepipelinestate%28_%29.md)
  Configures this encoder with a compute pipeline state that applies to your subsequent dispatch commands.
- [func setThreadgroupMemoryLength(Int, index: Int)](./setthreadgroupmemorylength%28_,index%29.md)
  Configures the size of a threadgroup memory buffer for a threadgroup argument in the compute shader function.
- [func setImageblockSize(width: Int, height: Int)](./setimageblocksize%28width,height%29.md)
  Specifies the size, in pixels, of imageblock data in tile memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder/setargumenttable(_:))*
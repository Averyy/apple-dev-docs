# setComputePipelineState(_:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (void) setComputePipelineState:(id<MTLComputePipelineState>) state;
```

## Parameters

- `state`: A non-`nil` [`MTLComputePipelineState`](../mtlcomputepipelinestate.md).

## See Also

### Configuring the pass
- [func setArgumentTable((any MTL4ArgumentTable)?)](./setargumenttable%28_%29.md)
  Sets an argument table for the compute shader stage of this pipeline.
- [func setThreadgroupMemoryLength(Int, index: Int)](./setthreadgroupmemorylength%28_,index%29.md)
  Configures the size of a threadgroup memory buffer for a threadgroup argument in the compute shader function.
- [func setImageblockSize(width: Int, height: Int)](./setimageblocksize%28width,height%29.md)
  Specifies the size, in pixels, of imageblock data in tile memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder/setcomputepipelinestate(_:))*
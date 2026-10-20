# setImageblockSize(width:height:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Specifies the size, in pixels, of imageblock data in tile memory.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func setImageblockSize(width: Int, height: Int)
```

```objc
- (void) setImageblockWidth:(NSUInteger) width height:(NSUInteger) height;
```

## Parameters

- `width`: The width of the imageblock, in pixels.
- `height`: The height of the imageblock, in pixels.

## See Also

### Configuring the pass
- [func setComputePipelineState(any MTLComputePipelineState)](./setcomputepipelinestate%28_%29.md)
  Configures this encoder with a compute pipeline state that applies to your subsequent dispatch commands.
- [func setArgumentTable((any MTL4ArgumentTable)?)](./setargumenttable%28_%29.md)
  Sets an argument table for the compute shader stage of this pipeline.
- [func setThreadgroupMemoryLength(Int, index: Int)](./setthreadgroupmemorylength%28_,index%29.md)
  Configures the size of a threadgroup memory buffer for a threadgroup argument in the compute shader function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder/setimageblocksize(width:height:))*
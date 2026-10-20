# setThreadgroupMemoryLength(_:index:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (void) setThreadgroupMemoryLength:(NSUInteger) length atIndex:(NSUInteger) index;
```

## Parameters

- `length`: The size of the threadgroup memory, in bytes. Use a multiple of `16` bytes.
- `index`: An integer that corresponds to the index of the argument you annotate with attribute `[[threadgroup(index)]]` in the shader function.

## See Also

### Configuring the pass
- [func setComputePipelineState(any MTLComputePipelineState)](./setcomputepipelinestate%28_%29.md)
  Configures this encoder with a compute pipeline state that applies to your subsequent dispatch commands.
- [func setArgumentTable((any MTL4ArgumentTable)?)](./setargumenttable%28_%29.md)
  Sets an argument table for the compute shader stage of this pipeline.
- [func setImageblockSize(width: Int, height: Int)](./setimageblocksize%28width,height%29.md)
  Specifies the size, in pixels, of imageblock data in tile memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder/setthreadgroupmemorylength(_:index:))*
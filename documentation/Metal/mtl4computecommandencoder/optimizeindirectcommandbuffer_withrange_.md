# optimizeIndirectCommandBuffer:withRange:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Encode a command to attempt to improve the performance of a range of commands within an indirect command buffer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
- (void) optimizeIndirectCommandBuffer:(id<MTLIndirectCommandBuffer>) indirectCommandBuffer withRange:(NSRange) range;
```

## Parameters

- `indirectCommandBuffer`: An [`MTLIndirectCommandBuffer`](../mtlindirectcommandbuffer.md) instance that this command optimizes.
- `range`: A range of commands within `indirectCommandBuffer`.

## See Also

### Encoding optimization commands
- [func optimizeContents(forCPUAccess: any MTLTexture)](./optimizecontents%28forcpuaccess%29.md)
  Encodes a command that modifies the contents of a texture to improve the performance of CPU accesses to its contents.
- [func optimizeContents(forCPUAccess: any MTLTexture, slice: Int, level: Int)](./optimizecontents%28forcpuaccess,slice,level%29.md)
  Encodes a command that modifies the contents of a texture to improve the performance of CPU accesses to its contents in a specific region.
- [func optimizeContents(forGPUAccess: any MTLTexture)](./optimizecontents%28forgpuaccess%29.md)
  Encodes a command that modifies the contents of a texture to improve the performance of GPU accesses to its contents.
- [func optimizeContents(forGPUAccess: any MTLTexture, slice: Int, level: Int)](./optimizecontents%28forgpuaccess,slice,level%29.md)
  Encodes a command that modifies the contents of a texture instance to improve the performance of GPU accesses to its contents in a specific region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder/optimizeindirectcommandbuffer:withrange:)*
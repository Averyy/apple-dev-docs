# setIndirectCommandBuffers:withRange:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Encodes an array of indirect command buffers into the argument buffer.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```objc
- (void) setIndirectCommandBuffers:(id<MTLIndirectCommandBuffer> const[]) buffers withRange:(NSRange) range;
```

## Parameters

- `buffers`: An array of indirect command buffers the method encodes.
- `range`: A range of indices within the argument buffer for each element in `buffers`. The values correspond to either the index IDs of declarations in Metal Shading Language (MSL) or the [`index`](../mtlargumentdescriptor/index.md) property of [`MTLArgumentDescriptor`](../mtlargumentdescriptor.md) instances.

## See Also

### Encoding indirect command buffers
- [func setIndirectCommandBuffer((any MTLIndirectCommandBuffer)?, index: Int)](./setindirectcommandbuffer%28_,index%29.md)
  Encodes a reference to an indirect command buffer into the argument buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlargumentencoder/setindirectcommandbuffers:withrange:)*
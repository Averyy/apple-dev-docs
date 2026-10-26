# setComputePipelineStates:withRange:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Encodes references to an array of compute pipeline states into the argument buffer.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```objc
- (void) setComputePipelineStates:(id<MTLComputePipelineState> const[]) pipelines withRange:(NSRange) range;
```

## Parameters

- `pipelines`: An array of pipeline states the method encodes.
- `range`: A range of indices within the argument buffer for each element in `pipelines`. The values correspond to either the index IDs of declarations in Metal Shading Language (MSL) or the [`index`](../mtlargumentdescriptor/index.md) property of [`MTLArgumentDescriptor`](../mtlargumentdescriptor.md) instances.

## See Also

### Encoding pipeline states
- [func setRenderPipelineState((any MTLRenderPipelineState)?, index: Int)](./setrenderpipelinestate%28_,index%29.md)
  Encodes a reference to a render pipeline state into the argument buffer.
- [- setRenderPipelineStates:withRange:](./setrenderpipelinestates_withrange_.md)
  Encodes references to an array of render pipeline states into the argument buffer.
- [func setComputePipelineState((any MTLComputePipelineState)?, index: Int)](./setcomputepipelinestate%28_,index%29.md)
  Encodes a reference to a compute pipeline state into the argument buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlargumentencoder/setcomputepipelinestates:withrange:)*
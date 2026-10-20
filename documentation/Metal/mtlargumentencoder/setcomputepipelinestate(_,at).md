# setComputePipelineState(_:at:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Encodes a reference to a compute pipeline state into the argument buffer.

**Availability**:
- iOS 13.0+ - Deprecated in 14.0 (renamed: setComputePipelineState)
- iPadOS 13.0+ - Deprecated in 14.0 (renamed: setComputePipelineState)
- tvOS 13.0+ - Deprecated in 14.0 (renamed: setComputePipelineState)
- visionOS

## Declaration

```swift
func setComputePipelineState(_ pipeline: (any MTLComputePipelineState)?, at index: Int)
```

## Parameters

- `pipeline`: A pipeline state the method encodes.
- `index`: The index of a pipeline state within the argument buffer. The value corresponds to either the index ID of a declaration in Metal Shading Language (MSL) or the [`index`](../mtlargumentdescriptor/index.md) property of an [`MTLArgumentDescriptor`](../mtlargumentdescriptor.md) instance.

## See Also

### Encoding pipeline states
- [func setRenderPipelineState((any MTLRenderPipelineState)?, index: Int)](./setrenderpipelinestate%28_,index%29.md)
  Encodes a reference to a render pipeline state into the argument buffer.
- [func setRenderPipelineStates([(any MTLRenderPipelineState)?], range: Range<Int>)](./setrenderpipelinestates%28_,range%29.md)
  Encodes references to an array of render pipeline states into the argument buffer.
- [func setComputePipelineState((any MTLComputePipelineState)?, index: Int)](./setcomputepipelinestate%28_,index%29.md)
  Encodes a reference to a compute pipeline state into the argument buffer.
- [func setComputePipelineStates(UnsafePointer<(any MTLComputePipelineState)?>, with: NSRange)](./setcomputepipelinestates%28_,with%29.md)
  Encodes references to an array of compute pipeline states into the argument buffer.
- [func setComputePipelineStates([(any MTLComputePipelineState)?], range: Range<Int>)](./setcomputepipelinestates%28_,range%29.md)
  Encodes references to an array of compute pipeline states into the argument buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlargumentencoder/setcomputepipelinestate(_:at:))*
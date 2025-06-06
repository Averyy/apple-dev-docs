# setComputePipelineStates(_:with:)

**Framework**: Metal  
**Kind**: method

Encodes references to an array of compute pipeline states into the argument buffer.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.13+
- tvOS 13.0+
- visionOS ?+

## Declaration

```swift
func setComputePipelineStates(_ pipelines: UnsafePointer<(any MTLComputePipelineState)?>, with range: NSRange)
```

## Parameters

- `pipelines`: An array of pipeline states the method encodes.
- `range`: A range of indices within the argument buffer for each element in  .   The values correspond to either the index IDs of declarations in   Metal Shading Language (MSL) or the   property   of   instances.

## See Also

- [func setRenderPipelineState((any MTLRenderPipelineState)?, index: Int)](mtlargumentencoder/setrenderpipelinestate(_:index:).md)
  Encodes a reference to a render pipeline state into the argument buffer.
- [func setRenderPipelineStates([(any MTLRenderPipelineState)?], range: Range<Int>)](mtlargumentencoder/setrenderpipelinestates(_:range:).md)
  Encodes references to an array of render pipeline states into the argument buffer.
- [func setComputePipelineState((any MTLComputePipelineState)?, index: Int)](mtlargumentencoder/setcomputepipelinestate(_:index:).md)
  Encodes a reference to a compute pipeline state into the argument buffer.
- [func setComputePipelineState((any MTLComputePipelineState)?, at: Int)](mtlargumentencoder/setcomputepipelinestate(_:at:).md)
  Encodes a reference to a compute pipeline state into the argument buffer.
- [func setComputePipelineStates([(any MTLComputePipelineState)?], range: Range<Int>)](mtlargumentencoder/setcomputepipelinestates(_:range:).md)
  Encodes references to an array of compute pipeline states into the argument buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlargumentencoder/setcomputepipelinestates(_:with:))*
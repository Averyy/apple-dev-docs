# setComputePipelineState(_:at:)

**Framework**: Metal  
**Kind**: method

Encodes a reference to a compute pipeline state into the argument buffer.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.13+
- tvOS 13.0+
- visionOS ?+

## Declaration

```swift
func setComputePipelineState(_ pipeline: (any MTLComputePipelineState)?, at index: Int)
```

## Parameters

- `pipeline`: A pipeline state the method encodes.
- `index`: The index of a pipeline state within the argument buffer.   The value corresponds to either the index ID of a declaration in   Metal Shading Language (MSL) or the   property of   an   instance.

## See Also

- [func setRenderPipelineState((any MTLRenderPipelineState)?, index: Int)](mtlargumentencoder/setrenderpipelinestate(_:index:).md)
  Encodes a reference to a render pipeline state into the argument buffer.
- [func setRenderPipelineStates([(any MTLRenderPipelineState)?], range: Range<Int>)](mtlargumentencoder/setrenderpipelinestates(_:range:).md)
  Encodes references to an array of render pipeline states into the argument buffer.
- [func setComputePipelineState((any MTLComputePipelineState)?, index: Int)](mtlargumentencoder/setcomputepipelinestate(_:index:).md)
  Encodes a reference to a compute pipeline state into the argument buffer.
- [func setComputePipelineStates(UnsafePointer<(any MTLComputePipelineState)?>, with: NSRange)](mtlargumentencoder/setcomputepipelinestates(_:with:).md)
  Encodes references to an array of compute pipeline states into the argument buffer.
- [func setComputePipelineStates([(any MTLComputePipelineState)?], range: Range<Int>)](mtlargumentencoder/setcomputepipelinestates(_:range:).md)
  Encodes references to an array of compute pipeline states into the argument buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlargumentencoder/setcomputepipelinestate(_:at:))*
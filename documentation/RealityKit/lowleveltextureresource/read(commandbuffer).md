# read(commandBuffer:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Returns a Metal texture containing the current contents of the texture resource for GPU read operations.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
final func read(commandBuffer: (any MTLCommandBuffer)?) -> any MTLTexture
```

#### Return Value

A `MTLTexture` ready for GPU read operations.

#### Discussion

The renderer waits for the provided command buffer to complete before discarding the texture.

## Parameters

- `commandBuffer`: The command buffer that reads from this texture, or `nil` to skip synchronization.

## See Also

### Reading and writing texture data
- [func replace(commandBuffer: (any MTLCommandBuffer)?) -> any MTLTexture](./replace%28commandbuffer%29.md)
  Returns a Metal texture you populate on the GPU with the new contents of the texture resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveltextureresource/read(commandbuffer:))*
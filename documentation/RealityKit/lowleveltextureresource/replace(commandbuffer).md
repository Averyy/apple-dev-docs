# replace(commandBuffer:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Returns a Metal texture you populate on the GPU with the new contents of the texture resource.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
final func replace(commandBuffer: (any MTLCommandBuffer)?) -> any MTLTexture
```

#### Return Value

A `MTLTexture` ready for GPU write operations.

#### Discussion

Upon return the texture’s contents are undefined; the caller is responsible for populating it with valid data. The renderer waits for the provided command buffer to complete before using the texture for rendering.

## Parameters

- `commandBuffer`: The command buffer that writes to this texture, or `nil` to skip synchronization.

## See Also

### Reading and writing texture data
- [func read(commandBuffer: (any MTLCommandBuffer)?) -> any MTLTexture](./read%28commandbuffer%29.md)
  Returns a Metal texture containing the current contents of the texture resource for GPU read operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveltextureresource/replace(commandbuffer:))*
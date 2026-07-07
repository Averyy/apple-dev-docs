# replace(commandBuffer:)

**Framework**: RealityKit  
**Kind**: method

Retrieves a Metal texture that shaders can write to on the GPU. The texture’s contents are in an uninitialized state. The renderer waits for the command buffer to complete before using the texture for rendering.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func replace(commandBuffer: (any MTLCommandBuffer)?) -> any MTLTexture
```

#### Return Value

A `MTLTexture` ready for GPU write operations.

## Parameters

- `commandBuffer`: The command buffer writing to this texture, or `nil` to skip synchronization.

## See Also

- [func read(commandBuffer: (any MTLCommandBuffer)?) -> any MTLTexture](lowleveltextureresource/read(commandbuffer:).md)
  Retrieves the Metal texture for GPU reading.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveltextureresource/replace(commandbuffer:))*
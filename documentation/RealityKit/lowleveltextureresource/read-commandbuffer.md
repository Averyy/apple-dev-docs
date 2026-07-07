# read(commandBuffer:)

**Framework**: RealityKit  
**Kind**: method

Retrieves the Metal texture for GPU reading.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func read(commandBuffer: (any MTLCommandBuffer)?) -> any MTLTexture
```

#### Return Value

The underlying `MTLTexture` for reading.

#### Discussion

The renderer waits for the command buffer to complete before using the texture for rendering.

## Parameters

- `commandBuffer`: The command buffer using this texture, or `nil` to skip synchronization.

## See Also

- [func replace(commandBuffer: (any MTLCommandBuffer)?) -> any MTLTexture](lowleveltextureresource/replace(commandbuffer:).md)
  Retrieves a Metal texture that shaders can write to on the GPU. The texture’s contents are in an uninitialized state. The renderer waits for the command buffer to complete before using the texture for rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveltextureresource/read(commandbuffer:))*
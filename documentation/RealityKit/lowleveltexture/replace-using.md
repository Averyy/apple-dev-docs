# replace(using:)

**Framework**: RealityKit  
**Kind**: method

Retrieves a Metal texture that your app’s shaders can write to when they run on a GPU.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
@MainActor
func replace(using commandBuffer: any MTLCommandBuffer) -> any MTLTexture
```

#### Discussion

The buffer’s contents are in an uninitialized state.

## Parameters

- `commandBuffer`: The    you intend to use for texture modifications.   RealityKit waits for the command buffer to complete before utilizing the texture for rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveltexture/replace(using:))*
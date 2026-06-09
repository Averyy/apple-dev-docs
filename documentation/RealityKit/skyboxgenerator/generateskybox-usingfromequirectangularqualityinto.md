# generateSkybox(using:fromEquirectangular:quality:into:)

**Framework**: RealityKit  
**Kind**: method

Adds commands for generating a cube from an equirectangular image, including generating mipmaps.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func generateSkybox(using commandBuffer: any MTLCommandBuffer, fromEquirectangular texture: any MTLTexture, quality: TextureSamplingQuality = .low, into destination: any MTLTexture) throws
```

## Parameters

- `commandBuffer`: The command buffer to dispatch GPU work to generate cubemap
- `texture`: The source image equirectangular texture, also known as “latitude longitude” texture.
- `quality`: The sampling quality the initializer applies as it generates the cube texture.
- `destination`: The destination cube texture. Use `makeDescriptor(fromEquirectangular:)` to get a recommended descriptor for creating the destination texture.

## See Also

- [func makeDescriptor(fromEquirectangular: any MTLTexture) throws -> MTLTextureDescriptor](skyboxgenerator/makedescriptor(fromequirectangular:).md)
  Returns a recommended skybox cube texture descriptor (for `MTLCommandBuffer.generateSkybox`).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/skyboxgenerator/generateskybox(using:fromequirectangular:quality:into:))*
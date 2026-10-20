# generateSkybox(using:fromEquirectangular:quality:into:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Adds commands for generating a cube from an equirectangular image, including generating mipmaps.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func generateSkybox(using commandBuffer: any MTLCommandBuffer, fromEquirectangular texture: any MTLTexture, quality: TextureSamplingQuality = .low, into destination: any MTLTexture) throws
```

#### Discussion

> **Throws**: If `texture` is not a 2D Metal texture, if `destination` is not a cube texture, or if `destination`’s pixel format does not support shader writes on this device.

## Parameters

- `commandBuffer`: The command buffer to dispatch GPU work to generate cubemap
- `texture`: The source image equirectangular texture, also known as “latitude longitude” texture.
- `quality`: The sampling quality the method applies as it generates the cube texture.
- `destination`: The destination cube texture. Use [`makeDescriptor(fromEquirectangular:)`](./makedescriptor%28fromequirectangular%29.md) to get a recommended descriptor for creating the destination texture.

## See Also

### Generating a skybox
- [func makeDescriptor(fromEquirectangular: any MTLTexture) throws -> MTLTextureDescriptor](./makedescriptor%28fromequirectangular%29.md)
  Returns a recommended skybox cube texture descriptor (for [`generateSkybox(using:fromEquirectangular:quality:into:)`](./generateskybox%28using,fromequirectangular,quality,into%29.md)).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/skyboxgenerator/generateskybox(using:fromequirectangular:quality:into:))*
# SkyboxGenerator

**Framework**: RealityKit  
**Kind**: class

An object that generates a skybox cube texture from an equirectangular source.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
class SkyboxGenerator
```

#### Overview

Use a skybox generator to convert a latitude/longitude (equirectangular) Metal texture into a cube texture that you can render as a scene background or feed into [`ImageBasedLightTextureGenerator`](imagebasedlighttexturegenerator.md) to derive image-based-lighting diffuse and specular textures. The generator dispatches its work onto a Metal command buffer that you provide, so it composes naturally with other GPU work and with RealityKit’s `LowLevelTexture`.

## Topics

### Creating a skybox generator
- [init(device: any MTLDevice)](skyboxgenerator/init(device:)-1hp6p.md)
- [init(device: any MTLDevice) async](skyboxgenerator/init(device:)-5ot7g.md)
### Generating a skybox
- [func generateSkybox(using: any MTLCommandBuffer, fromEquirectangular: any MTLTexture, quality: TextureSamplingQuality, into: any MTLTexture) throws](skyboxgenerator/generateskybox(using:fromequirectangular:quality:into:).md)
  Adds commands for generating a cube from an equirectangular image, including generating mipmaps.
- [func makeDescriptor(fromEquirectangular: any MTLTexture) throws -> MTLTextureDescriptor](skyboxgenerator/makedescriptor(fromequirectangular:).md)
  Returns a recommended skybox cube texture descriptor (for [`generateSkybox(using:fromEquirectangular:quality:into:)`](skyboxgenerator/generateskybox(using:fromequirectangular:quality:into:).md)).
### Initializers
- [init(device:)](skyboxgenerator/init(device:).md)

## See Also

- [class ImageBasedLightTextureGenerator](imagebasedlighttexturegenerator.md)
  An object that generates image-based-lighting diffuse and specular cube textures from a skybox.
- [enum TextureSamplingQuality](texturesamplingquality.md)
  A discrete trade-off between generation time and texture quality, used by [`SkyboxGenerator`](skyboxgenerator.md) and [`ImageBasedLightTextureGenerator`](imagebasedlighttexturegenerator.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/skyboxgenerator)*
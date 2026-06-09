# SkyboxGenerator

**Framework**: RealityKit  
**Kind**: class

An object for generating skybox textures.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
class SkyboxGenerator
```

## Topics

### Creating a skybox generator
- [init(device: any MTLDevice)](skyboxgenerator/init(device:)-1hp6p.md)
- [init(device: any MTLDevice) async](skyboxgenerator/init(device:)-5ot7g.md)
### Generating a skybox
- [func generateSkybox(using: any MTLCommandBuffer, fromEquirectangular: any MTLTexture, quality: TextureSamplingQuality, into: any MTLTexture) throws](skyboxgenerator/generateskybox(using:fromequirectangular:quality:into:).md)
  Adds commands for generating a cube from an equirectangular image, including generating mipmaps.
- [func makeDescriptor(fromEquirectangular: any MTLTexture) throws -> MTLTextureDescriptor](skyboxgenerator/makedescriptor(fromequirectangular:).md)
  Returns a recommended skybox cube texture descriptor (for `MTLCommandBuffer.generateSkybox`).
### Initializers
- [init(device:)](skyboxgenerator/init(device:).md)

## See Also

- [class ImageBasedLightTextureGenerator](imagebasedlighttexturegenerator.md)
  An object for generating based light textures. Computes an image based light’s diffuse and specular textures from a skybox texture.
- [enum TextureSamplingQuality](texturesamplingquality.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/skyboxgenerator)*
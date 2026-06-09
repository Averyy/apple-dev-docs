# ImageBasedLightTextureGenerator

**Framework**: RealityKit  
**Kind**: class

An object for generating based light textures. Computes an image based light’s diffuse and specular textures from a skybox texture.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
class ImageBasedLightTextureGenerator
```

## Topics

### Creating a generator
- [init(device: any MTLDevice)](imagebasedlighttexturegenerator/init(device:)-22qce.md)
- [init(device: any MTLDevice) async](imagebasedlighttexturegenerator/init(device:)-5yjyb.md)
### Generating IBL textures
- [func generateDiffuse(using: any MTLCommandBuffer, fromSkyboxCube: any MTLTexture, quality: TextureSamplingQuality, into: any MTLTexture) throws](imagebasedlighttexturegenerator/generatediffuse(using:fromskyboxcube:quality:into:).md)
  Adds commands for generating an image based light diffuse texture from a skybox cube.
- [func generateSpecular(using: any MTLCommandBuffer, fromSkyboxCube: any MTLTexture, quality: TextureSamplingQuality, into: any MTLTexture) throws](imagebasedlighttexturegenerator/generatespecular(using:fromskyboxcube:quality:into:).md)
  Adds commands for generating an image based light specular texture from a skybox cube.
### Describing output textures
- [func makeDiffuseDescriptor(fromCube: any MTLTexture) throws -> MTLTextureDescriptor](imagebasedlighttexturegenerator/makediffusedescriptor(fromcube:).md)
  Returns a recommended image based light diffuse cube texture descriptor (for `MTLCommandBuffer.generateDiffuse`).
- [func makeSpecularDescriptor(fromCube: any MTLTexture) throws -> MTLTextureDescriptor](imagebasedlighttexturegenerator/makespeculardescriptor(fromcube:).md)
  Returns a recommended image based light diffuse cube texture descriptor (for `MTLCommandBuffer.generateSpecular`).
### Initializers
- [init(device:)](imagebasedlighttexturegenerator/init(device:).md)

## See Also

- [class SkyboxGenerator](skyboxgenerator.md)
  An object for generating skybox textures.
- [enum TextureSamplingQuality](texturesamplingquality.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/imagebasedlighttexturegenerator)*
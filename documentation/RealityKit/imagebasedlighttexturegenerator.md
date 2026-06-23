# ImageBasedLightTextureGenerator

**Framework**: RealityKit  
**Kind**: class

An object that generates image-based-lighting diffuse and specular cube textures from a skybox.

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

#### Overview

Image-based lighting (IBL) approximates how an environment lights a surface by convolving the environment’s skybox into two cube textures: a diffuse irradiance map (low-frequency lighting that hits matte surfaces) and a specular pre-filtered map (per-roughness lighting that drives glossy reflections). RealityKit’s `EnvironmentResource` consumes textures of this shape, and this generator lets you produce them directly in Metal so you can control resolution, pixel format, sampling quality, and command-buffer scheduling.

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
  Returns a recommended image based light diffuse cube texture descriptor (for [`generateDiffuse(using:fromSkyboxCube:quality:into:)`](imagebasedlighttexturegenerator/generatediffuse(using:fromskyboxcube:quality:into:).md)).
- [func makeSpecularDescriptor(fromCube: any MTLTexture) throws -> MTLTextureDescriptor](imagebasedlighttexturegenerator/makespeculardescriptor(fromcube:).md)
  Returns a recommended image based light specular cube texture descriptor (for [`generateSpecular(using:fromSkyboxCube:quality:into:)`](imagebasedlighttexturegenerator/generatespecular(using:fromskyboxcube:quality:into:).md)).
### Initializers
- [init(device:)](imagebasedlighttexturegenerator/init(device:).md)

## See Also

- [class SkyboxGenerator](skyboxgenerator.md)
  An object that generates a skybox cube texture from an equirectangular source.
- [enum TextureSamplingQuality](texturesamplingquality.md)
  A discrete trade-off between generation time and texture quality, used by [`SkyboxGenerator`](skyboxgenerator.md) and [`ImageBasedLightTextureGenerator`](imagebasedlighttexturegenerator.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/imagebasedlighttexturegenerator)*
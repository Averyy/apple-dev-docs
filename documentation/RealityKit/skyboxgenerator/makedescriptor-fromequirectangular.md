# makeDescriptor(fromEquirectangular:)

**Framework**: RealityKit  
**Kind**: method

Returns a recommended skybox cube texture descriptor (for [`generateSkybox(using:fromEquirectangular:quality:into:)`](skyboxgenerator/generateskybox(using:fromequirectangular:quality:into:).md)).

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func makeDescriptor(fromEquirectangular texture: any MTLTexture) throws -> MTLTextureDescriptor
```

#### Discussion

The dimensions of the cubemap are chosen so that the resolution of the input texture is approximately preserved. This method allocates mipmap by default, as mipmaps are needed by [`generateDiffuse(using:fromSkyboxCube:quality:into:)`](imagebasedlighttexturegenerator/generatediffuse(using:fromskyboxcube:quality:into:).md) and [`generateSpecular(using:fromSkyboxCube:quality:into:)`](imagebasedlighttexturegenerator/generatespecular(using:fromskyboxcube:quality:into:).md).

> **Note**: If `texture` is not a 2D Metal texture.

## See Also

- [func generateSkybox(using: any MTLCommandBuffer, fromEquirectangular: any MTLTexture, quality: TextureSamplingQuality, into: any MTLTexture) throws](skyboxgenerator/generateskybox(using:fromequirectangular:quality:into:).md)
  Adds commands for generating a cube from an equirectangular image, including generating mipmaps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/skyboxgenerator/makedescriptor(fromequirectangular:))*
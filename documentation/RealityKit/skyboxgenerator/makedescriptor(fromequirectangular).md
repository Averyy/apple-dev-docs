# makeDescriptor(fromEquirectangular:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Returns a recommended skybox cube texture descriptor (for [`generateSkybox(using:fromEquirectangular:quality:into:)`](./generateskybox%28using,fromequirectangular,quality,into%29.md)).

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func makeDescriptor(fromEquirectangular texture: any MTLTexture) throws -> MTLTextureDescriptor
```

#### Discussion

The dimensions of the cubemap are chosen so that the resolution of the input texture is approximately preserved. This method allocates mipmap by default, as mipmaps are needed by [`generateDiffuse(using:fromSkyboxCube:quality:into:)`](../imagebasedlighttexturegenerator/generatediffuse%28using,fromskyboxcube,quality,into%29.md) and [`generateSpecular(using:fromSkyboxCube:quality:into:)`](../imagebasedlighttexturegenerator/generatespecular%28using,fromskyboxcube,quality,into%29.md).

> **Throws**: If `texture` is not a 2D Metal texture.

## See Also

### Generating a skybox
- [func generateSkybox(using: any MTLCommandBuffer, fromEquirectangular: any MTLTexture, quality: TextureSamplingQuality, into: any MTLTexture) throws](./generateskybox%28using,fromequirectangular,quality,into%29.md)
  Adds commands for generating a cube from an equirectangular image, including generating mipmaps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/skyboxgenerator/makedescriptor(fromequirectangular:))*
# generateSpecular(using:fromSkyboxCube:quality:into:)

**Framework**: RealityKit  
**Kind**: method

Adds commands for generating an image based light specular texture from a skybox cube.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func generateSpecular(using commandBuffer: any MTLCommandBuffer, fromSkyboxCube texture: any MTLTexture, quality: TextureSamplingQuality = .low, into destination: any MTLTexture) throws
```

## Parameters

- `commandBuffer`: The command buffer to dispatch GPU work to generate Image Based Light Specular
- `texture`: The source image cube skybox texture, which must have mipmaps.
- `quality`: The sampling quality the initializer applies as it generates the cube texture.
- `destination`: The destination cube texture. Use `makeImageBasedLightDiffuseDescriptor(fromCube:)` to get a recommended descriptor for creating the destination texture.

## See Also

- [func generateDiffuse(using: any MTLCommandBuffer, fromSkyboxCube: any MTLTexture, quality: TextureSamplingQuality, into: any MTLTexture) throws](imagebasedlighttexturegenerator/generatediffuse(using:fromskyboxcube:quality:into:).md)
  Adds commands for generating an image based light diffuse texture from a skybox cube.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/imagebasedlighttexturegenerator/generatespecular(using:fromskyboxcube:quality:into:))*
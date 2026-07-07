# generateDiffuse(using:fromSkyboxCube:quality:into:)

**Framework**: RealityKit  
**Kind**: method

Adds commands for generating an image based light diffuse texture from a skybox cube.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func generateDiffuse(using commandBuffer: any MTLCommandBuffer, fromSkyboxCube texture: any MTLTexture, quality: TextureSamplingQuality = .low, into destination: any MTLTexture) throws
```

#### Discussion

> **Note**: If `texture` or `destination` is not a cube texture, or if `destination`’s pixel format does not support shader writes on this device.

## Parameters

- `commandBuffer`: The command buffer to dispatch GPU work to generate Image Based Light Diffuse
- `texture`: The source image cube skybox texture, which must have mipmaps.
- `quality`: The sampling quality the method applies as it generates the cube texture.
- `destination`: The destination cube texture. Use [`makeDiffuseDescriptor(fromCube:)`](imagebasedlighttexturegenerator/makediffusedescriptor(fromcube:).md) to get a recommended descriptor for creating the destination texture.

## See Also

- [func generateSpecular(using: any MTLCommandBuffer, fromSkyboxCube: any MTLTexture, quality: TextureSamplingQuality, into: any MTLTexture) throws](imagebasedlighttexturegenerator/generatespecular(using:fromskyboxcube:quality:into:).md)
  Adds commands for generating an image based light specular texture from a skybox cube.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/imagebasedlighttexturegenerator/generatediffuse(using:fromskyboxcube:quality:into:))*
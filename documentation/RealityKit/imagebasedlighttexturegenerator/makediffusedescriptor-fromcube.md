# makeDiffuseDescriptor(fromCube:)

**Framework**: RealityKit  
**Kind**: method

Returns a recommended image based light diffuse cube texture descriptor (for [`generateDiffuse(using:fromSkyboxCube:quality:into:)`](imagebasedlighttexturegenerator/generatediffuse(using:fromskyboxcube:quality:into:).md)).

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func makeDiffuseDescriptor(fromCube texture: any MTLTexture) throws -> MTLTextureDescriptor
```

#### Discussion

> **Note**: If `texture` is not a cube texture.

## See Also

- [func makeSpecularDescriptor(fromCube: any MTLTexture) throws -> MTLTextureDescriptor](imagebasedlighttexturegenerator/makespeculardescriptor(fromcube:).md)
  Returns a recommended image based light specular cube texture descriptor (for [`generateSpecular(using:fromSkyboxCube:quality:into:)`](imagebasedlighttexturegenerator/generatespecular(using:fromskyboxcube:quality:into:).md)).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/imagebasedlighttexturegenerator/makediffusedescriptor(fromcube:))*
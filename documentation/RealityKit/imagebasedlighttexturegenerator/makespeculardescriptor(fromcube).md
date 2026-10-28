# makeSpecularDescriptor(fromCube:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Returns a recommended image based light specular cube texture descriptor (for [`generateSpecular(using:fromSkyboxCube:quality:into:)`](./generatespecular%28using,fromskyboxcube,quality,into%29.md)).

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func makeSpecularDescriptor(fromCube texture: any MTLTexture) throws -> MTLTextureDescriptor
```

## Discussion

> **Throws**: If `texture` is not a cube texture.

## See Also

### Describing output textures
- [func makeDiffuseDescriptor(fromCube: any MTLTexture) throws -> MTLTextureDescriptor](./makediffusedescriptor%28fromcube%29.md)
  Returns a recommended image based light diffuse cube texture descriptor (for [`generateDiffuse(using:fromSkyboxCube:quality:into:)`](./generatediffuse%28using,fromskyboxcube,quality,into%29.md)).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/imagebasedlighttexturegenerator/makespeculardescriptor(fromcube:))*
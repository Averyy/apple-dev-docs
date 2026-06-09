# makeSpecularDescriptor(fromCube:)

**Framework**: RealityKit  
**Kind**: method

Returns a recommended image based light diffuse cube texture descriptor (for `MTLCommandBuffer.generateSpecular`).

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func makeSpecularDescriptor(fromCube texture: any MTLTexture) throws -> MTLTextureDescriptor
```

## See Also

- [func makeDiffuseDescriptor(fromCube: any MTLTexture) throws -> MTLTextureDescriptor](imagebasedlighttexturegenerator/makediffusedescriptor(fromcube:).md)
  Returns a recommended image based light diffuse cube texture descriptor (for `MTLCommandBuffer.generateDiffuse`).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/imagebasedlighttexturegenerator/makespeculardescriptor(fromcube:))*
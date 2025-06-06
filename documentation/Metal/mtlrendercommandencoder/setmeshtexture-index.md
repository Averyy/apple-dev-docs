# setMeshTexture(_:index:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Assigns a texture to an entry in the mesh shader argument table.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func setMeshTexture(_ texture: (any MTLTexture)?, index: Int)
```

#### Discussion

By default, the texture at each index is `nil`.

## Parameters

- `texture`: An   instance the command assigns to an entry in the mesh shader argument table for textures.
- `index`: An integer that represents the entry in the mesh shader argument table for textures that stores a record of  .

## See Also

- [func setMeshTextures([(any MTLTexture)?], range: Range<Int>)](mtlrendercommandencoder/setmeshtextures(_:range:).md)
  Assigns multiple textures to a range of entries in the mesh shader argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setmeshtexture(_:index:))*
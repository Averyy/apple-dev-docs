# setVertexTexture(_:index:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Assigns a texture to an entry in the vertex shader argument table.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func setVertexTexture(_ texture: (any MTLTexture)?, index: Int)
```

#### Discussion

By default, the texture at each index is `nil`.

## Parameters

- `texture`: An   instance the command assigns to an entry in the vertex shader argument table for textures.
- `index`: An integer that represents the entry in the vertex shader argument table for textures that stores a record of  .

## See Also

- [func setVertexTextures([(any MTLTexture)?], range: Range<Int>)](mtlrendercommandencoder/setvertextextures(_:range:).md)
  Assigns multiple textures to a range of entries in the vertex shader argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setvertextexture(_:index:))*
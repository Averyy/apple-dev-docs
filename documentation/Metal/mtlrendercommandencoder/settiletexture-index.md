# setTileTexture(_:index:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Assigns a texture to an entry in the tile shader argument table.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.5+
- visionOS 1.0+

## Declaration

```swift
func setTileTexture(_ texture: (any MTLTexture)?, index: Int)
```

#### Discussion

By default, the texture at each index is `nil`.

## Parameters

- `texture`: An   instance the command assigns to an entry in the tile shader argument table for textures.
- `index`: An integer that represents the entry in the tile shader argument table for textures that stores a record of  .

## See Also

- [func setTileTextures([(any MTLTexture)?], range: Range<Int>)](mtlrendercommandencoder/settiletextures(_:range:).md)
  Assigns multiple textures to a range of entries in the tile shader argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/settiletexture(_:index:))*
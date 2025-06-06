# setTileTextures(_:range:)

**Framework**: Metal  
**Kind**: method

Assigns multiple textures to a range of entries in the tile shader argument table.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.5+
- visionOS ?+

## Declaration

```swift
func setTileTextures(_ textures: [(any MTLTexture)?], range: Range<Int>)
```

#### Discussion

By default, the texture at each index is `nil`.

> **Note**:  The Objective-C version of this method is [`setTileTextures:withRange:`](mtlrendercommandencoder/settiletextures:withrange:.md).

 The Objective-C version of this method is [`setTileTextures:withRange:`](mtlrendercommandencoder/settiletextures:withrange:.md).

## Parameters

- `textures`: An array of   instances the command assigns to entries in the tile shader argument table for textures.
- `range`: A span of integers that represent the entries in the tile shader argument table for textures. Each entry stores a record of the corresponding element in  .

## See Also

- [func setTileTexture((any MTLTexture)?, index: Int)](mtlrendercommandencoder/settiletexture(_:index:).md)
  Assigns a texture to an entry in the tile shader argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/settiletextures(_:range:))*
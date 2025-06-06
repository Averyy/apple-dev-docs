# setObjectTextures(_:range:)

**Framework**: Metal  
**Kind**: method

Assigns multiple textures to a range of entries in the object shader argument table.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+

## Declaration

```swift
func setObjectTextures(_ textures: [(any MTLTexture)?], range: Range<Int>)
```

#### Discussion

By default, the texture at each index is `nil`.

> **Note**:  The Objective-C version of this method is [`setObjectTextures:withRange:`](mtlrendercommandencoder/setobjecttextures:withrange:.md).

## Parameters

- `textures`: An array of   instances the command assigns to entries in the object shader argument table for textures.
- `range`: A span of integers that represent the entries in the object shader argument table for textures. Each entry stores a record of the corresponding element in  .

## See Also

- [func setObjectTexture((any MTLTexture)?, index: Int)](mtlrendercommandencoder/setobjecttexture(_:index:).md)
  Assigns a texture to an entry in the object shader argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setobjecttextures(_:range:))*
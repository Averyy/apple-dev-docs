# setVertexTextures(_:range:)

**Framework**: Metal  
**Kind**: method

Assigns multiple textures to a range of entries in the vertex shader argument table.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst ?+
- macOS 10.11+
- tvOS 8.0+
- visionOS ?+

## Declaration

```swift
func setVertexTextures(_ textures: [(any MTLTexture)?], range: Range<Int>)
```

#### Discussion

By default, the texture at each index is `nil`.

> **Note**:  The Objective-C version of this method is [`setVertexTextures:withRange:`](mtlrendercommandencoder/setvertextextures:withrange:.md).

 The Objective-C version of this method is [`setVertexTextures:withRange:`](mtlrendercommandencoder/setvertextextures:withrange:.md).

## Parameters

- `textures`: An array of   instances the command assigns to entries in the vertex shader argument table for textures.
- `range`: A span of integers that represent the entries in the vertex shader argument table for textures. Each entry stores a record of the corresponding element in  .

## See Also

- [func setVertexTexture((any MTLTexture)?, index: Int)](mtlrendercommandencoder/setvertextexture(_:index:).md)
  Assigns a texture to an entry in the vertex shader argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setvertextextures(_:range:))*
# setFragmentTextures(_:range:)

**Framework**: Metal  
**Kind**: method

Assigns multiple textures to a range of entries in the fragment shader argument table.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst ?+
- macOS 10.11+
- tvOS 8.0+
- visionOS ?+

## Declaration

```swift
func setFragmentTextures(_ textures: [(any MTLTexture)?], range: Range<Int>)
```

#### Discussion

By default, the texture at each index is `nil`.

> **Note**:  The Objective-C version of this method is [`setFragmentTextures:withRange:`](mtlrendercommandencoder/setfragmenttextures:withrange:.md).

## Parameters

- `textures`: An array of   instances the command assigns to entries in the fragment shader argument table for textures.
- `range`: A span of integers that represent the entries in the fragment shader argument table for textures. Each entry stores a record of the corresponding element in  .

## See Also

- [func setFragmentTexture((any MTLTexture)?, index: Int)](mtlrendercommandencoder/setfragmenttexture(_:index:).md)
  Assigns a texture to an entry in the fragment shader argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setfragmenttextures(_:range:))*
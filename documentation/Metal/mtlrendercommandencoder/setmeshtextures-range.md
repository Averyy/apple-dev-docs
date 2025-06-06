# setMeshTextures(_:range:)

**Framework**: Metal  
**Kind**: method

Assigns multiple textures to a range of entries in the mesh shader argument table.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+

## Declaration

```swift
func setMeshTextures(_ textures: [(any MTLTexture)?], range: Range<Int>)
```

#### Discussion

By default, the texture at each index is `nil`.

> **Note**:  The Objective-C version of this method is [`setMeshTextures:withRange:`](mtlrendercommandencoder/setmeshtextures:withrange:.md).

## Parameters

- `textures`: An array of   instances the command assigns to entries in the mesh shader argument table for textures.
- `range`: A span of integers that represent the entries in the mesh shader argument table for textures. Each entry stores a record of the corresponding element in  .

## See Also

- [func setMeshTexture((any MTLTexture)?, index: Int)](mtlrendercommandencoder/setmeshtexture(_:index:).md)
  Assigns a texture to an entry in the mesh shader argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setmeshtextures(_:range:))*
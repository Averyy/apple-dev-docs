# setObjectTextures(_:range:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Assigns multiple textures to a range of entries in the object shader argument table.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS

## Declaration

```swift
func setObjectTextures(_ textures: [(any MTLTexture)?], range: Range<Int>)
```

## Discussion

By default, the texture at each index is `nil`.

> **Note**:  The Objective-C version of this method is [`setObjectTextures:withRange:`](./setobjecttextures_withrange_.md).

## Parameters

- `textures`: An array of [`MTLTexture`](../mtltexture.md) instances the command assigns to entries in the object shader argument table for textures.
- `range`: A span of integers that represent the entries in the object shader argument table for textures. Each entry stores a record of the corresponding element in `textures`.

## See Also

### Assigning textures for object shaders
- [func setObjectTexture((any MTLTexture)?, index: Int)](./setobjecttexture%28_,index%29.md)
  Assigns a texture to an entry in the object shader argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setobjecttextures(_:range:))*
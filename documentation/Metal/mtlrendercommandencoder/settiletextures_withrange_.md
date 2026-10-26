# setTileTextures:withRange:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Assigns multiple textures to a range of entries in the tile shader argument table.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.5+
- visionOS 1.0+

## Declaration

```objc
- (void) setTileTextures:(id<MTLTexture> const[]) textures withRange:(NSRange) range;
```

#### Discussion

By default, the texture at each index is `nil`.

> **Note**:  The Swift version of this method is [`setTileTextures(_:range:)`](./settiletextures%28_,range%29.md).

## Parameters

- `textures`: A pointer to a C array of [`MTLTexture`](../mtltexture.md) instances the command assigns to entries in the tile shader argument table for textures.
- `range`: A span of integers that represent the entries in the tile shader argument table for textures. Each entry stores a record of the corresponding element in `textures`.

## See Also

### Assigning textures
- [func setTileTexture((any MTLTexture)?, index: Int)](./settiletexture%28_,index%29.md)
  Assigns a texture to an entry in the tile shader argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/settiletextures:withrange:)*
# setVertexTextures:withRange:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Assigns multiple textures to a range of entries in the vertex shader argument table.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```objc
- (void) setVertexTextures:(id<MTLTexture> const[]) textures withRange:(NSRange) range;
```

## Discussion

By default, the texture at each index is `nil`.

> **Note**:  The Swift version of this method is [`setVertexTextures(_:range:)`](./setvertextextures%28_,range%29.md).

## Parameters

- `textures`: A pointer to a C array of [`MTLTexture`](../mtltexture.md) instances the command assigns to entries in the vertex shader argument table for textures.
- `range`: A span of integers that represent the entries in the vertex shader argument table for textures. Each entry stores a record of the corresponding element in `textures`.

## See Also

### Assigning textures
- [func setVertexTexture((any MTLTexture)?, index: Int)](./setvertextexture%28_,index%29.md)
  Assigns a texture to an entry in the vertex shader argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setvertextextures:withrange:)*
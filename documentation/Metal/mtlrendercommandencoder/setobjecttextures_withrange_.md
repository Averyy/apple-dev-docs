# setObjectTextures:withRange:

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
- visionOS 1.0+

## Declaration

```objc
- (void) setObjectTextures:(id<MTLTexture> const[]) textures withRange:(NSRange) range;
```

#### Discussion

By default, the texture at each index is `nil`.

> **Note**:  The Swift version of this method is [`setObjectTextures(_:range:)`](./setobjecttextures%28_,range%29.md).

## Parameters

- `textures`: A pointer to a C array of [`MTLTexture`](../mtltexture.md) instances the command assigns to entries in the object shader argument table for textures.
- `range`: A span of integers that represent the entries in the object shader argument table for textures. Each entry stores a record of the corresponding element in `textures`.

## See Also

### Assigning textures for object shaders
- [func setObjectTexture((any MTLTexture)?, index: Int)](./setobjecttexture%28_,index%29.md)
  Assigns a texture to an entry in the object shader argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setobjecttextures:withrange:)*
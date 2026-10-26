# setTextures:withRange:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Binds multiple textures to the texture argument table, allowing compute kernels to access their data on the GPU.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```objc
- (void) setTextures:(id<MTLTexture> const[]) textures withRange:(NSRange) range;
```

#### Discussion

> ❗ **Important**:  This method requires that the number of instances in `textures` be the same as the length of `range`.

## Parameters

- `textures`: An array of [`MTLTexture`](../mtltexture.md) instances to bind to the texture argument table.
- `range`: The texture table indices to bind each of the `textures` to, in the order they appear.

## See Also

### Binding textures
- [func setTexture((any MTLTexture)?, index: Int)](./settexture%28_,index%29.md)
  Binds a texture to the texture argument table, allowing compute kernels to access its data on the GPU.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/settextures:withrange:)*
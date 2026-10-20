# setTextures(_:range:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Binds multiple textures to the texture argument table, allowing compute functions to access their data on the GPU.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.11+
- tvOS 8.0+
- visionOS

## Declaration

```swift
func setTextures(_ textures: [(any MTLTexture)?], range: Range<Int>)
```

#### Discussion

> ❗ **Important**:  This method requires that the number of instances in `textures` be the same as the length of `range`.

## Parameters

- `textures`: A list of [`MTLTexture`](../mtltexture.md) instances to bind to the texture argument table.
- `range`: The texture table indices to bind each of the `textures` to, in the order they appear.

## See Also

### Binding textures
- [func setTexture((any MTLTexture)?, index: Int)](./settexture%28_,index%29.md)
  Binds a texture to the texture argument table, allowing compute kernels to access its data on the GPU.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/settextures(_:range:))*
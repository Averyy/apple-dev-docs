# setTexture(_:index:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Binds a texture to the texture argument table, allowing compute kernels to access its data on the GPU.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func setTexture(_ texture: (any MTLTexture)?, index: Int)
```

## Parameters

- `texture`: An   instance to bind to the texture argument table.
- `index`: The index the texture binds to in the texture argument table.

## See Also

- [func setTextures([(any MTLTexture)?], range: Range<Int>)](mtlcomputecommandencoder/settextures(_:range:).md)
  Binds multiple textures to the texture argument table, allowing compute functions to access their data on the GPU.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/settexture(_:index:))*
# textureDataType

**Framework**: Metal  
**Kind**: property

The data type of a texture argument.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var textureDataType: MTLDataType { get }
```

#### Discussion

For information on possible values, see [`MTLDataType`](mtldatatype.md). If the argument is not a texture, querying this property is a fatal error.

## See Also

- [var textureType: MTLTextureType](mtlargument/texturetype.md)
  The texture type of a texture argument.
- [var isDepthTexture: Bool](mtlargument/isdepthtexture.md)
  A Boolean value that indicates whether the texture is a depth texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlargument/texturedatatype)*
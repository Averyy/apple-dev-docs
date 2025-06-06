# access

**Framework**: Metal  
**Kind**: property

The texture’s read/write access to the argument.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var access: MTLBindingAccess { get }
```

#### Discussion

This property indicates the type of access qualifiers (read-only, write-only, or read-write) used in the Metal shading language code. For information on possible values, see [`MTLArgumentAccess`](mtlargumentaccess.md).

## See Also

- [var textureType: MTLTextureType](mtltexturereferencetype/texturetype.md)
  The texture type of the texture.
- [var textureDataType: MTLDataType](mtltexturereferencetype/texturedatatype.md)
  The data type of the texture.
- [var isDepthTexture: Bool](mtltexturereferencetype/isdepthtexture.md)
  A Boolean value that indicates whether the texture is a depth texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltexturereferencetype/access)*
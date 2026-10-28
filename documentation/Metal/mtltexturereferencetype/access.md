# access

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly) MTLBindingAccess access;
```

## Discussion

This property indicates the type of access qualifiers (read-only, write-only, or read-write) used in the Metal shading language code. For information on possible values, see [`MTLArgumentAccess`](../mtlargumentaccess.md).

## See Also

### Describing the texture
- [var textureType: MTLTextureType](./texturetype.md)
  The texture type of the texture.
- [var textureDataType: MTLDataType](./texturedatatype.md)
  The data type of the texture.
- [var isDepthTexture: Bool](./isdepthtexture.md)
  A Boolean value that indicates whether the texture is a depth texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltexturereferencetype/access)*
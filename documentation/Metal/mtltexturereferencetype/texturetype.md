# textureType

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The texture type of the texture.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var textureType: MTLTextureType { get }
```

```objc
@property (readonly) MTLTextureType textureType;
```

## See Also

### Describing the texture
- [var textureDataType: MTLDataType](./texturedatatype.md)
  The data type of the texture.
- [var access: MTLBindingAccess](./access.md)
  The texture’s read/write access to the argument.
- [var isDepthTexture: Bool](./isdepthtexture.md)
  A Boolean value that indicates whether the texture is a depth texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltexturereferencetype/texturetype)*
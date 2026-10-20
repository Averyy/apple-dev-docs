# textureDataType

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The data type of a texture argument.

**Availability**:
- iOS 8.0+ - Deprecated in 16.0
- iPadOS 8.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.11+ - Deprecated in 13.0
- tvOS - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
var textureDataType: MTLDataType { get }
```

```objc
@property (readonly) MTLDataType textureDataType;
```

#### Discussion

For information on possible values, see [`MTLDataType`](../mtldatatype.md). If the argument is not a texture, querying this property is a fatal error.

## See Also

### Describing a texture argument
- [var textureType: MTLTextureType](./texturetype.md)
  The texture type of a texture argument.
- [var isDepthTexture: Bool](./isdepthtexture.md)
  A Boolean value that indicates whether the texture is a depth texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlargument/texturedatatype)*
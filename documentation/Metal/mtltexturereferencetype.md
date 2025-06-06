# MTLTextureReferenceType

**Framework**: Metal  
**Kind**: class

A description of a texture.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MTLTextureReferenceType
```

## Topics

### Describing the Texture
- [var textureType: MTLTextureType](mtltexturereferencetype/texturetype.md)
  The texture type of the texture.
- [var textureDataType: MTLDataType](mtltexturereferencetype/texturedatatype.md)
  The data type of the texture.
- [var access: MTLBindingAccess](mtltexturereferencetype/access.md)
  The texture’s read/write access to the argument.
- [var isDepthTexture: Bool](mtltexturereferencetype/isdepthtexture.md)
  A Boolean value that indicates whether the texture is a depth texture.

## Relationships

### Inherits From
- [MTLType](mtltype.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MTLType](mtltype.md)
  A description of a data type.
- [enum MTLDataType](mtldatatype.md)
  The types of GPU functions, including shaders and compute kernels.
- [class MTLArrayType](mtlarraytype.md)
  A description of an array.
- [class MTLStructType](mtlstructtype.md)
  A description of a structure.
- [class MTLStructMember](mtlstructmember.md)
  An object that provides information about a field in a structure.
- [class MTLPointerType](mtlpointertype.md)
  A description of a pointer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltexturereferencetype)*
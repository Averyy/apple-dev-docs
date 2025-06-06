# structType()

**Framework**: Metal  
**Kind**: method

Provides a description of the underlying struct when the struct member holds a struct.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func structType() -> MTLStructType?
```

#### Return Value

An object that describes the struct. If [`dataType`](mtlstructmember/datatype.md) indicates that this member is not a struct, this method returns `nil`.

## See Also

- [func arrayType() -> MTLArrayType?](mtlstructmember/arraytype.md)
  Provides a description of the underlying array when the struct member holds an array.
- [func pointerType() -> MTLPointerType?](mtlstructmember/pointertype.md)
  Provides a description of the underlying pointer when the struct member holds a pointer.
- [func textureReferenceType() -> MTLTextureReferenceType?](mtlstructmember/texturereferencetype.md)
  Provides a description of the underlying texture when the struct member holds a texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlstructmember/structtype())*
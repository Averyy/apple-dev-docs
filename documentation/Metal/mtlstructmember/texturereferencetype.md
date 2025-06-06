# textureReferenceType()

**Framework**: Metal  
**Kind**: method

Provides a description of the underlying texture when the struct member holds a texture.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func textureReferenceType() -> MTLTextureReferenceType?
```

#### Return Value

An object that describes the texture. If [`dataType`](mtlstructmember/datatype.md) indicates that this member isn’t a texture, this method returns `nil`.

## See Also

- [func arrayType() -> MTLArrayType?](mtlstructmember/arraytype.md)
  Provides a description of the underlying array when the struct member holds an array.
- [func structType() -> MTLStructType?](mtlstructmember/structtype.md)
  Provides a description of the underlying struct when the struct member holds a struct.
- [func pointerType() -> MTLPointerType?](mtlstructmember/pointertype.md)
  Provides a description of the underlying pointer when the struct member holds a pointer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlstructmember/texturereferencetype())*
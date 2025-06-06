# elementTextureReferenceType()

**Framework**: Metal  
**Kind**: method

Provides a description of the underlying texture type when an array holds textures as its elements.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func elementTextureReferenceType() -> MTLTextureReferenceType?
```

#### Return Value

An object that describes the texture. If the array elements aren’t textures, this method returns `nil`.

#### Discussion

Use this method if [`elementType`](mtlarraytype/elementtype.md) is [`MTLDataType.texture`](mtldatatype/texture.md).

## See Also

- [func element() -> MTLArrayType?](mtlarraytype/element.md)
  Provides a description of the underlying type when an array holds other arrays as its elements.
- [func elementStructType() -> MTLStructType?](mtlarraytype/elementstructtype.md)
  Provides a description of the underlying struct type when an array holds structs as its elements.
- [func elementPointerType() -> MTLPointerType?](mtlarraytype/elementpointertype.md)
  Provides a description of the underlying pointer type when an array holds pointers as its elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlarraytype/elementtexturereferencetype())*
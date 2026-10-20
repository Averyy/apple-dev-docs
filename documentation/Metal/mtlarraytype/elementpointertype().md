# elementPointerType()

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Provides a description of the underlying pointer type when an array holds pointers as its elements.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func elementPointerType() -> MTLPointerType?
```

```objc
- (MTLPointerType *) elementPointerType;
```

#### Return Value

An object that describes the pointer. If the array elements aren’t pointers, this method returns `nil`.

#### Discussion

Use this method if [`elementType`](./elementtype.md) is [`MTLDataType.pointer`](../mtldatatype/pointer.md).

## See Also

### Obtaining details for complex array elements
- [func element() -> MTLArrayType?](./element%28%29.md)
  Provides a description of the underlying type when an array holds other arrays as its elements.
- [func elementStructType() -> MTLStructType?](./elementstructtype%28%29.md)
  Provides a description of the underlying struct type when an array holds structs as its elements.
- [func elementTextureReferenceType() -> MTLTextureReferenceType?](./elementtexturereferencetype%28%29.md)
  Provides a description of the underlying texture type when an array holds textures as its elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlarraytype/elementpointertype())*
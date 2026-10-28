# elementStructType()

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Provides a description of the underlying struct type when an array holds structs as its elements.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func elementStructType() -> MTLStructType?
```

```objc
- (MTLStructType *) elementStructType;
```

## Return Value

An object that describes the struct. If the array elements aren’t structs, this method returns `nil`.

## Discussion

Use this method if [`elementType`](./elementtype.md) is [`MTLDataType.struct`](../mtldatatype/struct.md).

## See Also

### Obtaining details for complex array elements
- [func element() -> MTLArrayType?](./element%28%29.md)
  Provides a description of the underlying type when an array holds other arrays as its elements.
- [func elementPointerType() -> MTLPointerType?](./elementpointertype%28%29.md)
  Provides a description of the underlying pointer type when an array holds pointers as its elements.
- [func elementTextureReferenceType() -> MTLTextureReferenceType?](./elementtexturereferencetype%28%29.md)
  Provides a description of the underlying texture type when an array holds textures as its elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlarraytype/elementstructtype())*
# element()

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Provides a description of the underlying type when an array holds other arrays as its elements.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func element() -> MTLArrayType?
```

```objc
- (MTLArrayType *) elementArrayType;
```

## Return Value

Returns an object that describes an array. If the array elements aren’t arrays, this method returns `nil`.

## Discussion

Use this method if [`elementType`](./elementtype.md) is [`MTLDataType.array`](../mtldatatype/array.md).

## See Also

### Obtaining details for complex array elements
- [func elementStructType() -> MTLStructType?](./elementstructtype%28%29.md)
  Provides a description of the underlying struct type when an array holds structs as its elements.
- [func elementPointerType() -> MTLPointerType?](./elementpointertype%28%29.md)
  Provides a description of the underlying pointer type when an array holds pointers as its elements.
- [func elementTextureReferenceType() -> MTLTextureReferenceType?](./elementtexturereferencetype%28%29.md)
  Provides a description of the underlying texture type when an array holds textures as its elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlarraytype/element())*
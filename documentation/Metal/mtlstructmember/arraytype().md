# arrayType()

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Provides a description of the underlying array when the struct member holds an array.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func arrayType() -> MTLArrayType?
```

```objc
- (MTLArrayType *) arrayType;
```

## Return Value

An object that describes the array. If [`dataType`](./datatype.md) indicates that this member is not an array, this method returns `nil.`

## See Also

### Obtaining struct member details
- [func structType() -> MTLStructType?](./structtype%28%29.md)
  Provides a description of the underlying struct when the struct member holds a struct.
- [func pointerType() -> MTLPointerType?](./pointertype%28%29.md)
  Provides a description of the underlying pointer when the struct member holds a pointer.
- [func textureReferenceType() -> MTLTextureReferenceType?](./texturereferencetype%28%29.md)
  Provides a description of the underlying texture when the struct member holds a texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlstructmember/arraytype())*
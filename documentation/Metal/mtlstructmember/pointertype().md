# pointerType()

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Provides a description of the underlying pointer when the struct member holds a pointer.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func pointerType() -> MTLPointerType?
```

```objc
- (MTLPointerType *) pointerType;
```

#### Return Value

An object that describes the pointer. If [`dataType`](./datatype.md) indicates that this member isn’t a pointer, this method returns `nil`.

## See Also

### Obtaining struct member details
- [func arrayType() -> MTLArrayType?](./arraytype%28%29.md)
  Provides a description of the underlying array when the struct member holds an array.
- [func structType() -> MTLStructType?](./structtype%28%29.md)
  Provides a description of the underlying struct when the struct member holds a struct.
- [func textureReferenceType() -> MTLTextureReferenceType?](./texturereferencetype%28%29.md)
  Provides a description of the underlying texture when the struct member holds a texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlstructmember/pointertype())*
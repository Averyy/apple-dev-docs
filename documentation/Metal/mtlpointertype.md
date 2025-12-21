# MTLPointerType

**Framework**: Metal  
**Kind**: class

A description of a pointer.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MTLPointerType
```

## Topics

### Describing the pointer elements
- [var alignment: Int](mtlpointertype/alignment.md)
  The required byte alignment in memory for the element data.
- [var dataSize: Int](mtlpointertype/datasize.md)
  The size, in bytes, of the element data.
- [var elementType: MTLDataType](mtlpointertype/elementtype.md)
  The data type of the element data.
- [var access: MTLBindingAccess](mtlpointertype/access.md)
  The function’s read/write access to the element data.
- [var elementIsArgumentBuffer: Bool](mtlpointertype/elementisargumentbuffer.md)
  A Boolean value that indicates whether the element is an argument buffer.
### Obtaining details for complex pointer elements
- [func elementArrayType() -> MTLArrayType?](mtlpointertype/elementarraytype.md)
  Provides a description of the underlying array when the pointer points to an array.
- [func elementStructType() -> MTLStructType?](mtlpointertype/elementstructtype.md)
  Provides a description of the underlying struct when the pointer points to a struct.

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
  An instance that provides information about a field in a structure.
- [class MTLTextureReferenceType](mtltexturereferencetype.md)
  A description of a texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlpointertype)*
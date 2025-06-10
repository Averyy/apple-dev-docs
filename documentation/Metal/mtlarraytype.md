# MTLArrayType

**Framework**: Metal  
**Kind**: class

A description of an array.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
class MTLArrayType
```

#### Overview

A [`MTLArrayType`](mtlarraytype.md) object provides details about an array parameter. Don’t create [`MTLArrayType`](mtlarraytype.md) objects directly; other reflection objects contain properties to determine if a parameter is an array and to obtain the [`MTLArrayType`](mtlarraytype.md) object that describes the array.

## Topics

### Describing the Array Elements
- [var arrayLength: Int](mtlarraytype/arraylength.md)
  The number of elements in the array.
- [var elementType: MTLDataType](mtlarraytype/elementtype.md)
  The data type of the array’s elements.
- [var stride: Int](mtlarraytype/stride.md)
  The stride between array elements, in bytes.
- [var argumentIndexStride: Int](mtlarraytype/argumentindexstride.md)
  The stride, in bytes, between argument indices.
### Obtaining Details for Complex Array Elements
- [func element() -> MTLArrayType?](mtlarraytype/element.md)
  Provides a description of the underlying type when an array holds other arrays as its elements.
- [func elementStructType() -> MTLStructType?](mtlarraytype/elementstructtype.md)
  Provides a description of the underlying struct type when an array holds structs as its elements.
- [func elementPointerType() -> MTLPointerType?](mtlarraytype/elementpointertype.md)
  Provides a description of the underlying pointer type when an array holds pointers as its elements.
- [func elementTextureReferenceType() -> MTLTextureReferenceType?](mtlarraytype/elementtexturereferencetype.md)
  Provides a description of the underlying texture type when an array holds textures as its elements.
### Instance Methods
- [func elementTensorReferenceType() -> MTLTensorReferenceType?](mtlarraytype/elementtensorreferencetype.md)
  Provides a description of the underlying tensor type when this array holds tensors as its elements.

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
- [class MTLStructType](mtlstructtype.md)
  A description of a structure.
- [class MTLStructMember](mtlstructmember.md)
  An object that provides information about a field in a structure.
- [class MTLPointerType](mtlpointertype.md)
  A description of a pointer.
- [class MTLTextureReferenceType](mtltexturereferencetype.md)
  A description of a texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlarraytype)*
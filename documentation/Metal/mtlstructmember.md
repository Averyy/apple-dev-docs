# MTLStructMember

**Framework**: Metal  
**Kind**: class

An instance that provides information about a field in a structure.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
class MTLStructMember
```

#### Overview

[`MTLStructMember`](mtlstructmember.md) is part of the reflection API that allows Metal framework code to query details about an argument of a Metal shading language function. An [`MTLStructMember`](mtlstructmember.md) instance describes the data type of one field in a struct that is passed as an [`MTLFunction`](mtlfunction.md) argument, which is represented by [`MTLArgument`](mtlargument.md).

Don’t create [`MTLStructMember`](mtlstructmember.md) instances directly. You obtain an [`MTLStructMember`](mtlstructmember.md) instance from either the [`members`](mtlstructtype/members.md) property or the [`memberByName(_:)`](mtlstructtype/memberbyname(_:).md) method of an [`MTLStructType`](mtlstructtype.md) instance. The [`dataType`](mtlstructmember/datatype.md) property of the [`MTLStructMember`](mtlstructmember.md) instance tells you what kind of data is stored in the member. Recursively drill down every struct member until you reach a data type that is neither a struct nor an array.

## Topics

### Describing the struct member
- [var name: String](mtlstructmember/name.md)
  The name of the struct member.
- [var dataType: MTLDataType](mtlstructmember/datatype.md)
  The data type of the struct member.
- [var offset: Int](mtlstructmember/offset.md)
  The location of this member relative to the start of its struct, in bytes.
- [var argumentIndex: Int](mtlstructmember/argumentindex.md)
  The index in the argument table that corresponds to the struct member.
### Obtaining struct member details
- [func arrayType() -> MTLArrayType?](mtlstructmember/arraytype.md)
  Provides a description of the underlying array when the struct member holds an array.
- [func structType() -> MTLStructType?](mtlstructmember/structtype.md)
  Provides a description of the underlying struct when the struct member holds a struct.
- [func pointerType() -> MTLPointerType?](mtlstructmember/pointertype.md)
  Provides a description of the underlying pointer when the struct member holds a pointer.
- [func textureReferenceType() -> MTLTextureReferenceType?](mtlstructmember/texturereferencetype.md)
  Provides a description of the underlying texture when the struct member holds a texture.
### Instance Methods
- [func tensorReferenceType() -> MTLTensorReferenceType?](mtlstructmember/tensorreferencetype.md)
  Provides a description of the underlying tensor type when this struct member holds a tensor.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
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
- [class MTLPointerType](mtlpointertype.md)
  A description of a pointer.
- [class MTLTextureReferenceType](mtltexturereferencetype.md)
  A description of a texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlstructmember)*
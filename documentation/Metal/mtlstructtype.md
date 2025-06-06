# MTLStructType

**Framework**: Metal  
**Kind**: class

A description of a structure.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
class MTLStructType
```

#### Overview

[`MTLStructType`](mtlstructtype.md) is part of the reflection API that allows Metal framework code to query details of a struct that is passed as an argument of a Metal shading language function. Don’t create [`MTLStructType`](mtlstructtype.md) objects directly; instead query the [`bufferStructType`](mtlargument/bufferstructtype.md) property of a [`MTLArgument`](mtlargument.md) object, or call the [`structType()`](mtlstructmember/structtype().md) method for a [`MTLStructMember`](mtlstructmember.md) object. To examine the details of the struct, you can recursively drill down the [`members`](mtlstructtype/members.md) property of the [`MTLStructType`](mtlstructtype.md) object, which contains details about struct members, each of which is represented by a [`MTLStructMember`](mtlstructmember.md) object.

## Topics

### Obtaining Information about Struct Members
- [var members: [MTLStructMember]](mtlstructtype/members.md)
  An array of objects that describe the fields in the struct.
- [func memberByName(String) -> MTLStructMember?](mtlstructtype/memberbyname(_:).md)
  Provides a representation of a struct member.

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
- [class MTLStructMember](mtlstructmember.md)
  An object that provides information about a field in a structure.
- [class MTLPointerType](mtlpointertype.md)
  A description of a pointer.
- [class MTLTextureReferenceType](mtltexturereferencetype.md)
  A description of a texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlstructtype)*
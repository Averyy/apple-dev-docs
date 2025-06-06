# dataType

**Framework**: Metal  
**Kind**: property

The data type of the struct member.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var dataType: MTLDataType { get }
```

#### Discussion

For information on possible values, see [`MTLDataType`](mtldatatype.md). If the value is [`MTLDataType.array`](mtldatatype/array.md), then the [`arrayType()`](mtlstructmember/arraytype().md) method returns an object that describes the underlying array. If the value is [`MTLDataType.struct`](mtldatatype/struct.md), then the [`structType()`](mtlstructmember/structtype().md) method returns an object that describes the underlying struct.

## See Also

- [var name: String](mtlstructmember/name.md)
  The name of the struct member.
- [var offset: Int](mtlstructmember/offset.md)
  The location of this member relative to the start of its struct, in bytes.
- [var argumentIndex: Int](mtlstructmember/argumentindex.md)
  The index in the argument table that corresponds to the struct member.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlstructmember/datatype)*
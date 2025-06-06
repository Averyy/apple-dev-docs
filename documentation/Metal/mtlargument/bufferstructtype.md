# bufferStructType

**Framework**: Metal  
**Kind**: property

A description of the structure data of a buffer argument.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var bufferStructType: MTLStructType? { get }
```

#### Discussion

If the buffer data type is [`MTLDataType.struct`](mtldatatype/struct.md), this property describes the type of the struct; otherwise, this property is `nil`.

## See Also

- [var bufferAlignment: Int](mtlargument/bufferalignment.md)
  The required byte alignment in memory for the buffer data.
- [var bufferDataSize: Int](mtlargument/bufferdatasize.md)
  The size, in bytes, of the buffer data.
- [var bufferDataType: MTLDataType](mtlargument/bufferdatatype.md)
  The data type of the buffer data.
- [var bufferPointerType: MTLPointerType?](mtlargument/bufferpointertype.md)
  A description of the pointer to a buffer argument.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlargument/bufferstructtype)*
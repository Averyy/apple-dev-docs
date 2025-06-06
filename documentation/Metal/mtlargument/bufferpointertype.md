# bufferPointerType

**Framework**: Metal  
**Kind**: property

A description of the pointer to a buffer argument.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var bufferPointerType: MTLPointerType? { get }
```

#### Discussion

This property describes the type of the pointer to the buffer.

## See Also

- [var bufferAlignment: Int](mtlargument/bufferalignment.md)
  The required byte alignment in memory for the buffer data.
- [var bufferDataSize: Int](mtlargument/bufferdatasize.md)
  The size, in bytes, of the buffer data.
- [var bufferDataType: MTLDataType](mtlargument/bufferdatatype.md)
  The data type of the buffer data.
- [var bufferStructType: MTLStructType?](mtlargument/bufferstructtype.md)
  A description of the structure data of a buffer argument.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlargument/bufferpointertype)*
# bufferDataType

**Framework**: Metal  
**Kind**: property

The data type of the buffer data.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var bufferDataType: MTLDataType { get }
```

#### Discussion

If the argument is not a buffer, querying this property is a fatal error.

## See Also

- [var bufferAlignment: Int](mtlargument/bufferalignment.md)
  The required byte alignment in memory for the buffer data.
- [var bufferDataSize: Int](mtlargument/bufferdatasize.md)
  The size, in bytes, of the buffer data.
- [var bufferStructType: MTLStructType?](mtlargument/bufferstructtype.md)
  A description of the structure data of a buffer argument.
- [var bufferPointerType: MTLPointerType?](mtlargument/bufferpointertype.md)
  A description of the pointer to a buffer argument.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlargument/bufferdatatype)*
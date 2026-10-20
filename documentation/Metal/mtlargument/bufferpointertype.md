# bufferPointerType

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

A description of the pointer to a buffer argument.

**Availability**:
- iOS 11.0+ - Deprecated in 16.0
- iPadOS 11.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.13+ - Deprecated in 13.0
- tvOS 11.0+ - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
var bufferPointerType: MTLPointerType? { get }
```

```objc
@property (readonly, nullable) MTLPointerType * bufferPointerType;
```

#### Discussion

This property describes the type of the pointer to the buffer.

## See Also

### Describing a buffer argument
- [var bufferAlignment: Int](./bufferalignment.md)
  The required byte alignment in memory for the buffer data.
- [var bufferDataSize: Int](./bufferdatasize.md)
  The size, in bytes, of the buffer data.
- [var bufferDataType: MTLDataType](./bufferdatatype.md)
  The data type of the buffer data.
- [var bufferStructType: MTLStructType?](./bufferstructtype.md)
  A description of the structure data of a buffer argument.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlargument/bufferpointertype)*
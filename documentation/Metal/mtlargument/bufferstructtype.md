# bufferStructType

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

A description of the structure data of a buffer argument.

**Availability**:
- iOS 8.0+ - Deprecated in 16.0
- iPadOS 8.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.11+ - Deprecated in 13.0
- tvOS - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
var bufferStructType: MTLStructType? { get }
```

```objc
@property (readonly, nullable) MTLStructType * bufferStructType;
```

#### Discussion

If the buffer data type is [`MTLDataType.struct`](../mtldatatype/struct.md), this property describes the type of the struct; otherwise, this property is `nil`.

## See Also

### Describing a buffer argument
- [var bufferAlignment: Int](./bufferalignment.md)
  The required byte alignment in memory for the buffer data.
- [var bufferDataSize: Int](./bufferdatasize.md)
  The size, in bytes, of the buffer data.
- [var bufferDataType: MTLDataType](./bufferdatatype.md)
  The data type of the buffer data.
- [var bufferPointerType: MTLPointerType?](./bufferpointertype.md)
  A description of the pointer to a buffer argument.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlargument/bufferstructtype)*
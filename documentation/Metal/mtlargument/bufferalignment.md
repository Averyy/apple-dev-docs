# bufferAlignment

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The required byte alignment in memory for the buffer data.

**Availability**:
- iOS 8.0+ - Deprecated in 16.0
- iPadOS 8.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.11+ - Deprecated in 13.0
- tvOS - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
var bufferAlignment: Int { get }
```

```objc
@property (readonly) NSUInteger bufferAlignment;
```

#### Discussion

If the argument is not a buffer, querying this property is a fatal error.

## See Also

### Describing a buffer argument
- [var bufferDataSize: Int](./bufferdatasize.md)
  The size, in bytes, of the buffer data.
- [var bufferDataType: MTLDataType](./bufferdatatype.md)
  The data type of the buffer data.
- [var bufferStructType: MTLStructType?](./bufferstructtype.md)
  A description of the structure data of a buffer argument.
- [var bufferPointerType: MTLPointerType?](./bufferpointertype.md)
  A description of the pointer to a buffer argument.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlargument/bufferalignment)*
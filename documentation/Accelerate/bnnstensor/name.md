# name

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

An optional name for the tensor that you can use for debugging.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var name: UnsafePointer<CChar>?
```

```c
const char * name;
```

## See Also

### Specifying a tensor’s properties
- [var data_type: BNNSDataType](./data_type.md)
  The data type of the tensor.
- [var rank: UInt8](./rank.md)
  The rank of the tensor.
- [var shape: (Int, Int, Int, Int, Int, Int, Int, Int)](./shape.md)
  A tuple of unsigned-integer elements that specify the size of the tensor.
- [var stride: (Int, Int, Int, Int, Int, Int, Int, Int)](./stride.md)
  A tuple of unsigned-integer elements that specify the stride of the tensor.
- [var data: UnsafeMutableRawPointer?](./data.md)
  A pointer to the memory that contains the tensor values.
- [var data_size_in_bytes: Int](./data_size_in_bytes.md)
  The size, in bytes, of the memory that contains the tensor values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnstensor/name)*
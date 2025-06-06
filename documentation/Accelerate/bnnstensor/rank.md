# rank

**Framework**: Accelerate  
**Kind**: property

The rank of the tensor.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var rank: UInt8
```

#### Discussion

This value must be greater than or equal to zero, and less than or equal to `BNNS_MAX_TENSOR_DIMENSION`.

## See Also

- [var data_type: BNNSDataType](bnnstensor/data_type.md)
  The data type of the tensor.
- [var shape: (Int, Int, Int, Int, Int, Int, Int, Int)](bnnstensor/shape.md)
  A tuple of unsigned-integer elements that specify the size of the tensor.
- [var stride: (Int, Int, Int, Int, Int, Int, Int, Int)](bnnstensor/stride.md)
  A tuple of unsigned-integer elements that specify the stride of the tensor.
- [var data: UnsafeMutableRawPointer?](bnnstensor/data.md)
  A pointer to the memory that contains the tensor values.
- [var data_size_in_bytes: Int](bnnstensor/data_size_in_bytes.md)
  The size, in bytes, of the memory that contains the tensor values.
- [var name: UnsafePointer<CChar>?](bnnstensor/name.md)
  An optional name for the tensor that you can use for debugging.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnstensor/rank)*
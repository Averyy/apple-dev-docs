# init(data_type:rank:shape:stride:data:data_size_in_bytes:name:)

**Framework**: Accelerate  
**Kind**: init

Creates a tensor with the specified properties.

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
init(data_type: BNNSDataType, rank: UInt8, shape: (Int, Int, Int, Int, Int, Int, Int, Int), stride: (Int, Int, Int, Int, Int, Int, Int, Int), data: UnsafeMutableRawPointer?, data_size_in_bytes: Int, name: UnsafePointer<CChar>?)
```

## Parameters

- `data_type`: The data type of the tensor.
- `rank`: The rank of the tensor. This value must be greater than or equal to zero, and less than or equal to `BNNS_MAX_TENSOR_DIMENSION`.
- `shape`: A tuple of unsigned-integer elements. The first [`rank`](bnnstensor/rank.md) element that specify the size of each dimension.
- `stride`: A tuple of unsigned-integer elements. The first [`rank`](bnnstensor/rank.md) element that specify the stride of each dimension.
- `data`: A pointer to the memory that contains the tensor values.
- `data_size_in_bytes`: The extent of [`data`](bnnstensor/data.md) that BNNS uses for bounds checking.
- `name`: An optional name for the tensor that you can use for debugging.

## See Also

- [init()](bnnstensor/init.md)
  Creates an empty tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnstensor/init(data_type:rank:shape:stride:data:data_size_in_bytes:name:))*
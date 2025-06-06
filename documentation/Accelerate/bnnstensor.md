# BNNSTensor

**Framework**: Accelerate  
**Kind**: struct

A structure that describes the shape, stride, data type, and, optionally, the memory location of an n-dimensional array.

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
struct BNNSTensor
```

## Topics

### Initializers
- [init()](bnnstensor/init.md)
  Creates an empty tensor.
- [init(data_type: BNNSDataType, rank: UInt8, shape: (Int, Int, Int, Int, Int, Int, Int, Int), stride: (Int, Int, Int, Int, Int, Int, Int, Int), data: UnsafeMutableRawPointer?, data_size_in_bytes: Int, name: UnsafePointer<CChar>?)](bnnstensor/init(data_type:rank:shape:stride:data:data_size_in_bytes:name:).md)
  Creates a tensor with the specified properties.
### Specifying a tensor’s properties
- [var data_type: BNNSDataType](bnnstensor/data_type.md)
  The data type of the tensor.
- [var rank: UInt8](bnnstensor/rank.md)
  The rank of the tensor.
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

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [func BNNSTensorGetAllocationSize(UnsafePointer<BNNSTensor>) -> Int](bnnstensorgetallocationsize(_:).md)
  Returns the minimum allocation size, in bytes, of the specified tensor.
- [func BNNSGraphContextGetTensor(bnns_graph_context_t, UnsafePointer<CChar>?, UnsafePointer<CChar>, Bool, UnsafeMutablePointer<BNNSTensor>) -> Int32](bnnsgraphcontextgettensor(_:_:_:_:_:).md)
  Sets the properties of a tensor for the specified function argument.
- [func BNNSGraphTensorFillStrides(bnns_graph_t, UnsafePointer<CChar>?, UnsafePointer<CChar>, UnsafeMutablePointer<BNNSTensor>) -> Int32](bnnsgraphtensorfillstrides(_:_:_:_:).md)
  Sets the stride of the specifed tensor for compatibility with the given model’s input or output argument based on its current shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnstensor)*
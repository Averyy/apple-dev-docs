# init(flags:layout:size:stride:data:data_type:table_data:table_data_type:data_scale:data_bias:)

**Framework**: Accelerate  
**Kind**: init

Returns a new n-dimensional array descriptor with the specified parameters.

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
init(flags: BNNSNDArrayFlags, layout: BNNSDataLayout, size: (Int, Int, Int, Int, Int, Int, Int, Int), stride: (Int, Int, Int, Int, Int, Int, Int, Int), data: UnsafeMutableRawPointer?, data_type: BNNSDataType, table_data: UnsafeMutableRawPointer?, table_data_type: BNNSDataType, data_scale: Float, data_bias: Float)
```

## Parameters

- `flags`: Flags that control some behaviors of the n-dimensional array.
- `layout`: The dimension of the n-dimensional array.
- `size`: The number of values in each dimension.
- `stride`: The increment, in values, between values in each dimension.
- `data`: A pointer that is optional and points to the underlying data.
- `data_type`: The data type of the n-dimensional array.
- `table_data`: The lookup table for indexed data types.
- `table_data_type`: The data type of the lookup table.
- `data_scale`: The scale you use to convert integer and unsigned integer data to floating point.
- `data_bias`: The bias you use to convert integer and unsigned integer data to floating point.

## See Also

- [init?(data: UnsafeMutableRawBufferPointer, scalarType: any BNNSScalar.Type, shape: BNNS.Shape)](bnnsndarraydescriptor/init(data:scalartype:shape:).md)
  Returns a new n-dimensional array descriptor that references the same data as the specified raw pointer.
- [init?<T>(data: UnsafeMutableBufferPointer<T>, shape: BNNS.Shape)](bnnsndarraydescriptor/init(data:shape:).md)
  Returns a new n-dimensional array descriptor that references the same data as the specified pointer.
- [init(dataType: BNNSDataType, shape: BNNS.Shape)](bnnsndarraydescriptor/init(datatype:shape:).md)
  Returns a new n-dimensional array descriptor from the specified data type and shape.
- [init()](bnnsndarraydescriptor/init.md)
  Returns a new n-dimensional array descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsndarraydescriptor/init(flags:layout:size:stride:data:data_type:table_data:table_data_type:data_scale:data_bias:))*
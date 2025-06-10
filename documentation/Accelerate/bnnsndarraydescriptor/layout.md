# layout

**Framework**: Accelerate  
**Kind**: property

The dimension of the n-dimensional array.

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
var layout: BNNSDataLayout
```

## See Also

- [var flags: BNNSNDArrayFlags](bnnsndarraydescriptor/flags.md)
  Flags that control some behaviors of the n-dimensional array.
- [var size: (Int, Int, Int, Int, Int, Int, Int, Int)](bnnsndarraydescriptor/size.md)
  The number of values in each dimension.
- [var stride: (Int, Int, Int, Int, Int, Int, Int, Int)](bnnsndarraydescriptor/stride.md)
  The increment, in values, between consecutive elements in each dimension.
- [var data: UnsafeMutableRawPointer?](bnnsndarraydescriptor/data.md)
  A pointer that is optional and points to the underlying data.
- [var data_type: BNNSDataType](bnnsndarraydescriptor/data_type.md)
  The data type of the n-dimensional array.
- [var table_data: UnsafeMutableRawPointer?](bnnsndarraydescriptor/table_data.md)
  The lookup table for indexed data types.
- [var table_data_type: BNNSDataType](bnnsndarraydescriptor/table_data_type.md)
  The data type of the lookup table.
- [var data_scale: Float](bnnsndarraydescriptor/data_scale.md)
  The scale you use to convert integer and unsigned integer data to floating point.
- [var data_bias: Float](bnnsndarraydescriptor/data_bias.md)
  The bias you use to convert integer and unsigned integer data to floating point.
- [var shape: BNNS.Shape](bnnsndarraydescriptor/shape.md)
  The shape of the n-dimensional array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsndarraydescriptor/layout)*
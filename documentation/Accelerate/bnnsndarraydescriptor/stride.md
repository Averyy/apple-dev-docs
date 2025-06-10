# stride

**Framework**: Accelerate  
**Kind**: property

The increment, in values, between consecutive elements in each dimension.

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
var stride: (Int, Int, Int, Int, Int, Int, Int, Int)
```

#### Discussion

Specify the stride of an array descriptor the define the increment between neighboring elements in each dimension. For example, the following values represent a 2D row-major matrix:

```swift
[ 10, 20, 30,
  40, 50, 60,
  70, 80, 90 ]
```

The stride for the first dimension is `1`, for example, the increment between `50` and `60` is a single element. The stride for the second dimension is `3`, for example, the stride between `50` and `80` is three elements.

## See Also

- [var flags: BNNSNDArrayFlags](bnnsndarraydescriptor/flags.md)
  Flags that control some behaviors of the n-dimensional array.
- [var layout: BNNSDataLayout](bnnsndarraydescriptor/layout.md)
  The dimension of the n-dimensional array.
- [var size: (Int, Int, Int, Int, Int, Int, Int, Int)](bnnsndarraydescriptor/size.md)
  The number of values in each dimension.
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

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsndarraydescriptor/stride)*
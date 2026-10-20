# shape

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The shape of the n-dimensional array.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS
- watchOS 7.0+

## Declaration

```swift
var shape: BNNS.Shape { get }
```

## See Also

### Accessing the Properties of an Array Descriptor
- [var flags: BNNSNDArrayFlags](./flags.md)
  Flags that control some behaviors of the n-dimensional array.
- [var layout: BNNSDataLayout](./layout.md)
  The dimension of the n-dimensional array.
- [var size: (Int, Int, Int, Int, Int, Int, Int, Int)](./size.md)
  The number of values in each dimension.
- [var stride: (Int, Int, Int, Int, Int, Int, Int, Int)](./stride.md)
  The increment, in values, between consecutive elements in each dimension.
- [var data: UnsafeMutableRawPointer?](./data.md)
  A pointer that is optional and points to the underlying data.
- [var data_type: BNNSDataType](./data_type.md)
  The data type of the n-dimensional array.
- [var table_data: UnsafeMutableRawPointer?](./table_data.md)
  The lookup table for indexed data types.
- [var table_data_type: BNNSDataType](./table_data_type.md)
  The data type of the lookup table.
- [var data_scale: Float](./data_scale.md)
  The scale you use to convert integer and unsigned integer data to floating point.
- [var data_bias: Float](./data_bias.md)
  The bias you use to convert integer and unsigned integer data to floating point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsndarraydescriptor/shape)*
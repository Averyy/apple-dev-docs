# init(dataType:shape:)

**Framework**: Accelerate  
**Kind**: init

Returns a new n-dimensional array descriptor from the specified data type and shape.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
init(dataType: BNNSDataType, shape: BNNS.Shape)
```

## Parameters

- `dataType`: The data type of the data.
- `shape`: The shape of the n-dimensional array descriptor.

## See Also

- [init(flags: BNNSNDArrayFlags, layout: BNNSDataLayout, size: (Int, Int, Int, Int, Int, Int, Int, Int), stride: (Int, Int, Int, Int, Int, Int, Int, Int), data: UnsafeMutableRawPointer?, data_type: BNNSDataType, table_data: UnsafeMutableRawPointer?, table_data_type: BNNSDataType, data_scale: Float, data_bias: Float)](bnnsndarraydescriptor/init(flags:layout:size:stride:data:data_type:table_data:table_data_type:data_scale:data_bias:).md)
  Returns a new n-dimensional array descriptor with the specified parameters.
- [init?(data: UnsafeMutableRawBufferPointer, scalarType: any BNNSScalar.Type, shape: BNNS.Shape)](bnnsndarraydescriptor/init(data:scalartype:shape:).md)
  Returns a new n-dimensional array descriptor that references the same data as the specified raw pointer.
- [init?<T>(data: UnsafeMutableBufferPointer<T>, shape: BNNS.Shape)](bnnsndarraydescriptor/init(data:shape:).md)
  Returns a new n-dimensional array descriptor that references the same data as the specified pointer.
- [init()](bnnsndarraydescriptor/init.md)
  Returns a new n-dimensional array descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsndarraydescriptor/init(datatype:shape:))*
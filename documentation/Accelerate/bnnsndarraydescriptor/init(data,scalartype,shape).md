# init(data:scalarType:shape:)

**Framework**: Accelerate  
**Kind**: init  
**Role**: Initializer

Returns a new n-dimensional array descriptor that references the same data as the specified raw pointer.

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
init?(data: UnsafeMutableRawBufferPointer, scalarType: any BNNSScalar.Type, shape: BNNS.Shape)
```

## Parameters

- `data`: A pointer to the underlying data.
- `scalarType`: The data type of the data.
- `shape`: The shape of the n-dimensional array descriptor.

## See Also

### Creating an Array Descriptor
- [init(flags: BNNSNDArrayFlags, layout: BNNSDataLayout, size: (Int, Int, Int, Int, Int, Int, Int, Int), stride: (Int, Int, Int, Int, Int, Int, Int, Int), data: UnsafeMutableRawPointer?, data_type: BNNSDataType, table_data: UnsafeMutableRawPointer?, table_data_type: BNNSDataType, data_scale: Float, data_bias: Float)](./init%28flags,layout,size,stride,data,data_type,table_data,table_data_type,data_scale,data_bias%29.md)
  Returns a new n-dimensional array descriptor with the specified parameters.
- [init?<T>(data: UnsafeMutableBufferPointer<T>, shape: BNNS.Shape)](./init%28data,shape%29.md)
  Returns a new n-dimensional array descriptor that references the same data as the specified pointer.
- [init(dataType: BNNSDataType, shape: BNNS.Shape)](./init%28datatype,shape%29.md)
  Returns a new n-dimensional array descriptor from the specified data type and shape.
- [init()](./init%28%29.md)
  Returns a new n-dimensional array descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsndarraydescriptor/init(data:scalartype:shape:))*
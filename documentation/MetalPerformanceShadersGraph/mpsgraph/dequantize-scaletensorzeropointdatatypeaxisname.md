# dequantize(_:scaleTensor:zeroPoint:dataType:axis:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates Dequantize operation and returns the result tensor.

**Availability**:
- iOS 16.2+
- iPadOS 16.2+
- Mac Catalyst 16.2+
- macOS 13.1+
- tvOS 16.2+
- visionOS 1.0+

## Declaration

```swift
func dequantize(_ tensor: MPSGraphTensor, scaleTensor: MPSGraphTensor, zeroPoint: Double, dataType: MPSDataType, axis: Int, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor array of datatype dataType

#### Discussion

Convert the quantized `tensor` to a float tensor by applying a scale + bias transform: result = scaleTensor * (tensor - zeroPoint)

Supported input types: `MPSDataTypeInt4`, `MPSDataTypeUInt4`, `MPSDataTypeInt8`, `MPSDataTypeUInt8`, `MPSDataTypeFloat8E4M3`, `MPSDataTypeFloat8E5M2`. The `scaleTensor` type and `dataType` must match (`MPSDataTypeFloat16`, `MPSDataTypeFloat32`, or `MPSDataTypeBFloat16`).

## Parameters

- `tensor`: Input tensor to be dequantized
- `scaleTensor`: Scale scalar or 1D Tensor parameter with size == tensor.shape[axis]
- `zeroPoint`: Bias scalar parameter (converted to dataType of tensor)
- `dataType`: Float data type of the result tensor.
- `axis`: Axis on which the scale 1D value is being broadcasted
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/dequantize(_:scaletensor:zeropoint:datatype:axis:name:))*
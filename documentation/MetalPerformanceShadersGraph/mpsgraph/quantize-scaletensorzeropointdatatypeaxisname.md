# quantize(_:scaleTensor:zeroPoint:dataType:axis:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a Quantize operation and returns the result tensor.

**Availability**:
- iOS 16.2+
- iPadOS 16.2+
- Mac Catalyst 16.2+
- macOS 13.1+
- tvOS 16.2+
- visionOS 1.0+

## Declaration

```swift
func quantize(_ tensor: MPSGraphTensor, scaleTensor: MPSGraphTensor, zeroPoint: Double, dataType: MPSDataType, axis: Int, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor array of datatype dataType

#### Discussion

Convert the float `tensor` to a quantized tensor by applying a scale + bias transform: result = round(tensor / scaleTensor) + zeroPoint

## Parameters

- `tensor`: Input tensor to be quantized
- `scaleTensor`: Scale 1D Tensor parameter with size == tensor.shape[axis]
- `zeroPoint`: Bias scalar parameter (converted to dataType of resultTensor)
- `dataType`: Data type of the result tensor. Supports `MPSDataTypeInt8`, `MPSDataTypeUInt8`, `MPSDataTypeFloat8E4M3`, and `MPSDataTypeFloat8E5M2`. Float8 output requires symmetric quantization (zeroPoint = 0).
- `axis`: Axis on which the scale 1D value is being broadcasted
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/quantize(_:scaletensor:zeropoint:datatype:axis:name:))*
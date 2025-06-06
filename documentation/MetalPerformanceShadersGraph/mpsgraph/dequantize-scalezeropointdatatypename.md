# dequantize(_:scale:zeroPoint:dataType:name:)

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
func dequantize(_ tensor: MPSGraphTensor, scale: Double, zeroPoint: Double, dataType: MPSDataType, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor array of datatype dataType

#### Discussion

Convert the i8 or u8 `tensor` to a float tensor by applying a scale + bias transform: result = scale(tensor - zeroPoint)

## Parameters

- `tensor`: Input tensor to be dequantized
- `scale`: Scale scalar parameter
- `zeroPoint`: Bias scalar parameter (converted to dataType of tensor)
- `dataType`: Float data type of the result tensor.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/dequantize(_:scale:zeropoint:datatype:name:))*
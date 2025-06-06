# dequantize(_:scaleTensor:dataType:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a dequantize operation and returns the result tensor.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func dequantize(_ tensor: MPSGraphTensor, scaleTensor: MPSGraphTensor, dataType: MPSDataType, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid [`MPSGraphTensor`](mpsgraphtensor.md) array of datatype `dataType`.

#### Discussion

Converts the i8, u8, i4 or u4 `tensor` to a float tensor by applying a scale and bias transform:

```md
result = scaleTensor * tensor.
```

## Parameters

- `tensor`: Input tensor to be dequantized.
- `scaleTensor`: Scale Tensor parameter with groups support.
- `dataType`: Float data type of the result tensor.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/dequantize(_:scaletensor:datatype:name:))*
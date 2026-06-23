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

Converts the quantized `tensor` to a float tensor by applying a scale transform (symmetric — zero point is implicitly 0):

```md
result = scaleTensor * tensor
```

The quantization mode is determined by the element type of `scaleTensor`:

**Regular blockwise** (`scaleTensor` type is an MPSGraph float type):

- Supported input types: `MPSDataTypeInt4`, `MPSDataTypeUInt4`, `MPSDataTypeInt8`, `MPSDataTypeUInt8`, `MPSDataTypeFloat8E4M3`, `MPSDataTypeFloat8E5M2`.
- `scaleTensor` shape: leading dims of `tensor` with the last dim replaced by `tensor.shape[last] / blockSize`.

**MX mode** (`scaleTensor` type is `MPSDataTypeFloat8E8M0`):

- Supported input types: `MPSDataTypeFloat4E2M1`, `MPSDataTypeFloat8E4M3`, `MPSDataTypeFloat8E5M2`.
- Block size 32.

**F4 with F8E4M3 scale** (`scaleTensor` type is `MPSDataTypeFloat8E4M3`, input type is `MPSDataTypeFloat4E2M1`):

- Block size 16.

## Parameters

- `tensor`: Input tensor to be dequantized.
- `scaleTensor`: Scale Tensor parameter with groups support.
- `dataType`: Float data type of the result tensor.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/dequantize(_:scaletensor:datatype:name:))*
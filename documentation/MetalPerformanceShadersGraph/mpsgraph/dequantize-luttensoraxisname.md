# dequantize(_:LUTTensor:axis:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a vector lookup-table based quantization operation and returns the result tensor.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func dequantize(_ tensor: MPSGraphTensor, LUTTensor: MPSGraphTensor, axis: Int, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid [`MPSGraphTensor`](mpsgraphtensor.md) object.

#### Discussion

Converts a u8 or u4 `tensor` to a float tensor by applying a lookup operation, where each input index defines a vector of values. The operation reads the vector values from the last dimension of the lookup table tensor and stores them into the dimension defined by `axis` on the result tensor.

```md
result[i1, ... , i_axis, ..., in] = LUTTensor[i1', ..., in', tensor[i1, ..., in], i_axis]
```

Note: The operation supports LUT groups up to the last 2 dimensions for `tensor`.

## Parameters

- `tensor`: Input tensor to be dequantized.
- `LUTTensor`: The lookup table to use - for u4 the second to last dimension should have 16 elements, and for u8 256 elements.
- `axis`: Axis on which the scale 1D value is being broadcasted.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/dequantize(_:luttensor:axis:name:))*
# normalize(_:mean:variance:gamma:beta:epsilon:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a batch normalization operation and returns the result tensor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func normalize(_ tensor: MPSGraphTensor, mean: MPSGraphTensor, variance: MPSGraphTensor, gamma: MPSGraphTensor?, beta: MPSGraphTensor?, epsilon: Float, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid `MPSGraphTensor` object.

#### Discussion

The mean and variance tensors should be outputs of `meanWithTensor:axes:name` and `varianceWithTensor:meanTensor:axes:name`. Use the axes parameter to achieve different types of normalizations. For example (assuming your data is in NxHxWxC format) Batch normalization: axes = [0, 1, 2] Instance normalization: axes = [1, 2] Shapes for gamma and beta must match the input data along at least one dimension and will be broadcast along the rest. For batch normalization, gamma and beta would typically be 1x1x1xC i.e. one value per channel.

## Parameters

- `tensor`: The input tensor.
- `mean`: The mean tensor.
- `variance`: The variance tensor.
- `gamma`: The tensor used to scale the normalized result.
- `beta`: The tensor used to bias the normalized result.
- `epsilon`: A small value to add to the variance when normalizing the inputs.
- `name`: An optional name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/normalize(_:mean:variance:gamma:beta:epsilon:name:))*
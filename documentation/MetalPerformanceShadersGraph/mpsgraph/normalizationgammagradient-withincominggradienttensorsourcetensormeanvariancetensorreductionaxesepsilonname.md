# normalizationGammaGradient(withIncomingGradientTensor:sourceTensor:mean:varianceTensor:reductionAxes:epsilon:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a normalization gamma-gradient operation and returns the result tensor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func normalizationGammaGradient(withIncomingGradientTensor incomingGradientTensor: MPSGraphTensor, sourceTensor: MPSGraphTensor, mean meanTensor: MPSGraphTensor, varianceTensor: MPSGraphTensor, reductionAxes axes: [NSNumber], epsilon: Float, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid `MPSGraphTensor` object.

#### Discussion

The mean and variance tensors should be outputs of `meanWithTensor:axes:name` and `varianceWithTensor:meanTensor:axes:name`. Use the axes parameter to achieve different types of normalizations. For example (assuming your data is in `NxHxWxC` format) Batch normalization: axes = [0, 1, 2] Instance normalization: axes = [1, 2]

## Parameters

- `incomingGradientTensor`: The incoming original   gradient.
- `sourceTensor`: The original input source in forward direction.
- `meanTensor`: The mean tensor.
- `varianceTensor`: The variance tensor.
- `axes`: The axes of normalization.
- `epsilon`: A small value to add to the variance when normalizing the inputs.
- `name`: An optional name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/normalizationgammagradient(withincominggradienttensor:sourcetensor:mean:variancetensor:reductionaxes:epsilon:name:))*
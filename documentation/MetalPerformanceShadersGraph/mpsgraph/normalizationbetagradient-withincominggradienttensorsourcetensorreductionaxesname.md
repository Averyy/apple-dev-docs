# normalizationBetaGradient(withIncomingGradientTensor:sourceTensor:reductionAxes:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a normalization beta-gradient operation and returns the result tensor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func normalizationBetaGradient(withIncomingGradientTensor incomingGradientTensor: MPSGraphTensor, sourceTensor: MPSGraphTensor, reductionAxes axes: [NSNumber], name: String?) -> MPSGraphTensor
```

#### Return Value

A valid `MPSGraphTensor` object.

#### Discussion

The mean and variance tensors should be outputs of `meanWithTensor:axes:name` and `varianceWithTensor:meanTensor:axes:name`. Use the axes parameter to achieve different types of normalizations. For example (assuming your data is in `NxHxWxC` format) Batch normalization: axes = [0, 1, 2] Instance normalization: axes = [1, 2]

## Parameters

- `incomingGradientTensor`: The incoming original   gradient.
- `sourceTensor`: The original input source in forward direction.
- `axes`: The axes of normalization.
- `name`: An optional name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/normalizationbetagradient(withincominggradienttensor:sourcetensor:reductionaxes:name:))*
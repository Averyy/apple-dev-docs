# init(normalizedShape:beta:gamma:varianceEpsilon:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates a normalization layer with a shape, optional beta and gamma tensors, and variance epsilon you specify.

**Availability**:
- iOS 14.5+ - Deprecated in 17.0
- iPadOS 14.5+ - Deprecated in 17.0
- Mac Catalyst 14.5+ - Deprecated in 17.0
- macOS 11.3+ - Deprecated in 14.0
- tvOS 14.5+ - Deprecated in 17.0

> **Deprecated**: Use Metal Performance Shaders Graph or BNNS instead.

## Declaration

```swift
convenience init?(normalizedShape: [Int], beta: MLCTensor?, gamma: MLCTensor?, varianceEpsilon: Float)
```

## Parameters

- `normalizedShape`: The shape of the axes where normalization occurs.
- `beta`: The beta tensor.
- `gamma`: The gamma tensor.
- `varianceEpsilon`: The variance epsilon you use for numerical stability.

## See Also

### Creating Layer Normalization Layers
- [convenience init?(normalizedShape: [Int], beta: MLCTensor, gamma: MLCTensor, varianceEpsilon: Float)](./init%28normalizedshape,beta,gamma,varianceepsilon%29-5i2aa.md)
  Creates a normalization layer with a shape, beta and gamma tensors, and variance epsilon you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlclayernormalizationlayer/init(normalizedshape:beta:gamma:varianceepsilon:)-28e6g)*
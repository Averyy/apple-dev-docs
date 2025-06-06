# init(normalizedShape:beta:gamma:varianceEpsilon:)

**Framework**: ML Compute  
**Kind**: init

Creates a normalization layer with a shape, optional beta and gamma tensors, and variance epsilon you specify.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- tvOS 14.5+

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

- [convenience init?(normalizedShape: [Int], beta: MLCTensor, gamma: MLCTensor, varianceEpsilon: Float)](mlclayernormalizationlayer/init(normalizedshape:beta:gamma:varianceepsilon:)-5i2aa.md)
  Creates a normalization layer with a shape, beta and gamma tensors, and variance epsilon you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlclayernormalizationlayer/init(normalizedshape:beta:gamma:varianceepsilon:)-28e6g)*
# layerWithNormalizedShape:beta:gamma:varianceEpsilon:

**Framework**: ML Compute  
**Kind**: method  
**Role**: Type Method

Creates a normalization layer with a shape, beta and gamma tensors, and variance epsilon you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```objc
+ (instancetype) layerWithNormalizedShape:(NSArray<NSNumber *> *) normalizedShape beta:(MLCTensor *) beta gamma:(MLCTensor *) gamma varianceEpsilon:(float) varianceEpsilon;
```

## Return Value

A new [`MLCLayerNormalizationLayer`](../mlclayernormalizationlayer.md) instance.

## Parameters

- `normalizedShape`: The shape of the axes where normalization occurs.
- `beta`: The beta tensor.
- `gamma`: The gamma tensor.
- `varianceEpsilon`: The variance epsilon you use for numerical stability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlclayernormalizationlayer/layerwithnormalizedshape:beta:gamma:varianceepsilon:)*
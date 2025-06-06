# appending(_:)

**Framework**: Create ML Components  
**Kind**: method

Composes this tabular transformer with another tabular transformer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
func appending<Other>(_ other: Other) -> ComposedTabularTransformer<Self, Other> where Other : TabularTransformer
```

## See Also

- [func adaptedAsEstimator() -> TabularTransformerToEstimatorAdaptor<Self>](tabulartransformer/adaptedasestimator.md)
  Exposes this tabular transformer as a trivial tabular estimator.
- [func adaptedAsUpdatableEstimator() -> TabularTransformerToUpdatableEstimatorAdaptor<Self>](tabulartransformer/adaptedasupdatableestimator.md)
  Exposes this tabular transformer as an updatable tabular estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/tabulartransformer/appending(_:)-7d5ca)*
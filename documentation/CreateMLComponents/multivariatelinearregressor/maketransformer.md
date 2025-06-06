# makeTransformer()

**Framework**: Create ML Components  
**Kind**: method

Creates a default-initialized model suitable for incremental fitting.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func makeTransformer() -> MultivariateLinearRegressor<Scalar>.Model
```

## See Also

- [func update(inout MultivariateLinearRegressor<Scalar>.Model, with: some Sequence<AnnotatedFeature<MLShapedArray<Scalar>, MLShapedArray<Scalar>>>, eventHandler: EventHandler?) async throws](multivariatelinearregressor/update(_:with:eventhandler:).md)
  Updates a model with a new sequence of examples.
- [func update(inout MultivariateLinearRegressor<Scalar>.Model, with: AnnotatedBatch<Scalar>) async throws -> Scalar](multivariatelinearregressor/update(_:with:).md)
  Updates a model with a new shaped array of examples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/multivariatelinearregressor/maketransformer())*
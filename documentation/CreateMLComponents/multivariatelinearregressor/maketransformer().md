# makeTransformer()

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

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

Available when `Scalar` conforms to `MLShapedArrayScalar` and `BinaryFloatingPoint`.

## See Also

### Fitting Progressively
- [func update(inout MultivariateLinearRegressor<Scalar>.Model, with: some Sequence<AnnotatedFeature<MLShapedArray<Scalar>, MLShapedArray<Scalar>>>, eventHandler: EventHandler?) async throws](./update%28_,with,eventhandler%29.md)
  Updates a model with a new sequence of examples.
- [func update(inout MultivariateLinearRegressor<Scalar>.Model, with: AnnotatedBatch<Scalar>) async throws -> Scalar](./update%28_,with%29.md)
  Updates a model with a new shaped array of examples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/multivariatelinearregressor/maketransformer())*
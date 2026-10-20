# update(_:with:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

Updates a model with a new sequence of examples.

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
func update(_ model: inout MultivariateLinearRegressor<Scalar>.Model, with input: some Sequence<AnnotatedFeature<MLShapedArray<Scalar>, MLShapedArray<Scalar>>>, eventHandler: EventHandler? = nil) async throws
```

Available when `Scalar` conforms to `MLShapedArrayScalar` and `BinaryFloatingPoint`.

## Parameters

- `model`: A model to update.
- `input`: A sequence of examples. For faster updates, consider passing a single [`AnnotatedBatch`](../annotatedbatch.md) with shaped arrays that contain multiple training examples. For example instead of passing a sequence of `N` shaped arrays with shape `[M]`, pass a single shaped array with shape `[N, M]`. See also [`update(_:with:)`](./update%28_,with%29.md).
- `eventHandler`: An event handler. This method reports the mean squared error.

## See Also

### Fitting Progressively
- [func makeTransformer() -> MultivariateLinearRegressor<Scalar>.Model](./maketransformer%28%29.md)
  Creates a default-initialized model suitable for incremental fitting.
- [func update(inout MultivariateLinearRegressor<Scalar>.Model, with: AnnotatedBatch<Scalar>) async throws -> Scalar](./update%28_,with%29.md)
  Updates a model with a new shaped array of examples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/multivariatelinearregressor/update(_:with:eventhandler:))*
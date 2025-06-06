# update(_:with:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

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

## Parameters

- `model`: A model to update.
- `input`: A sequence of examples. For faster updates, consider passing a single   with   shaped arrays that contain multiple training examples. For example instead of passing a sequence of    shaped arrays with shape  , pass a single shaped array with shape  . See also   .
- `eventHandler`: An event handler. This method reports the mean squared error.

## See Also

- [func makeTransformer() -> MultivariateLinearRegressor<Scalar>.Model](multivariatelinearregressor/maketransformer.md)
  Creates a default-initialized model suitable for incremental fitting.
- [func update(inout MultivariateLinearRegressor<Scalar>.Model, with: AnnotatedBatch<Scalar>) async throws -> Scalar](multivariatelinearregressor/update(_:with:).md)
  Updates a model with a new shaped array of examples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/multivariatelinearregressor/update(_:with:eventhandler:))*
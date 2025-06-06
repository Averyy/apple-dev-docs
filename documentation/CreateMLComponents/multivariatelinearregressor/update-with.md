# update(_:with:)

**Framework**: Create ML Components  
**Kind**: method

Updates a model with a new shaped array of examples.

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
func update(_ model: inout MultivariateLinearRegressor<Scalar>.Model, with input: AnnotatedBatch<Scalar>) async throws -> Scalar
```

#### Return Value

The mean squared error for the batch, also known as the batch loss.

## Parameters

- `model`: A model to update.
- `input`: An annotated batch containing the features and annotations. The last dimension of the features is   the model’s input size and the last dimension of the annotations is the model’s output size. All the   leading dimensions of the features must match all leading dimensions of the annotations. For example, the   feature shape can be   and the annotation shape can be   for   examples where   is the   input size and   is the output size.

## See Also

- [func makeTransformer() -> MultivariateLinearRegressor<Scalar>.Model](multivariatelinearregressor/maketransformer.md)
  Creates a default-initialized model suitable for incremental fitting.
- [func update(inout MultivariateLinearRegressor<Scalar>.Model, with: some Sequence<AnnotatedFeature<MLShapedArray<Scalar>, MLShapedArray<Scalar>>>, eventHandler: EventHandler?) async throws](multivariatelinearregressor/update(_:with:eventhandler:).md)
  Updates a model with a new sequence of examples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/multivariatelinearregressor/update(_:with:))*
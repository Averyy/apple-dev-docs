# fitted(to:validateOn:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Fits a linear regressor model to shaped arrays of features and annotations.

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
func fitted(to input: AnnotatedBatch<Scalar>, validateOn validation: AnnotatedBatch<Scalar>?, eventHandler: EventHandler? = nil) async throws -> MultivariateLinearRegressor<Scalar>.Model
```

#### Return Value

The fitted model.

## Parameters

- `input`: An annotated batch containing the features and annotations. The last dimension of the features is   the model’s input size and the last dimension of the annotations is the model’s output size. All the   leading dimensions of the features must match all leading dimensions of the annotations. For example, the   feature shape can be   and the annotation shape can be   for   examples where   is the   input size and   is the output size.
- `validation`: An annotated batch containing the validation features and annotations. The last dimension of   the features must be   and the last dimension of the annotations must be  . All the   leading dimensions of the features must match all leading dimensions of the annotations.
- `eventHandler`: An event handler. This method reports the mean squared errors.

## See Also

- [func fitted(to: some Sequence<AnnotatedFeature<MLShapedArray<Scalar>, MLShapedArray<Scalar>>>, eventHandler: EventHandler?) async throws -> MultivariateLinearRegressor<Scalar>.Model](multivariatelinearregressor/fitted(to:eventhandler:).md)
  Fits a linear regressor model to a sequence of annotated features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/multivariatelinearregressor/fitted(to:validateon:eventhandler:))*
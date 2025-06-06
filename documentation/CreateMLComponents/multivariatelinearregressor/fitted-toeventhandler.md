# fitted(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Fits a linear regressor model to a sequence of annotated features.

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
func fitted(to input: some Sequence<AnnotatedFeature<MLShapedArray<Scalar>, MLShapedArray<Scalar>>>, eventHandler: EventHandler? = nil) async throws -> MultivariateLinearRegressor<Scalar>.Model
```

#### Return Value

The fitted linear regressor model.

## Parameters

- `input`: A sequence of examples used for fitting the regressor. For faster processing, instead of passing a   sequence of shaped arrays, consider passing a single shaped array containing all the training examples. For   example instead of passing   shaped arrays with shape  , pass a single shaped array with shape   . See  .
- `eventHandler`: An event handler. This method reports mean squared errors.

## See Also

- [func fitted(to: some Sequence<AnnotatedFeature<MLShapedArray<Scalar>, MLShapedArray<Scalar>>>, validateOn: some Sequence<AnnotatedFeature<MLShapedArray<Scalar>, MLShapedArray<Scalar>>>, eventHandler: EventHandler?) async throws -> MultivariateLinearRegressor<Scalar>.Model](multivariatelinearregressor/fitted(to:validateon:eventhandler:)-9bluu.md)
  Fits a linear regressor model to a sequence of annotated features.
- [func fitted(to: AnnotatedBatch<Scalar>, validateOn: AnnotatedBatch<Scalar>?, eventHandler: EventHandler?) async throws -> MultivariateLinearRegressor<Scalar>.Model](multivariatelinearregressor/fitted(to:validateon:eventhandler:)-82szq.md)
  Fits a linear regressor model to shaped arrays of features and annotations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/multivariatelinearregressor/fitted(to:eventhandler:))*
# fitted(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

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

- `input`: A sequence of examples used for fitting the regressor. For faster processing, instead of passing a sequence of shaped arrays, consider passing a single shaped array containing all the training examples. For example instead of passing `N` shaped arrays with shape `[M]`, pass a single shaped array with shape `[N, M]`. See [`fitted(to:validateOn:eventHandler:)`](./fitted%28to,validateon,eventhandler%29-82szq.md).
- `eventHandler`: An event handler. This method reports mean squared errors.

## See Also

### Fitting
- [func fitted(to:validateOn:eventHandler:)](./fitted%28to,validateon,eventhandler%29.md)
  Fits a linear regressor model to shaped arrays of features and annotations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/multivariatelinearregressor/fitted(to:eventhandler:))*